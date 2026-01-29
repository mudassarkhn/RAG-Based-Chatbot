# RAG-Based-Chatbot
# Ninesol ChatBot - RAG-Powered AI Assistant

A sophisticated Retrieval-Augmented Generation (RAG) chatbot built with **LangChain**, **Streamlit**, and **Qdrant** vector database. This intelligent assistant answers questions specifically about Ninesol Technologies by leveraging advanced language models and contextual information retrieval.

## 📋 Table of Contents

- [Features](#features)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API & Services](#api--services)
- [Key Components](#key-components)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## ✨ Features

- **Intelligent Question Answering**: Leverages RAG to provide accurate, context-aware answers about Ninesol Technologies
- **Conversation Memory**: Maintains chat history for contextual, multi-turn conversations
- **Vector-Based Retrieval**: Uses Qdrant vector database for efficient semantic search
- **Modern UI**: Interactive Streamlit-powered chat interface
- **High-Performance LLM**: Powered by Groq's fast inference engine with GPT-OSS-120B model
- **Advanced Embeddings**: Uses Hugging Face sentence transformers for high-quality semantic embeddings
- **Maximal Marginal Relevance (MMR)**: Smart retrieval strategy to balance relevance and diversity
- **Error Handling**: Graceful error messages and fallback responses

---

## 🏗️ Project Architecture

### High-Level Flow

```
User Input
    ↓
Frontend (Streamlit)
    ↓
RAG Chain (LangChain)
    ├→ Retriever (Qdrant Vector Store)
    │   ├→ Embeddings (HuggingFace)
    │   └→ Context Documents
    ├→ Memory (Chat History)
    └→ LLM (Groq)
    ↓
Response
    ↓
User Interface
```

### Architecture Components

1. **Frontend Layer**: Streamlit-based conversational UI
2. **Chain Layer**: LangChain RAG pipeline orchestration
3. **Retrieval Layer**: Qdrant vector database with semantic search
4. **LLM Layer**: Groq API with GPT-OSS-120B model
5. **Embedding Layer**: HuggingFace sentence transformers
6. **Memory Layer**: Conversation buffer for context maintenance

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Web Framework** | Streamlit | Latest |
| **LLM Orchestration** | LangChain | Latest |
| **Language Model** | Groq (GPT-OSS-120B) | OpenAI-compatible |
| **Vector Database** | Qdrant | Cloud-hosted |
| **Embeddings** | Hugging Face Transformers | sentence-transformers/all-mpnet-base-v2 |
| **API Client** | LangChain Groq | Latest |
| **Environment** | Python | 3.12+ |
| **Package Manager** | pip/conda | Latest |

---

## 📦 Prerequisites

- **Python 3.12 or higher**
- **pip** or **conda** package manager
- **API Keys**:
  - Groq API Key (for LLM access)
  - Hugging Face API Token (for embeddings)
  - Qdrant API Key (for vector database)
- **Internet Connection** (for API access)
- **4GB+ RAM** (minimum recommended)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd RAG\ Project
```

### 2. Create a Virtual Environment

**Using conda (recommended):**
```bash
conda create -n rag_chatbot python=3.12
conda activate rag_chatbot
```

**Using venv:**
```bash
python -m venv botenv
# On Windows:
botenv\Scripts\activate
# On macOS/Linux:
source botenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Key dependencies:**
- `langchain` - LLM orchestration framework
- `langchain-groq` - Groq API integration
- `langchain-huggingface` - HuggingFace embeddings
- `langchain-qdrant` - Qdrant vector store
- `streamlit` - Web UI framework
- `python-dotenv` - Environment variable management
- `qdrant-client` - Qdrant client library

### 4. Install Additional Requirements

```bash
pip install langchain-core langchain-classic
```

---

## ⚙️ Configuration

### 1. Environment Variables

Create a `.env` file in the `app/` directory with the following variables:

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Hugging Face Configuration
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here

# Qdrant Vector Database Configuration
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key

# Optional: Supabase (if using Supabase)
SUPABASE_DB_PASSWORD=your_password_here
```

### 2. Get API Keys

**Groq API Key:**
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Create a new API key
4. Copy and add to `.env`

**Hugging Face Token:**
1. Visit [huggingface.co](https://huggingface.co)
2. Go to Settings → Access Tokens
3. Create a new token with "read" access
4. Copy and add to `.env`

**Qdrant Cloud:**
1. Visit [cloud.qdrant.io](https://cloud.qdrant.io)
2. Create a cluster
3. Get URL and API key
4. Add to `.env`

### 3. Verify Qdrant Collection

Ensure the Qdrant collection `Ninesol_Technologies_Knowledge_Base` exists with:
- Proper embeddings ingested
- Correct dimension size (matching HuggingFace embeddings)
- Indexed documents

---

## 📁 Project Structure

```
RAG Project/
├── app/
│   ├── .env                          # Environment variables (DO NOT COMMIT)
│   ├── chain.py                      # RAG chain orchestration
│   ├── frontend.py                   # Streamlit UI application
│   │
│   ├── config/
│   │   └── config.py                 # Configuration loader
│   │
│   ├── LLM/
│   │   └── LLM.py                    # Language model initialization (Groq)
│   │
│   ├── Prompt/
│   │   └── Prompt.py                 # Prompt templates
│   │
│   ├── embeddings/
│   │   └── embedding.py              # Embedding model initialization
│   │
│   ├── VectorStores/
│   │   └── Vectorstores.py           # Qdrant vector store configuration
│   │
│   └── Resources/                    # Resource files, documents, etc.
│
├── botenv/                           # Python virtual environment
├── README.md                         # Project documentation (this file)
└── requirements.txt                  # Python dependencies

---

## 🎯 Usage

### Running the Application

1. **Activate the virtual environment**

```bash
# On Windows:
botenv\Scripts\activate
# On macOS/Linux:
source botenv/bin/activate
```

2. **Navigate to the app directory**

```bash
cd app
```

3. **Run the Streamlit application**

```bash
streamlit run frontend.py
```

4. **Access the application**

The app will open in your default browser at `http://localhost:8501`

### Using the Chatbot

1. **Type your question** in the chat input field
2. **Press Enter** to submit
3. **Wait for response** (indicated by "Loading..." spinner)
4. **Review the answer** which is based on Ninesol Technologies knowledge
5. **Continue conversation** - chat history is automatically maintained
6. **Reset chat** using the "Reset Chat" button to clear history

### Example Questions

- "Tell me about Ninesol Technologies"
- "What services does Ninesol offer?"
- "How do I contact Ninesol?"
- "What is the company culture?"
- "Tell me about the team"

---

## 🔌 API & Services

### External Services

| Service | Purpose | Free Tier |
|---------|---------|-----------|
| **Groq** | Fast LLM inference | Yes (limited) |
| **Hugging Face** | Embeddings generation | Yes (with token) |
| **Qdrant** | Vector database | 1 free cluster |

### API Rate Limits

- **Groq**: Check console.groq.com for current limits
- **Hugging Face**: Endpoint-based usage
- **Qdrant**: Depends on your cluster plan

---

## 🧩 Key Components

### 1. **Chain (chain.py)**

```python
# RAG Chain Architecture:
# 1. Retriever: Fetches relevant documents using MMR
# 2. Prompt: Injects context into template
# 3. LLM: Generates response
# 4. Memory: Tracks conversation history
```

**Key Features:**
- Maximal Marginal Relevance (MMR) retrieval
- Top-3 documents retrieved (configurable via `k` parameter)
- Fetch 10 candidates before ranking (`fetch_k`)
- Parallel processing with `RunnableParallel`

### 2. **Frontend (frontend.py)**

**Components:**
- Page configuration with custom title and icon
- Chat message display (user and assistant)
- User input field with context hints
- Reset chat button
- Loading spinner during inference
- Error handling and display

**Session Management:**
- Stores messages in Streamlit session state
- Maintains conversation history throughout session
- Memory integration for multi-turn context

### 3. **LLM Configuration (LLM.py)**

**Model Details:**
- **Model**: openai/gpt-oss-120b (via Groq)
- **Temperature**: 1.0 (balanced creativity)
- **Reasoning Format**: Parsed (structured output)
- **Max Retries**: 2 (reliability)

### 4. **Embeddings (embedding.py)**

**Model**: `sentence-transformers/all-mpnet-base-v2`
- High-quality semantic embeddings
- 768-dimensional vectors
- Optimized for semantic search
- Supports multiple languages

### 5. **Vector Store (Vectorstores.py)**

**Qdrant Configuration:**
- Cloud-hosted vector database
- Collection: `Ninesol_Technologies_Knowledge_Base`
- Uses gRPC for faster communication
- Authenticated access with API key

---

## 🏃 Running the Application

### Development Mode

```bash
cd app
streamlit run frontend.py --logger.level=debug
```

### Production Deployment

```bash
# Using gunicorn (example)
streamlit run frontend.py --server.headless true --server.port 8000
```

### Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
EXPOSE 8501
CMD ["streamlit", "run", "frontend.py"]
```

Build and run:

```bash
docker build -t ninesol-chatbot .
docker run -p 8501:8501 --env-file .env ninesol-chatbot
```

---

## 🔄 How It Works

### Step-by-Step Flow

1. **User submits a question** via the Streamlit interface
2. **Retriever queries Qdrant** with embeddings of the question
3. **Top-3 documents retrieved** using MMR (balancing relevance and diversity)
4. **Context is formatted** with documents + chat history
5. **Prompt template injects** context + question + history
6. **LLM (Groq) generates response** using the enriched prompt
7. **Response is displayed** to user in the chat interface
8. **Messages are added to memory** for future context

### Key Data Flows

```
Question Input
    ↓
Embedding Generation (HuggingFace)
    ↓
Vector Similarity Search (Qdrant)
    ↓
Document Retrieval & Ranking (MMR)
    ↓
Context Assembly
    ↓
Prompt Engineering
    ↓
LLM Inference (Groq)
    ↓
Response Post-processing
    ↓
Display & Storage
```


## 🚢 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)
3. Create new app pointing to `frontend.py`
4. Add secrets in dashboard (GROQ_API_KEY, etc.)

### Self-Hosted (Linux/Ubuntu)

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install python3.12 python3.12-venv

# Clone and setup
git clone <repo> && cd RAG\ Project/app
python3.12 -m venv botenv
source botenv/bin/activate
pip install -r requirements.txt

# Run with systemd
sudo nano /etc/systemd/system/ninesol-chatbot.service
```

Systemd service file:

```ini
[Unit]
Description=Ninesol Chatbot
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/home/user/RAG\ Project/app
ExecStart=/home/user/RAG\ Project/botenv/bin/streamlit run frontend.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Code Style

- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Include comments for complex logic
- Test thoroughly before submitting

---

## 📧 Support & Contact

For issues, questions, or suggestions:

1. **Open an GitHub Issue**
2. **Check existing issues** for similar problems
3. **Include details**: error message, steps to reproduce, environment info
4. **Contact ME** for business inquiries

---

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Qdrant Documentation](https://qdrant.tech/documentation/)
- [Groq API Reference](https://console.groq.com/docs/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/)

---

## ⭐ Acknowledgments

- Built with **LangChain** for RAG orchestration
- Powered by **Groq** for fast LLM inference
- Vector storage by **Qdrant**
- Embeddings from **Hugging Face**
- UI framework **Streamlit**

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Status**: Active Development

---

