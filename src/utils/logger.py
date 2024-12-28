import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger to log messages to a file."""
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger('example_logger', 'example.log')
    logger.info("This is an informational message.")
    logger.error("This is an error message.")