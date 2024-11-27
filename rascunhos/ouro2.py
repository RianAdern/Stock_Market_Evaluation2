import streamlit as st
import yfinance as yf
import os
from datetime import datetime

def get_stock_data(stock_symbol, start_date, end_date):
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data for {stock_symbol}: {e}")
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

def main():
    st.title("Stock Data Analysis App")

    # Dictionary with different stocks and commodities
    stocks_dict = {
        "Gold": "XAUUSD=X",
        "Oil": "CL=F",
        "USDollar": "DX-Y.NYB",
        "S&P 500": "^GSPC",
        "Other": "AAPL"  # Replace with another stock symbol of your choice
    }

    # Dropdown menu to select stock or commodity
    selected_stock = st.selectbox("Select a Stock or Commodity", list(stocks_dict.keys()))

    # Default start date and end date
    start_date = '2022-01-01'
    end_date = datetime.today().strftime('%Y-%m-%d')

    # Fetch data on button click
    if st.button("Fetch Data"):
        stock_symbol = stocks_dict[selected_stock]
        stock_data = get_stock_data(stock_symbol, start_date, end_date)

        if stock_data is not None:
            # Display the tail of the data
            st.subheader("Tail of the Data")
            st.write(stock_data.tail())

            # Save the data to a CSV file
            save_data_to_csv(stock_data, f"{selected_stock}_data.csv", "Stock")

if __name__ == "__main__":
    main()
