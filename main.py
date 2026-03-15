import os
from loguru import logger
from dotenv import load_dotenv
from core.engine import FinancialRAGCore
from langchain.schema import Document

load_dotenv()

def main():
    print("--- Financial RAG Orchestrator Demo ---")
    
    # 1. Environment Check
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY not found in .env file.")
        return

    # 2. Initialize Engine
    rag = FinancialRAGCore(api_key=api_key)

    # 3. Simulate Ingestion (e.g., from an Earnings Call snippet)
    sample_docs = [
        Document(
            page_content=\"\"\"
            Q3 Performance Summary: Revenue increased by 12% YoY, driven by strong cloud demand. 
            Operating margin expanded to 28% from 25% in the previous year. 
            Cash flow from operations remained robust at .2B.
            \"\"\", 
            metadata={"source": "Earnings_Call_Q3.pdf", "ticker": "TECH_CORP"}
        )
    ]
    
    print("📂 Ingesting sample financial documents...")
    rag.ingest_documents(sample_docs)

    # 4. Perform Analysis
    query = "Analyze the revenue growth drivers and impact on operating margins."
    print(f"💬 Query: {query}")
    
    try:
        result = rag.analyze_portfolio(query)
        print(f"\n🤖 AI FINANCIAL INSIGHT:\n{result}")
    except Exception as e:
        logger.exception(f"Query failed: {str(e)}")

if __name__ == "__main__":
    main()