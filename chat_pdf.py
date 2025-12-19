import streamlit as st
import os
from config import OPENAI_API_KEY
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


CHROMA_BASE_DIR = "./chroma_store"

st.set_page_config(page_title="Chat with PDF", layout= "centered")
st.title("Chat with PDF")

llm = ChatOpenAI(
    api_key = OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0
)

#embeddings = A translator that converts words into numbers
embeddings = OpenAIEmbeddings(
    api_key = OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    model="openai/text-embedding-3-small"
)

pdf_file = st.file_uploader("Upload a PDF file here", type = ["pdf"])


if pdf_file:
    with st.spinner("PDF Loading"):
        pdf_path = f"temp_{pdf_file.name}"
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())

#Steamlit Upload -> Memoty(Can't use with PyPDFLoader but File on computer can use with PyPDFLoader)
        loader = PyPDFLoader(pdf_path)
        doc = loader.load()

        print(f"Loaded {len(doc)} pages from PDF")

        #split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        chunks = splitter.split_documents(doc)

        #store in Vector DB
        db = Chroma(
            embedding_function=embeddings,
            persist_directory = f"./chroma_store/{pdf_file.name}"
        )

        db.add_documents(chunks)

        #MMR Retriever
        retriever = db.as_retriever(
            search_type = "mmr",
            search_kwargs = {
                "k" : 3,
                "fetch_k" : 6,
                "lambda_mult" : 0.7
            }
        )

        #RAG Prompt
        prompt = PromptTemplate.from_template(
            """
        You are a factual Assistant. Answer the question using only the Context below.
        If the answer is not in the context, say "Infomration Not Available" 

        context:
        {context}

        question:
        {question}
        """
        )


        #RAG Chain
        rag_chain = (
            {
                "context": retriever, "question" : RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )


        #Ask Questions
        question = st.text_input("Ask a question now, your PDF file is loaded.")

        if question:
            with st.spinner("Thinking.."):
                result = rag_chain.invoke(question)
                st.markdown("Answer")
                st.write(result)