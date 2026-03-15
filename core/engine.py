import os
import logging
from typing import List, Optional
from loguru import logger
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.schema import Document

# Setup industrial-grade logging
logger.add("logs/fin_rag.log", rotation="10 MB", retention="10 days")

class FinancialRAGCore:
    \"\"\"
    A sophisticated RAG engine designed for high-fidelity financial analysis.
    Combines LangChain orchestration with production-ready best practices.
    \"\"\"
    def __init__(self, api_key: str, model_name: str = "gpt-4-turbo-preview"):
        self.api_key = api_key
        self.embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        self.llm = ChatOpenAI(model_name=model_name, openai_api_key=api_key, temperature=0.1)
        self.vector_store = None
        logger.info(f"Initialized FinancialRAGCore with model: {model_name}")

    def ingest_documents(self, documents: List[Document], persist_directory: str = "./db"):
        \"\"\"
        Processes and indexes financial documents into the vector store.
        Uses recursive chunking to maintain semantic flow of complex financial data.
        \"\"\"
        logger.info(f"Starting ingestion for {len(documents)} document objects.")
        
        # Recursive splitter is essential for financial reports which often have nested structures
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200, 
            chunk_overlap=200,
            separators=["\n\n", "\n", "(?<=\. )", " ", ""]
        )
        
        chunks = text_splitter.split_documents(documents)
        logger.info(f"Generated {len(chunks)} semantic chunks.")

        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=persist_directory
        )
        logger.success("Vector store successfully updated and persisted.")

    def analyze_portfolio(self, query: str) -> str:
        \"\"\"
        Executes a domain-specific retrieval query to provide financial insights.
        \"\"\"
        if not self.vector_store:
            logger.error("Attempted query without initialized vector store.")
            raise ValueError("Vector store not initialized. Please ingest documents first.")

        logger.info(f"Executing investment query: {query}")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 4}),
            return_source_documents=True
        )

        response = qa_chain.invoke({"query": query})
        logger.success("Query execution complete.")
        return response["result"]

# Designed for Senthil's Financial AI Profile