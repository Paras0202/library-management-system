import logging

# Set up the basic logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# Global logger instance for the app
logger = logging.getLogger("library-management")
