from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=1.0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    api_key=GROQ_API_KEY,
    # other params...
)