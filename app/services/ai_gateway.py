import re

# Math-related keywords & symbols for basic checks
MATH_KEYWORDS = ["solve", "integrate", "differentiate", "equation", "matrix", "limits", "probability", "algebra", "geometry"]
MATH_SYMBOLS = ["=", "+", "-", "∫", "Δ", "^", "π"]


def sanitize_input(user_input: str) -> str:
    """Remove sensitive info (emails, phone numbers) from input."""
    sanitized = re.sub(r'\S+@\S+', '[REDACTED]', user_input)
    sanitized = re.sub(r'\b\d{10}\b', '[REDACTED]', sanitized)
    return sanitized


def input_guardrail(user_input: str) -> str:
    """Check if input contains math-related keywords."""
    user_input = user_input.lower()
    if any(keyword in user_input for keyword in MATH_KEYWORDS):
        return user_input
    return "Error: Only math-related questions are allowed."


def output_guardrail(generated_solution: str) -> str:
    """Check if output contains math symbols."""
    if any(symbol in generated_solution for symbol in MATH_SYMBOLS):
        return generated_solution
    return "Error: Solution is unrelated to math or not available."


def ai_gateway_pipeline(user_input: str, rag_agent_func) -> str:
    """Full guardrail pipeline from input to output."""
    sanitized_input = sanitize_input(user_input)
    guarded_input = input_guardrail(sanitized_input)
    
    if "Error" in guarded_input:
        return guarded_input

    generated_solution = rag_agent_func(guarded_input)  # RAG Agent generates solution
    guarded_output = output_guardrail(generated_solution)
    
    return guarded_output
