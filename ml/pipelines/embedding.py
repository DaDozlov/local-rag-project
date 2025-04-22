from langchain_community.embeddings import OllamaEmbeddings
from chromadb import PersistentClient

EMBED_MODEL = "mxbai-embed-large"
DB_DIR = "./chromadb"

_emb = OllamaEmbeddings(model=EMBED_MODEL)
_client = PersistentClient(path=DB_DIR)
_collection = _client.get_or_create_collection("docs")


def embed(chunks):
    texts = [c.page_content for c in chunks]
    meta = [c.metadata for c in chunks]
    _collection.add(texts=texts, metadatas=meta)
    return _collection