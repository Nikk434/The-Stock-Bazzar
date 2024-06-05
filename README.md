# The Stock Bazzar

## Overview

The Stock Bazzar is a web-based tool for retrieving and displaying historical stock data. It uses the Alpha Vantage API to fetch stock data and displays the data in a user-friendly format.

## Features

- Fetch daily stock data for a given stock symbol.
- Display data for different time ranges: 7 days, 1 month, and 3 months.
- Use a simple web interface to input the stock symbol and select the time range.

## Technologies Used

- Python
- Flask
- Pandas
- HTML/CSS
- Alpha Vantage API

## Installation

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Requests

## Usage
### Running the Application
- Set your Alpha Vantage API key in the code.
API_KEY = 'your_alpha_vantage_api_key'

- Start the Flask application.
  `stonks.py`
- Open your web browser and navigate to http://127.0.0.1:5000.

### Using the Application
- Home Page: Enter the stock symbol and select the time range to fetch the stock data.
- Data Display: The stock data for the selected range will be displayed in a table format.

## API Endpoints
`/`
- Method: GET
- Description: Renders the home page.

`/get_stock_data`
- Method: POST
- Description: Fetches stock data for the given symbol and time range. Displays the data in a table.
- Parameters:
stock_symbol: The symbol of the stock (e.g., AAPL for Apple Inc.).
ts: Time range selection (7 days, 1 month, 3 months).

`/get_stock_data_2`
- Method: GET
- Description: Fetches 3 months of stock data for the given symbol and displays the data in a table.
- Parameters:
stock_symbol: The symbol of the stock (e.g., AAPL for Apple Inc.).