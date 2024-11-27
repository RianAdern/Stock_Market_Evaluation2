import streamlit as st
import yfinance as yf
import os
from datetime import datetime

def get_stock_data(stock_symbol, start_date, end_date):
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def save_data_to_csv(data, filename, directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the full path for the CSV file
    file_path = os.path.join(directory, filename)

    # Save the DataFrame to a CSV file
    data.to_csv(file_path)
    st.success(f"Data saved to {file_path}")


def Stock_dicionario(nomeStock):


    dicionario =[('S&P 500','^GSPC'),('Dow Jones Industrial Average','^DJI'),
                ('NASDAQ Composite','^IXIC'),('Nasdaq 100 Mar 24','NQ=F'),('Russell 2000','^RUT'),
                ('Crude Oil Apr 24','CL=F'),('Gold Apr 24 ','GC=F'),('Silver May 24','SI=F'),
                ('EUR/USD','EURUSD=X'),('GBP/USD','GBPUSD=X'),('USD/JPY','JPY=X'),('Bitcoin USD','BTC-USD'),
                ('FTSE 100 GBP','^FTSE'),('Nikkei 225 Osaka','^N225'),
                ('EUR/BRL','EURBRL=X'),('IBOVESPA','^BVSP'),('USD/BRL','BRL=X'),('IPC MEXICO','^MXX'),
                ]

    CodeStock = 0 #dicionario[]
    print(dicionario[10])

    
    return CodeStock 


def main():
    st.title("Stock Data Analysis App")

    #st.set_page_config(layout="wide")
    col1, col2, col3 = st.columns([1,9,1])

    # Input for stock symbol
    #stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):")


    with col2:


        stock_symbol ='CL=F'

        # Default start date and end date
        start_date = '2022-01-01'
        end_date = datetime.today().strftime('%Y-%m-%d')

        # Fetch data on button click
        if st.button("Fetch Data"):
            if stock_symbol:
                stock_data = get_stock_data(stock_symbol, start_date, end_date)

                if stock_data is not None:
                    # Display the tail of the data
                    st.subheader("Tail of the Data")
                    st.write(stock_data.tail())

                    # Save the data to a CSV file
                    save_data_to_csv(stock_data, f"{stock_symbol}_data.csv", "Stock")






if __name__ == "__main__":
    main()
