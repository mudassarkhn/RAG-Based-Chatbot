from langchain_qdrant import QdrantVectorStore
from embeddings.embedding import get_embedding
from config.config import QDRANT_URL, QDRANT_API_KEY
from dotenv import load_dotenv
load_dotenv()

def get_vectorstore():
    return QdrantVectorStore.from_existing_collection(
        embedding=get_embedding(),
        collection_name="Ninesol_Technologies_Knowledge_Base",
        prefer_grpc=True,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )