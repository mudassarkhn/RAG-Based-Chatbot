from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from config.config import HUGGINGFACEHUB_API_TOKEN
load_dotenv()

def get_embedding():
    embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-mpnet-base-v2",
    task="feature-extraction",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )
    return embeddings


# vector = embedding().embed_query("This is a cloud-based embedding.")
# print(vector)