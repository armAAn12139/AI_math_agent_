import json
from sentence_transformers import SentenceTransformer

# Initialize SentenceTransformer model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def load_math_knowledge_base(json_file: str = "./../data/math_knowledge_base.json"):
    """
    Load math Q&A dataset and pre-compute embeddings for all questions.
    Returns a tuple: (questions, solutions, embeddings)
    """
    with open(json_file, "r") as f:
        data = json.load(f)

    problem = [entry["Problem"] for entry in data]
    solutions = [entry["Rationale"] for entry in data]
    correct = [entry["correct"] for entry in data]
    annoted_formula = [entry["annotated_formula"] for entry in data]


    embeddings = embedding_model.encode(problem, convert_to_tensor=True)

    print(f"[INFO] Loaded {len(data)} Q&A pairs into memory.")
    return problem, solutions, embeddings


if __name__ == "__main__":
    load_math_knowledge_base()
