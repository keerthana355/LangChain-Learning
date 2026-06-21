from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions = 32)

documents = [
    "Delhi is the capital of India",
    "Amaravathi is the capita of Andhra Prcadesh",
    "Paris is the capital of France"
]
response = embedding.embed_documents(documents)

print(response)
print(str(response))
print(len(response))


