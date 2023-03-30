from walkthrough import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/companies')
def companies_page():
    return render_template('companies.html')