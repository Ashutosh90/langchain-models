from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4', temperature=1.1, max_completion_tokens=100)

result = model.invoke("Write a 5 line paragraph on GenAI?")

print(result.content)