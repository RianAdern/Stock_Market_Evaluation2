import yfinance as yf
import os
from datetime import datetime


def get_market_data(ticker):
    # Ticker symbol for Gold (assuming XAU/USD, but please check the correct symbol)
    #ticker = 'CL=F'

    # Define the time period for data retrieval
    start_date = '2000-09-01' # 1 de setembro de 2000

    end_date = datetime.today().strftime('%Y-%m-%d')
    #end_date = '2023-01-01'

    # Fetch historical market data
    gold_data = yf.download(ticker, start=start_date, end=end_date)

    return gold_data

def save_data_to_csv(data, filename, directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the full path for the CSV file
    file_path = os.path.join(directory, filename)

    # Save the DataFrame to a CSV file
    data.to_csv(file_path)
    print(f"Data saved to {file_path}")
 

if __name__ == "__main__":
    

    ticker = 'CL=F'
    market_data = get_market_data(ticker)
    
    print(market_data)

    csv_filename = 'stock_'+ticker+'_market_data.csv'
    csv_directory = 'Stock'

    save_data_to_csv(market_data, csv_filename, csv_directory)