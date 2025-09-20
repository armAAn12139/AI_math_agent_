from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_agent import rag_pipeline

router = APIRouter()


# Request body schema
class MathQuestionRequest(BaseModel):
    question: str
    use_feedback: bool = False


@router.post("/solve")
async def solve_math_question(request: MathQuestionRequest):
    """
    Solve a math question using RAG pipeline:
    1. Knowledge Base lookup
    2. Fallback to Web Search
    """
    result = rag_pipeline(request.question)

    return {
        "question": result["question"],
        "answer": result["answer"]
    }
