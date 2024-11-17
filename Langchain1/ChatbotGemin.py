from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

message = [
    SystemMessage(content="solove the following question"),
    HumanMessage(content="What is a bird ?"),
]

model = GoogleGenerativeAI(model="gemini-1.5-flash")
result = model.invoke(message)
print(f"Answer from google : {result}")


