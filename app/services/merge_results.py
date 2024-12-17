def merge_results(static_results: list, ml_results: list) -> list:
    """
    Merge static analysis and ML-based analysis results.
    """
    # Deduplicate based on the message
    combined = {f"{item['line']}-{item['message']}": item for item in static_results + ml_results}
    return list(combined.values())
