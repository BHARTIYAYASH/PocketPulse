from rich.console import Console
from rich.logging import RichHandler
import logging
from typing import Optional

def configure_logging(app_name: str, log_level: Optional[int] = None) -> logging.Logger:
    """Configure and initialize a Rich-enhanced logger with custom settings"""
    # Initialize rich console for enhanced output
    rich_console = Console(force_terminal=True, width=120)
    
    # Set default log level if not provided
    if log_level is None:
        log_level = logging.INFO
    
    # Configure logging with rich handler
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(
            console=rich_console, 
            rich_tracebacks=True,
            show_path=False,
            markup=True
        )],
        force=True
    )
    
    # Create and configure logger instance
    logger = logging.getLogger(app_name)
    logger.setLevel(log_level)
    
    return logger


def setup_file_logging(app_name: str, log_file: str = "app.log") -> logging.Logger:
    """Configure logger with both console and file output"""
    logger = logging.getLogger(f"{app_name}_file")
    
    if not logger.handlers:
        # Console handler with Rich
        console_handler = RichHandler(
            console=Console(force_terminal=True),
            rich_tracebacks=True,
            show_path=False
        )
        console_handler.setLevel(logging.INFO)
        
        # File handler for persistent logging
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        
        # Configure logger
        logger.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.propagate = False
    
    return logger


def get_logger_config() -> dict:
    """Return current logging configuration settings"""
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'rich.logging.RichHandler',
                'level': 'INFO',
                'formatter': 'standard'
            },
            'file': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'detailed',
                'filename': 'application.log',
                'encoding': 'utf-8'
            }
        },
        'loggers': {
            '': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }