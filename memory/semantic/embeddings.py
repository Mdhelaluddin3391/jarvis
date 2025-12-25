try:
    from sentence_transformers import SentenceTransformer
    HAS_EMBED = True
except ImportError:
    HAS_EMBED = False

class EmbeddingModel:
    def __init__(self):
        self.model = None
        if HAS_EMBED:
            # 'all-MiniLM-L6-v2' is fast and lightweight
            self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def embed(self, text: str) -> list[float]:
        if not self.model:
            # Fallback if library missing
            return [0.0] * 384
        
        # Convert numpy array to standard list for JSON serialization
        vector = self.model.encode(text)
        return vector.tolist()