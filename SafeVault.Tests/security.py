import re

def sanitize_input(user_input):
    """
    Cleans user input to reduce the risk of
    SQL injection and cross-site scripting (XSS).
    """
    if not isinstance(user_input, str):
        return ""

    # Remove characters commonly used in SQL injection attacks
    sanitized = re.sub(r"[;\'\"--]", "", user_input)

    # Encode HTML tags to prevent XSS
    sanitized = sanitized.replace("<", "&lt;").replace(">", "&gt;")

    return sanitized
