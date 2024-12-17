from fastapi import FastAPI
from app.routers import analyze

app = FastAPI(
    title="Code Analyzer API",
    description="Analyze code snippets for optimization and linting suggestions",
    version="1.0.0",
)

# Include Routers
app.include_router(analyze.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Code Analyzer API!"}
