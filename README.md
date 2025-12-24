# AI-Powered RAG System: Dynamic Web & Wikipedia Q&A

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows users to chat with web content. By combining **LangChain**, **Groq (Llama 3.3)**, and **ChromaDB**, the system fetches live data from websites or Wikipedia, indexes it, and provides accurate, context-aware answers.



## 🌟 Features
* **Smart Retrieval:** Uses `ChromaDB` and `HuggingFace Embeddings` for high-accuracy document matching.
* **Dynamic Scraping:** Handles JavaScript-heavy sites using `Playwright` and `AsyncHtmlLoader`.
* **Wikipedia Integration:** Built-in support for official Wikipedia API to avoid rate-limiting issues.
* **Llama 3.3 Optimized:** Leverages Groq's API for lightning-fast inference using the latest Llama models.

---

## 🛠️ Technical Stack
* **Orchestration:** [LangChain](https://python.langchain.com/)
* **LLM:** [Groq Llama 3.3-70B](https://groq.com/)
* **Vector Store:** [ChromaDB](https://www.trychroma.com/)
* **Embeddings:** `all-MiniLM-L6-v2` (HuggingFace)
* **Web Extraction:** BeautifulSoup4, Playwright, and Wikipedia-API.
---

