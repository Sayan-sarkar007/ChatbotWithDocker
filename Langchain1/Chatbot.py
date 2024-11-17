from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

result = model.invoke("What is 81 divided by 9?")
print("Full resutl: ")
print(result)
print("content only:")
print(result.content)