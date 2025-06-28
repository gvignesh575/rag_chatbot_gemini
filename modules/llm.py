# llm.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

load_dotenv()

def get_llm_chain(vectorstore):
    # 1. Load Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",  # or "gemini-1.5-pro" / "gemini-2.5-pro-preview-03-25"
        temperature=0.3,
        convert_system_message_to_human=True,  # ensures proper formatting
        verbose=True
    )

    # 2. Setup retriever from vectorstore
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 3. Create RetrievalQA chain
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # can also try "map_reduce", "refine", etc.
        retriever=retriever,
        return_source_documents=True
    )
