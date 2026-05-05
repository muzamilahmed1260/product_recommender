import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.prompt import PRODUCT_PROMPT

# Load environment variables for local development
load_dotenv()

# Secure API key (works locally + Streamlit Cloud)
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

# Prompt
prompt = PromptTemplate(
    input_variables=["query"],
    template=PRODUCT_PROMPT
)

# Output parser
parser = StrOutputParser()

# LCEL Chain (modern LangChain)
chain = prompt | llm | parser


# Function
def get_recommendations(query):
    return chain.invoke({
        "query": query
    })