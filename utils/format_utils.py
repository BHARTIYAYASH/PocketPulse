from typing import Union, Optional
from decimal import Decimal
import locale
from datetime import datetime


def format_currency(amount: Union[float, int, Decimal], 
                   currency_symbol: str = 'Rs.', 
                   show_symbol: bool = True,
                   use_commas: bool = True) -> str:
    """
    Format amount as currency string.
    
    Args:
        amount: Amount to format
        currency_symbol: Currency symbol to use
        show_symbol: Whether to include currency symbol
        use_commas: Whether to use comma thousand separators
    
    Returns:
        Formatted currency string
    """
    try:
        num_amount = float(amount)
        
        if use_commas:
            formatted = f"{num_amount:,.2f}"
        else:
            formatted = f"{num_amount:.2f}"
        
        if show_symbol:
            return f"{currency_symbol} {formatted}"
        else:
            return formatted
            
    except (ValueError, TypeError):
        return "0.00"


def format_number(number: Union[float, int], 
                 decimal_places: int = 2,
                 use_commas: bool = True) -> str:
    """
    Format number with specified decimal places.
    
    Args:
        number: Number to format
        decimal_places: Number of decimal places
        use_commas: Whether to use comma separators
    
    Returns:
        Formatted number string
    """
    try:
        if use_commas:
            format_str = f"{{:,.{decimal_places}f}}"
        else:
            format_str = f"{{:.{decimal_places}f}}"
        
        return format_str.format(float(number))
        
    except (ValueError, TypeError):
        return "0" + ("." + "0" * decimal_places if decimal_places > 0 else "")


def format_percentage(value: Union[float, int], decimal_places: int = 1) -> str:
    """
    Format value as percentage.
    
    Args:
        value: Value to format (0.1 = 10%)
        decimal_places: Number of decimal places
    
    Returns:
        Formatted percentage string
    """
    try:
        percentage = float(value) * 100
        format_str = f"{{:.{decimal_places}f}}%"
        return format_str.format(percentage)
        
    except (ValueError, TypeError):
        return "0.0%"


def format_large_number(number: Union[float, int]) -> str:
    """
    Format large numbers with K, M, B suffixes.
    
    Args:
        number: Number to format
    
    Returns:
        Formatted number string with suffix
    """
    try:
        num = float(number)
        
        if abs(num) >= 1_000_000_000:
            return f"{num / 1_000_000_000:.1f}B"
        elif abs(num) >= 1_000_000:
            return f"{num / 1_000_000:.1f}M"
        elif abs(num) >= 1_000:
            return f"{num / 1_000:.1f}K"
        else:
            return f"{num:.0f}"
            
    except (ValueError, TypeError):
        return "0"


def format_transaction_amount(amount: Union[float, int], 
                            transaction_type: str,
                            currency_symbol: str = 'Rs.') -> str:
    """
    Format transaction amount with type-specific styling.
    
    Args:
        amount: Transaction amount
        transaction_type: Type of transaction (Income/Expense)
        currency_symbol: Currency symbol
    
    Returns:
        Formatted amount string with appropriate prefix
    """
    formatted_amount = format_currency(amount, currency_symbol)
    
    if transaction_type.lower() == 'income':
        return f"+ {formatted_amount}"
    elif transaction_type.lower() == 'expense':
        return f"- {formatted_amount}"
    else:
        return formatted_amount


def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """
    Truncate text to specified length with suffix.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add when truncated
    
    Returns:
        Truncated text
    """
    if not text:
        return ""
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def format_duration(seconds: int) -> str:
    """
    Format duration in seconds to human readable format.
    
    Args:
        seconds: Duration in seconds
    
    Returns:
        Formatted duration string
    """
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds}s"
    else:
        hours = seconds // 3600
        remaining_minutes = (seconds % 3600) // 60
        return f"{hours}h {remaining_minutes}m"


def capitalize_words(text: str) -> str:
    """
    Capitalize each word in text while preserving certain lowercase words.
    
    Args:
        text: Text to capitalize
    
    Returns:
        Capitalized text
    """
    if not text:
        return ""
    
    # Words that should remain lowercase (articles, prepositions, etc.)
    lowercase_words = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 
                      'in', 'of', 'on', 'or', 'the', 'to', 'up', 'via'}
    
    words = text.lower().split()
    result = []
    
    for i, word in enumerate(words):
        if i == 0 or word not in lowercase_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    
    return ' '.join(result)


def format_list_display(items: list, 
                       max_items: int = 3, 
                       separator: str = ", ",
                       final_separator: str = " and ") -> str:
    """
    Format list for display with proper separators.
    
    Args:
        items: List of items to format
        max_items: Maximum items to show before truncation
        separator: Separator between items
        final_separator: Separator before last item
    
    Returns:
        Formatted list string
    """
    if not items:
        return ""
    
    str_items = [str(item) for item in items]
    
    if len(str_items) == 1:
        return str_items[0]
    elif len(str_items) == 2:
        return f"{str_items[0]}{final_separator}{str_items[1]}"
    elif len(str_items) <= max_items:
        return f"{separator.join(str_items[:-1])}{final_separator}{str_items[-1]}"
    else:
        displayed = str_items[:max_items]
        remaining = len(str_items) - max_items
        return f"{separator.join(displayed)} and {remaining} more"


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in bytes to human readable format.
    
    Args:
        size_bytes: Size in bytes
    
    Returns:
        Formatted size string
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return f"{s} {size_names[i]}"


def format_phone_number(phone: str, country_code: str = "+91") -> str:
    """
    Format phone number with country code.
    
    Args:
        phone: Phone number to format
        country_code: Country code prefix
    
    Returns:
        Formatted phone number
    """
    if not phone:
        return ""
    
    # Remove all non-digit characters
    digits = ''.join(filter(str.isdigit, phone))
    
    if len(digits) == 10:
        # Indian format: +91 XXXXX XXXXX
        return f"{country_code} {digits[:5]} {digits[5:]}"
    elif len(digits) == 11 and digits.startswith('0'):
        # Remove leading 0 and format
        digits = digits[1:]
        return f"{country_code} {digits[:5]} {digits[5:]}"
    else:
        return phone  # Return original if can't format