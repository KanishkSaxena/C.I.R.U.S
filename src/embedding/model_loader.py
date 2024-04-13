try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    raise ImportError("Could not import sentence_transformers: Please install sentence-transformers package.")
        
try:
    from chromadb.api.types import EmbeddingFunction
except ImportError:
    raise ImportError("Could not import chromdb: Please install chromadb package.")

class MiniLML6V2EmbeddingFunction(EmbeddingFunction):
    MODEL = SentenceTransformer('all-MiniLM-L6-v2')
    def __call__(self, texts):
        return MiniLML6V2EmbeddingFunction.MODEL.encode(texts).tolist()


emb_func = MiniLML6V2EmbeddingFunction()