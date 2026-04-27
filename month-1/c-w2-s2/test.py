from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
def embed_task(text):
    embeddings = model.encode(text,convert_to_numpy=True,show_progress_bar=False)
    for i in range(len(embeddings)):
        norm = np.linalg.norm(embeddings[i])
        print(norm)
        if norm > 0:
            embeddings[i] = embeddings[i] / norm

    return embeddings

print(embed_task("apple"))
