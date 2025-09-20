from typing import Dict, Any
from app.services.knowledge_base import search_knowledge_base



def generate_step_by_step_solution(question: str, source: str, answer: str) -> str:
    """
    Format the final response as a step-by-step solution.
    """
    return (
        f" Source: {source}\n\n"
        f" Question: {question}\n\n"
        f" Step-by-step Solution:\n{answer}"
    )


def rag_pipeline(user_question: str) -> Dict[str, Any]:
    """
    Agentic RAG pipeline:
    1. Search knowledge base
    2. If not found, fallback to web search
    3. Return structured response
    """
    # Step 1: Try Knowledge Base
    kb_answer = search_knowledge_base(user_question)
    if kb_answer:
        return {
            "question": user_question,
            "answer": generate_step_by_step_solution(
                question=user_question,
                source="Knowledge Base",
                answer=kb_answer,
            ),
        }

   
            
        

    # Step 3: Nothing found
    return {
        "question": user_question,
        "answer": " Sorry, I couldn't find a solution in either the Knowledge Base or Web Search.",
    }
