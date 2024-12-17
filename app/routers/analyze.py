from fastapi import APIRouter, HTTPException
from app.models.code_snippet import CodeSnippet
from app.services.static_analysis import perform_static_analysis
from app.services.ml_analysis import perform_ml_analysis
from app.services.merge_results import merge_results

router = APIRouter(prefix="/analyze", tags=["Analyze"])

@router.post("/")
async def analyze_code(snippet: CodeSnippet):
    """
    Analyze the provided code snippet and return linting and optimization suggestions.
    """
    if not snippet.code.strip():
        raise HTTPException(status_code=400, detail="Code snippet cannot be empty.")

    # Perform static analysis
    static_results = perform_static_analysis(snippet.language, snippet.code)

    # Perform ML-based analysis
    ml_results = perform_ml_analysis(snippet.code)

    # Merge results
    combined_results = merge_results(static_results, ml_results)
    return {"results": combined_results}
