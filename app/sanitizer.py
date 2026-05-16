import html
import re

def sanitize_input(value: str) -> str:
    """Sanitize user input to prevent XSS attacks."""
    value = html.escape(value)
    value = re.sub(r"<script[^>]*>.*?</script>", "", value, flags=re.IGNORECASE)
    return value.strip()
