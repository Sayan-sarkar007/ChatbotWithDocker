from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import yfinance as yf


def Analyze_Stock(stock_name):

    load_dotenv()

    Stock_name = stock_name
    # Step 1: Fetch stock data using yfinance
    # reliance = yf.Ticker("RELIANCE.NS")
    # hist = reliance.history(period="1mo")
    # stock_data = hist[['Close', 'Volume']].tail(10).to_string()

    # Step 1: Fetch stock data using yfinance
    stock = yf.Ticker(stock_name)

    # Fetch the historical data for 1 month
    hist = stock.history(period="1mo")

    # Convert the relevant columns to a string format for analysis
    # You can use .to_string() directly to include more rows if needed.
    # Here, we'll keep the last 30 days of data, which corresponds to about 1 month.
    stock_data = hist[['Close', 'Volume']].to_string()

    llm = GoogleGenerativeAI(model="gemini-1.5-flash")

    prompt_template = """
    You are an AI stock analyst. Given the following stock data, provide a comprehensive analysis, including:
    - First print the Stock current price
    - Key trends and patterns
    - Indicators to consider (like moving averages, P/E ratio, etc.)
    - Suggestions for investors.

    Stock Data: {stock_data}

    Your analysis should help investors understand the current stock performance.
    It will be better to have some numbers for more understanding. give an copact analysis summery, that anyone can understand. 
    Keep in mind that this for people who know the about indian stock a littlebit and those who completely don't understand anything technical. 
    """

    prompt = PromptTemplate(
        input_variables=["stock_data"],
        template=prompt_template,
    )

    # Step 4: Create a LangChain analysis chain
    stock_analysis_chain = LLMChain(
        llm=llm,
        prompt=prompt,
    )

    # Step 5: Run the chain with the stock data
    analysis = stock_analysis_chain.run(stock_data)

    # Step 6: Print AI's analysis
    # print("AI Analysis Output:")
    # print(analysis)
    return analysis

