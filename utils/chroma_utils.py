from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

PERSIST_DIRECTORY = "/home/tatsye/Desktop/book_recommendation/vectorstore"
MODEL_NAME = "all-MiniLM-L6-v2"

def get_embedding_model():
    """Initialize and return the embedding model."""
    return SentenceTransformerEmbeddings(model_name=MODEL_NAME)
def save_to_chroma(documents, persist_directory=PERSIST_DIRECTORY):
    """Save documents to Chroma vector store."""
    embedding_model = get_embedding_model()
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    vector_store.persist()
    return vector_store

def load_chroma(persist_directory=PERSIST_DIRECTORY):
    """Load the Chroma vector store from the specified directory."""
    embedding_model = get_embedding_model()
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )