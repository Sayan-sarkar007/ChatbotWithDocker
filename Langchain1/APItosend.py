from stockAnalysis import  Analyze_Stock as Analyze
from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "You are connected to the network"

@app.route('/stockAnalyze/<string:stockName>')
def stockAnalyze(stockName):
     result = Analyze(stockName)
     return result

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
