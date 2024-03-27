from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from flask import Flask, jsonify, render_template, request
import json
import requests

app = Flask(__name__)

API_KEY = '54c68ba3bdmshd0f85b301433eafp122d90jsn65a6d58d21f5'  # Replace this with your API key

@app.route('/')
def stoncks_index():
    return render_template("stoncks/stoncks_index.html")

@app.route('/get_stock_data', methods = ['POST'])
def get_stock_data_daily():
    print("Request to /get_stock_data received")
    stock_symbol = request.form.get('stock_symbol')
    selected_option = request.form['ts']

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={API_KEY}'
    response = requests.get(url)
    json_text = response.text  # Get the JSON text from the response
    
    # Parse the JSON text into a dictionary
    try:
        daily_data = json.loads(json_text)
    except json.JSONDecodeError as e:
        return 'error''Failed to decode JSON: ' + str(e)
    print(daily_data)
    # Check if the response contains an error message
    if 'Error Message' in daily_data:
        return 'error'; daily_data['Error Message']
        
    time_series_data = daily_data.get('Time Series (Daily)', {})
    
    def convert_date_format(input_date):
        date_object = datetime.strptime(input_date, '%Y-%m-%d')
        formatted_date = date_object.strftime('%b %d, %Y')
        return formatted_date

    # Convert date format and create DataFrame
    data_list = []
    for date, values in time_series_data.items():
        formatted_date = convert_date_format(date)
        values['Date'] = formatted_date
        data_list.append(values)
    
    print('data list',data_list)
    df = pd.DataFrame(data_list)
    df.reset_index(inplace=True)
    df = df[['Date', '1. open', '2. high', '3. low', '4. close', '5. volume']]
    print("Column names in DataFrame:", df.columns)
    # print(df)
    # x = df[['2. high', '3. low', '4. close', '5. volume']]
    # y = df['1. open']

    # X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    # model = LogisticRegression()
    # model.fit(X_train,y_train)
    # y_pred = model.predict(X_test)

    if selected_option== '7 days':
        _7daysdf = df.head(7)
        return render_template('stoncks/daily.html', daily_data=_7daysdf.to_dict(orient='records'), stock_symb=stock_symbol)
    elif selected_option== '1 month':
        _1monthdf = df.head(30)
        return render_template('stoncks/daily.html', daily_data=_1monthdf.to_dict(orient='records'), stock_symb=stock_symbol)
    elif selected_option== '3 Month':
        _3monthdf = df.head(90)
        return render_template('stoncks/daily.html', daily_data=_3monthdf.to_dict(orient='records'), stock_symb=stock_symbol)
    else: 
        return render_template('stoncks/err.html')

# @app.route('/get_stock_data_monthly')
# def get_stock_data_monthly():
#     symbol = 'AAPL'  # Replace this with the stock symbol you want to retrieve
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={API_KEY}'
    
#     response = requests.get(url)
#     json_text = response.text  # Get the JSON text from the response
    
#     # Parse the JSON text into a dictionary
#     try:
#         data = json.loads(json_text)
#     except json.JSONDecodeError as e:
#         return 'error''Failed to decode JSON: ' + str(e)
    
#     # Check if the response contains an error message
#     if 'Error Message' in data:
#         return 'error'; data['Error Message']
        
#     monthly_data = data.get('Monthly Time Series', {})
#     df = pd.DataFrame.from_dict(monthly_data, orient='index')
#     df.reset_index(inplace=True)
#     df.columns = ['Month', 'Open', 'High', 'Low', 'Close', 'Volume']

#     print(df.head())
#     print(monthly_data)
#     return render_template('monthly.html', data=df.to_dict(orient='records'), stock_symb=symbol)
    
    # return jsonify(json_text)

@app.route('/get_stock_data_2', methods = ['GET'])
def get_stock_3m():
    print("Request to /get_stock_data received")
    stock_symbol_args = request.args.get('stock_symbol')
    selected_option_args= '3 Month'
    url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol_args}&apikey={API_KEY}'  

    response = requests.get(url2)
    json_text = response.text  # Get the JSON text from the response
    
    # Parse the JSON text into a dictionary
    try:
        daily_data = json.loads(json_text)
    except json.JSONDecodeError as e:
        return 'error''Failed to decode JSON: ' + str(e)
    print(daily_data)
    # Check if the response contains an error message
    if 'Error Message' in daily_data:
        return 'error'; daily_data['Error Message']
        
    time_series_data = daily_data.get('Time Series (Daily)', {})
    
    def convert_date_format(input_date):
        date_object = datetime.strptime(input_date, '%Y-%m-%d')
        formatted_date = date_object.strftime('%b %d, %Y')
        return formatted_date

    # Convert date format and create DataFrame
    data_list = []
    for date, values in time_series_data.items():
        formatted_date = convert_date_format(date)
        values['Date'] = formatted_date
        data_list.append(values)
    
    print('data list',data_list)
    df = pd.DataFrame(data_list)
    df.reset_index(inplace=True)
    df = df[['Date', '1. open', '2. high', '3. low', '4. close', '5. volume']]
    print("Column names in DataFrame:", df.columns)
    print(df)
    if selected_option_args== '3 Month':
        _3monthdf_2 = df.head(90)
        return render_template('stoncks/daily.html', daily_data=_3monthdf_2.to_dict(orient='records'), stock_symb=stock_symbol_args)
    else: 
        return render_template('stoncks/err.html')

if __name__ == '__main__':
    app.run(debug=True)

