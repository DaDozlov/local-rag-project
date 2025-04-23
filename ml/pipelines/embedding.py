from langchain_community.embeddings import OllamaEmbeddings
from chromadb import PersistentClient
import uuid

EMBED_MODEL = "mxbai-embed-large"
DB_DIR = "./chromadb"

_emb = OllamaEmbeddings(model=EMBED_MODEL)
_client = PersistentClient(path=DB_DIR)
_collection = _client.get_or_create_collection("docs")


def embed(chunks, collection_name="docs", db_path=DB_DIR):
    client = PersistentClient(path=db_path)
    collection = client.get_or_create_collection(collection_name)

    texts = [c.page_content for c in chunks]
    meta = [c.metadata for c in chunks]
    ids = [str(uuid.uuid4()) for _ in texts]

    collection.add(documents=texts, metadatas=meta, ids=ids)
    return collection
