# AI-Powered RAG System: Dynamic Web & Wikipedia Q&A

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows users to chat with web content. The system supports dual-vector store backends: **PostgreSQL (pgvector)** for enterprise-level persistence and **ChromaDB** for lightweight local storage.

---

## 🌟 Features
* **Dual Vector Store Support:** * **PostgreSQL + pgvector:** For robust, persistent, and scalable database storage.
    * **ChromaDB:** For fast, file-based local prototyping.
* **Smart Retrieval:** Uses `HuggingFace Embeddings` (`all-MiniLM-L6-v2`) for high-accuracy document matching.
* **Dynamic Scraping:** Handles JavaScript-heavy sites using `Playwright` and `AsyncHtmlLoader`.
* **Wikipedia Integration:** Built-in support for official Wikipedia API.
* **Llama 3.3 Optimized:** Leverages Groq's API for lightning-fast inference.

---

## 🛠️ Technical Stack
* **Orchestration:** [LangChain](https://python.langchain.com/)
* **LLM:** [Groq Llama 3.3-70B](https://groq.com/)
* **Vector Stores:** * [PostgreSQL](https://www.postgresql.org/) with [pgvector](https://github.com/pgvector/pgvector)
    * [ChromaDB](https://www.trychroma.com/)
* **Embeddings:** `all-MiniLM-L6-v2` (HuggingFace)
* **Web Extraction:** BeautifulSoup4, Playwright, and Wikipedia-API.

---

## 🚀 Setup & Configuration

### 1. Vector Store Selection
The system can be configured to use either Chroma or Postgres. 

**For PostgreSQL:**
* Ensure `pgvector` extension is enabled: `CREATE EXTENSION vector;`.
* Set your `DATABASE_URL` in the `.env` file.

**For ChromaDB:**
* The system will automatically create a `./chroma_db` directory for local storage.

### 2. Environment Variables
Create a `.env` file and add the following:
```env
GROQ_API_KEY=your_groq_key
DATABASE_URL=your data base that you are created in PostgreSQL
