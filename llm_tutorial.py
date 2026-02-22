import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM
# Ensure you have OPENAI_API_KEY set in your environment or .env file
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the user's questions conciselly."),
    ("user", "{input}")
])

# Create an output parser
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Invoke the chain
if __name__ == "__main__":
    user_input = input("Enter your question: ")
    response = chain.invoke({"input": user_input})
    print("\nResponse:")
    print(response)
