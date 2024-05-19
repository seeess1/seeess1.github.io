from flask import Flask, send_from_directory, render_template
import pandas as pd
from app.helpers.data_reader import read_data_csv

app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for displaying the data
@app.route('/data')
def show_data():
    # Read data from CSV file using the data_reader module
    df = read_data_csv('app/data/data.csv')
    print(df)  # Add this line to print the DataFrame
    # Pass the DataFrame to the template
    return render_template('data.html', tables=[df.to_html(index=False)], titles=df.columns.values)

# Route to serve the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')
