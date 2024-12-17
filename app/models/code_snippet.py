from pydantic import BaseModel

class CodeSnippet(BaseModel):
    language: str
    code: str
