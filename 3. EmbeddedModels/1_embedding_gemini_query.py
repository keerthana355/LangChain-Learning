from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions =32)

response = embedding.embed_query("Delhi is the capital of India")

print(len(response))
print(str(response))

