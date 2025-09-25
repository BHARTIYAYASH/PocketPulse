import re
from typing import Union, Optional
from decimal import Decimal, InvalidOperation


def validate_amount(amount_input: Union[str, int, float]) -> tuple[bool, Optional[float], Optional[str]]:
    """
    Validate and convert amount input to float.
    
    Args:
        amount_input: Amount as string, int, or float
    
    Returns:
        Tuple of (is_valid, validated_amount, error_message)
    """
    try:
        if isinstance(amount_input, str):
            # Remove currency symbols and whitespace
            cleaned = re.sub(r'[^\d.-]', '', amount_input.strip())
            if not cleaned:
                return False, None, "Amount cannot be empty"
            amount = float(cleaned)
        else:
            amount = float(amount_input)
        
        if amount <= 0:
            return False, None, "Amount must be greater than zero"
        
        if amount > 999999999:
            return False, None, "Amount exceeds maximum limit"
        
        # Round to 2 decimal places
        amount = round(amount, 2)
        
        return True, amount, None
        
    except (ValueError, TypeError):
        return False, None, "Invalid amount format"


def validate_transaction_description(description: str) -> tuple[bool, Optional[str], Optional[str]]:
    """
    Validate transaction description.
    
    Args:
        description: Transaction description string
    
    Returns:
        Tuple of (is_valid, cleaned_description, error_message)
    """
    if not description or not description.strip():
        return False, None, "Description cannot be empty"
    
    cleaned = description.strip()
    
    if len(cleaned) < 3:
        return False, None, "Description must be at least 3 characters long"
    
    if len(cleaned) > 500:
        return False, None, "Description cannot exceed 500 characters"
    
    # Remove excessive whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    return True, cleaned, None


def validate_category(category: str, valid_categories: list) -> tuple[bool, Optional[str]]:
    """
    Validate category against allowed categories.
    
    Args:
        category: Category to validate
        valid_categories: List of valid categories
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not category or not category.strip():
        return False, "Category must be selected"
    
    if category not in valid_categories:
        return False, f"Invalid category. Must be one of: {', '.join(valid_categories)}"
    
    return True, None


def validate_email(email: str) -> tuple[bool, Optional[str]]:
    """
    Validate email address format.
    
    Args:
        email: Email address to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not email or not email.strip():
        return False, "Email address is required"
    
    email = email.strip().lower()
    
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False, "Invalid email address format"
    
    if len(email) > 254:
        return False, "Email address is too long"
    
    return True, None


def sanitize_input(input_text: str, max_length: int = 1000) -> str:
    """
    Sanitize user input by removing potentially harmful characters.
    
    Args:
        input_text: Text to sanitize
        max_length: Maximum allowed length
    
    Returns:
        Sanitized text
    """
    if not input_text:
        return ""
    
    # Remove or escape potentially harmful characters
    sanitized = input_text.strip()
    
    # Remove null bytes and control characters
    sanitized = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', sanitized)
    
    # Limit length
    sanitized = sanitized[:max_length]
    
    # Normalize whitespace
    sanitized = re.sub(r'\s+', ' ', sanitized)
    
    return sanitized


def validate_numeric_range(value: Union[int, float], min_val: float, max_val: float) -> tuple[bool, Optional[str]]:
    """
    Validate that a numeric value falls within a specified range.
    
    Args:
        value: Value to validate
        min_val: Minimum allowed value
        max_val: Maximum allowed value
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        num_value = float(value)
        
        if num_value < min_val:
            return False, f"Value must be at least {min_val}"
        
        if num_value > max_val:
            return False, f"Value cannot exceed {max_val}"
        
        return True, None
        
    except (ValueError, TypeError):
        return False, "Invalid numeric value"


def validate_text_length(text: str, min_length: int = 0, max_length: int = 1000) -> tuple[bool, Optional[str]]:
    """
    Validate text length constraints.
    
    Args:
        text: Text to validate
        min_length: Minimum required length
        max_length: Maximum allowed length
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not text:
        text = ""
    
    length = len(text.strip())
    
    if length < min_length:
        return False, f"Text must be at least {min_length} characters long"
    
    if length > max_length:
        return False, f"Text cannot exceed {max_length} characters"
    
    return True, None


def is_safe_filename(filename: str) -> bool:
    """
    Check if filename is safe (no directory traversal, etc.).
    
    Args:
        filename: Filename to check
    
    Returns:
        True if filename is safe
    """
    if not filename or not filename.strip():
        return False
    
    # Check for directory traversal attempts
    if '..' in filename or '/' in filename or '\\' in filename:
        return False
    
    # Check for reserved characters
    reserved_chars = '<>:"|?*'
    if any(char in filename for char in reserved_chars):
        return False
    
    # Check length
    if len(filename) > 255:
        return False
    
    return True


def validate_currency_amount(amount_str: str, currency_symbol: str = 'Rs.') -> tuple[bool, Optional[float], Optional[str]]:
    """
    Validate currency amount with specific formatting.
    
    Args:
        amount_str: Amount string with or without currency symbol
        currency_symbol: Expected currency symbol
    
    Returns:
        Tuple of (is_valid, amount, error_message)
    """
    if not amount_str or not amount_str.strip():
        return False, None, "Amount is required"
    
    # Remove currency symbol and whitespace
    cleaned = amount_str.strip()
    if cleaned.startswith(currency_symbol):
        cleaned = cleaned[len(currency_symbol):].strip()
    
    # Remove commas (thousand separators)
    cleaned = cleaned.replace(',', '')
    
    try:
        amount = Decimal(cleaned)
        
        if amount <= 0:
            return False, None, "Amount must be greater than zero"
        
        if amount.as_tuple().exponent < -2:
            return False, None, "Amount cannot have more than 2 decimal places"
        
        return True, float(amount), None
        
    except (InvalidOperation, ValueError):
        return False, None, "Invalid amount format"