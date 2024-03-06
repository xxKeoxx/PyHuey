import logging

def configuration():
    # Create handlers for console and file logging
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename='app.log')

    # Create formatters for different log levels
    debug_formatter = logging.Formatter('%(asctime)s - %(name)s - DEBUG - Message: %(message)s - File Name: %(filename)s - Line number: %(lineno)d')
    info_formatter = logging.Formatter('%(asctime)s - %(name)s - INFO - %(message)s')
    warning_formatter = logging.Formatter('%(asctime)s - %(name)s - WARNING - %(message)s')
    error_formatter = logging.Formatter('%(asctime)s - %(name)s - ERROR - %(message)s')

    # Set formatter for each handler
    console_handler.setFormatter(debug_formatter)  # For console, use debug format by default
    file_handler.setFormatter(debug_formatter)  # For file, use debug format by default

    # Add handlers to the root logger
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Set log levels for handlers
    console_handler.setLevel(logging.DEBUG)  # Set console handler to log all levels
    file_handler.setLevel(logging.INFO)  # Set file handler to log only INFO level and above

