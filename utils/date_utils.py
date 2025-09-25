from datetime import datetime, timedelta
from typing import Optional, Union
import re
from dateutil import parser


def parse_natural_date(date_text: str, reference_date: Optional[datetime] = None) -> datetime:
    """
    Parse natural language date expressions into datetime objects.
    
    Args:
        date_text: Natural language date string
        reference_date: Base date for relative calculations (defaults to now)
    
    Returns:
        Parsed datetime object
    """
    if reference_date is None:
        reference_date = datetime.now()
    
    text = date_text.lower().strip()
    
    # Handle relative date expressions
    relative_patterns = {
        'today': reference_date,
        'yesterday': reference_date - timedelta(days=1),
        'tomorrow': reference_date + timedelta(days=1),
        'day before yesterday': reference_date - timedelta(days=2),
        'day after tomorrow': reference_date + timedelta(days=2),
    }
    
    for pattern, date_obj in relative_patterns.items():
        if pattern in text:
            return date_obj
    
    # Handle "last N days/weeks/months" patterns
    last_pattern = r'last (\d+) (day|week|month)s?'
    match = re.search(last_pattern, text)
    if match:
        number = int(match.group(1))
        unit = match.group(2)
        
        if unit == 'day':
            return reference_date - timedelta(days=number)
        elif unit == 'week':
            return reference_date - timedelta(weeks=number)
        elif unit == 'month':
            return reference_date - timedelta(days=number * 30)
    
    # Handle "next N days/weeks/months" patterns
    next_pattern = r'next (\d+) (day|week|month)s?'
    match = re.search(next_pattern, text)
    if match:
        number = int(match.group(1))
        unit = match.group(2)
        
        if unit == 'day':
            return reference_date + timedelta(days=number)
        elif unit == 'week':
            return reference_date + timedelta(weeks=number)
        elif unit == 'month':
            return reference_date + timedelta(days=number * 30)
    
    # Try to parse standard date formats
    try:
        return parser.parse(text)
    except Exception:
        # Fallback to reference date if parsing fails
        return reference_date


def format_date_display(date_obj: datetime, format_type: str = "standard") -> str:
    """
    Format datetime object for display purposes.
    
    Args:
        date_obj: Datetime object to format
        format_type: Format style ('standard', 'short', 'long', 'iso')
    
    Returns:
        Formatted date string
    """
    formats = {
        'standard': '%Y-%m-%d',
        'short': '%m/%d/%y',
        'long': '%B %d, %Y',
        'iso': '%Y-%m-%dT%H:%M:%S',
        'display': '%d %b %Y',
        'time': '%H:%M:%S'
    }
    
    return date_obj.strftime(formats.get(format_type, formats['standard']))


def get_date_range(period: str, reference_date: Optional[datetime] = None) -> tuple[datetime, datetime]:
    """
    Get start and end dates for common time periods.
    
    Args:
        period: Time period ('today', 'week', 'month', 'year', 'last_week', etc.)
        reference_date: Reference date for calculations
    
    Returns:
        Tuple of (start_date, end_date)
    """
    if reference_date is None:
        reference_date = datetime.now()
    
    if period == 'today':
        start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end = reference_date.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    elif period == 'week':
        start = reference_date - timedelta(days=reference_date.weekday())
        start = start.replace(hour=0, minute=0, second=0, microsecond=0)
        end = start + timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)
    
    elif period == 'month':
        start = reference_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        next_month = start.replace(month=start.month + 1) if start.month < 12 else start.replace(year=start.year + 1, month=1)
        end = next_month - timedelta(microseconds=1)
    
    elif period == 'year':
        start = reference_date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        end = reference_date.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
    
    elif period == 'last_week':
        start = reference_date - timedelta(days=reference_date.weekday() + 7)
        start = start.replace(hour=0, minute=0, second=0, microsecond=0)
        end = start + timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)
    
    elif period == 'last_month':
        if reference_date.month == 1:
            start = reference_date.replace(year=reference_date.year - 1, month=12, day=1)
        else:
            start = reference_date.replace(month=reference_date.month - 1, day=1)
        start = start.replace(hour=0, minute=0, second=0, microsecond=0)
        end = reference_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(microseconds=1)
    
    else:
        # Default to today
        start = reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
        end = reference_date.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    return start, end


def calculate_business_days(start_date: datetime, end_date: datetime) -> int:
    """
    Calculate number of business days between two dates.
    
    Args:
        start_date: Start date
        end_date: End date
    
    Returns:
        Number of business days
    """
    business_days = 0
    current_date = start_date
    
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Monday = 0, Friday = 4
            business_days += 1
        current_date += timedelta(days=1)
    
    return business_days


def is_weekend(date_obj: datetime) -> bool:
    """Check if given date falls on a weekend."""
    return date_obj.weekday() >= 5


def get_month_name(month_num: int) -> str:
    """Get month name from month number."""
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    return months[month_num - 1] if 1 <= month_num <= 12 else 'Invalid'