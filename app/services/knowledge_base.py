import json
from typing import Optional
from sentence_transformers import SentenceTransformer, util

# Load embedding model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load KB
with open("data/math_knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

# Extract problems and rationales
kb_problems = [item["Problem"] for item in knowledge_base]
kb_rationales = [item["Rationale"] for item in knowledge_base]

# Precompute embeddings
kb_embeddings = embedding_model.encode(kb_problems, convert_to_tensor=True)


def search_knowledge_base(user_question: str, threshold: float = 0.6) -> Optional[str]:
    """
    Search KB by cosine similarity.
    Returns rationale if a good match is found, else None.
    """
    query_embedding = embedding_model.encode(user_question, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, kb_embeddings)[0]

    best_score = scores.max().item()
    best_idx = scores.argmax().item()

    if best_score >= threshold:
        return kb_rationales[best_idx]

    return None
