from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Agentic RAG Math Professor",
    description="Educational assistant that solves math step-by-step",
    version="1.0.0"
)

# Register routes
app.include_router(router)
