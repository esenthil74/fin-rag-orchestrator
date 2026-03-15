# 📈 Financial RAG Orchestrator
### *Advanced Document Intelligence for Portfolio & Market Analysis*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://langchain.com/)
[![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-blue.svg)]()

**Financial RAG Orchestrator** is a production-grade Retrieval-Augmented Generation (RAG) system specifically architected for the financial services industry. It bridges the gap between raw, multi-format financial data (10-Ks, earnings calls, research reports) and actionable investment insights.

## 🌟 Key Features
- **Multi-Format Ingestion Engine**: Robust processing of PDF, Audio (MP4), and Tabular data using high-performance loaders.
- **Hybrid Semantic Search**: Combines dense vector retrieval with keyword-based metadata filtering for precision.
- **Financial Reasoning Layer**: Custom prompting strategies tailored for CFA/CPA-level analysis (e.g., ratio calculation, sentiment attribution).
- **Scale-Ready Architecture**: Inspired by NVIDIA/Databricks methodologies for handling high-volume document pipelines.
- **Observability**: Production logging with loguru for traceability of reasoning chains.

## 🏗️ Architecture
`mermaid
graph TD
    A[Financial Docs: 10-K, PPT, MP4] --> B[Smart Loader]
    B --> C[Recursive Semantic Chunker]
    C --> D[Vector Store - ChromaDB]
    E[User Investment Query] --> F{RAG Orchestrator}
    D --> F
    F --> G[Financial Domain LLM]
    G --> H[Actionable Investment Insight]
`

## 🚀 Quick Start
1. **Clone the Repo**
   `ash
   git clone https://github.com/esenthil74/fin-rag-orchestrator.git
   cd fin-rag-orchestrator
   `

2. **Install Dependencies**
   `ash
   pip install -r requirements.txt
   `

3. **Configure Environment**
   Create a .env file with your OPENAI_API_KEY.

---
## 🧑‍💻 Author
**Senthil E.** — AI/ML Engineer @ Apple | Ex-NVIDIA & Databricks. MS in Data Science, CPA, and CFA. Focusing on the intersection of scalable AI and high-fidelity financial data.

---
*Precision. Performance. Proven Expertise.*