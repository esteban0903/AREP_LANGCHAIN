import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

response = llm.invoke(
    "Explain Retrieval-Augmented Generation (RAG) in simple technical terms."
)

print(response.content)