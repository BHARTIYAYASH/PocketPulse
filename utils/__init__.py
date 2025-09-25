"""
Financial Tracker Utilities Package

This package provides various utility functions for the financial tracker application,
including logging, date processing, validation, and formatting utilities.
"""

from .logging_utils import configure_logging, setup_file_logging, get_logger_config
from .date_utils import (
    parse_natural_date, 
    format_date_display, 
    get_date_range,
    calculate_business_days,
    is_weekend,
    get_month_name
)
from .validation_utils import (
    validate_amount,
    validate_transaction_description,
    validate_category,
    validate_email,
    sanitize_input,
    validate_numeric_range,
    validate_text_length,
    is_safe_filename,
    validate_currency_amount
)
from .format_utils import (
    format_currency,
    format_number,
    format_percentage,
    format_large_number,
    format_transaction_amount,
    truncate_text,
    format_duration,
    capitalize_words,
    format_list_display,
    format_file_size,
    format_phone_number
)

__version__ = "1.0.0"
__author__ = "Financial Tracker Team"

# Package-level exports
__all__ = [
    # Logging utilities
    'configure_logging',
    'setup_file_logging', 
    'get_logger_config',
    
    # Date utilities
    'parse_natural_date',
    'format_date_display',
    'get_date_range',
    'calculate_business_days',
    'is_weekend',
    'get_month_name',
    
    # Validation utilities
    'validate_amount',
    'validate_transaction_description',
    'validate_category',
    'validate_email',
    'sanitize_input',
    'validate_numeric_range',
    'validate_text_length',
    'is_safe_filename',
    'validate_currency_amount',
    
    # Formatting utilities
    'format_currency',
    'format_number',
    'format_percentage',
    'format_large_number',
    'format_transaction_amount',
    'truncate_text',
    'format_duration',
    'capitalize_words',
    'format_list_display',
    'format_file_size',
    'format_phone_number',
]