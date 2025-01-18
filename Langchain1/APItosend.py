from stockAnalysis import  Analyze_Stock as Analyze
from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return "You are connected to the network"

@app.route('/stockAnalyze/<string:stockName>')
def stockAnalyze(stockName):
     Stock = stockName+".NS"
     result = Analyze(Stock)
     return render_template("stock_analysis.html", result=result, stockName= Stock)

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.getenv("PORT"))
    app.run(debug = True)
