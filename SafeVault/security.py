import re

def sanitize_input(user_input):
    """
    Removes potentially dangerous characters to prevent SQL injection/XSS.
    """
    if not isinstance(user_input, str):
        return ""
    # Remove common SQL injection characters
    sanitized = re.sub(r"[;\'\"--]", "", user_input)
    # Escape HTML characters for XSS prevention
    sanitized = sanitized.replace("<", "&lt;").replace(">", "&gt;")
    return sanitized
