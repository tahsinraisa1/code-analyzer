import subprocess

def run_pylint(code: str) -> list:
    """
    Run PyLint on the provided Python code and return the linting results.
    """
    with open("temp_code.py", "w") as temp_file:
        temp_file.write(code)

    try:
        result = subprocess.run(
            ["pylint", "temp_code.py", "--output-format=json"],
            capture_output=True,
            text=True,
        )
        pylint_output = eval(result.stdout)
        suggestions = [
            {
                "line": item["line"],
                "message": item["message"],
                "type": item["type"].capitalize(),  # Error, Warning, etc.
            }
            for item in pylint_output
        ]
        return suggestions
    except Exception as e:
        return [{"line": 0, "message": f"Static analysis failed: {str(e)}", "type": "Error"}]


def perform_static_analysis(language: str, code: str) -> list:
    """
    Perform static analysis based on the programming language.
    """
    if language.lower() == "python":
        return run_pylint(code)
    else:
        # Placeholder for other language support
        return [{"line": 0, "message": f"Language '{language}' not supported.", "type": "Error"}]
