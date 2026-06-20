from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=1.5, max_completion_tokens=10)

result = llm.invoke("What is the capital of India?")
print(result.content)