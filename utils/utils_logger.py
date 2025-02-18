# utils/utils_logger.py

import logging

# Set up logger for the project
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(ch)

# Now you can import 'logger' from this module