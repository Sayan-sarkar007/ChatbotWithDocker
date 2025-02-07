from stockAnalysis import Analyze_Stock as Analyze
from dotenv import load_dotenv

load_dotenv()
import os
from flask import Flask, render_template, request
from yahoo_fin.stock_info import tickers_nifty50

app = Flask(__name__)


def fetch_stock_names():
    try:
        stock_list = tickers_nifty50()  # Fetch Nifty 50 stock tickers
        # print("Fetched Stock List:", stock_list)  # Debugging statement
        return stock_list
    except Exception as e:
        print("Error fetching NSE stocks:", e)
        return []


# @app.route('/')
# def home():
#    return render_template("index.html")


@app.route("/stockAnalyzer/<string:stockName>")
def stockAnalyze(stockName):
    Stock = stockName + ".NS"
    result = Analyze(Stock)
    return render_template("stock_analysis.html", result=result, stockName=Stock)


@app.route("/stockAnalyze", methods=["GET"])
def index():
    stockName = request.args.get("stockName", "")

    if not stockName:
        return "No stock selected.", 400  # Error if no stock selected

    # Append ".NS" to stock name
    Stock = stockName + ".NS"

    # Analyze stock
    result = Analyze(Stock)

    # Render template with result
    return render_template("index.html", result=result, stockName=stockName)


@app.route("/")
def home():
    stock_names = fetch_stock_names()
    return render_template("index.html", stock_names=stock_names)


@app.route("/stockAnalyze2", methods=["GET"])
def stock_analyze():
    stockName = request.args.get("stockName", "")

    if not stockName:
        return "No stock selected.", 400

    Stock = stockName

    stock_names = fetch_stock_names()
    result = Analyze(Stock)
    return render_template(
        "index.html", result=result, stockName=stockName, stock_names=stock_names
    )


if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.getenv("PORT"))
    app.run(debug=True)
