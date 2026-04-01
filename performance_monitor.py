"""
Python Logging Lab: Building an Application Performance Monitor
================================================================
Learn how to use Python's logging library by creating a simple performance
monitoring system that tracks function execution times and system metrics.
"""

import logging
import time
import random
import json
from datetime import datetime
from functools import wraps

# Setup logging function
def setup_logging():
    """Configure a comprehensive logging system with multiple handlers"""
    
    detailed_formatter = logging.Formatter(
        '%(asctime)s | %(name)-15s | %(levelname)-8s | %(funcName)-20s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    simple_formatter = logging.Formatter('%(levelname)s: %(message)s')
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    file_handler = logging.FileHandler('performance_monitor.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    error_handler = logging.FileHandler('errors.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(detailed_formatter)
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(error_handler)
    
    return root_logger

# Create module-specific loggers
performance_logger = logging.getLogger('performance')
database_logger = logging.getLogger('database')
api_logger = logging.getLogger('api')

def log_performance(threshold_ms=100):
    """Decorator to log function execution time"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            logger = performance_logger
            
            logger.debug(f"Starting execution of {func.__name__}")
            
            try:
                result = func(*args, **kwargs)
                execution_time_ms = (time.time() - start_time) * 1000
                
                if execution_time_ms > threshold_ms:
                    logger.warning(f"Slow function: {func.__name__} took {execution_time_ms:.2f}ms")
                else:
                    logger.info(f"{func.__name__} completed in {execution_time_ms:.2f}ms")
                
                return result
            except Exception as e:
                logger.error(f"Function {func.__name__} failed: {str(e)}", exc_info=True)
                raise
        return wrapper
    return decorator

@log_performance(threshold_ms=50)
def simulate_database_query(query_type="SELECT"):
    """Simulate a database operation"""
    database_logger.debug(f"Executing {query_type} query")
    time.sleep(random.uniform(0.01, 0.15))
    
    if random.random() < 0.1:
        database_logger.error(f"Database connection timeout")
        raise ConnectionError("Database connection failed")
    
    rows = random.randint(1, 100)
    database_logger.info(f"{query_type} query affected {rows} rows")
    return rows

def run_monitoring_demo():
    """Run the monitoring demonstration"""
    setup_logging()
    main_logger = logging.getLogger('main')
    main_logger.info("="*60)
    main_logger.info("Application Performance Monitor Started")
    main_logger.info("="*60)
    
    print("\nTesting Database Operations...")
    for i in range(3):
        try:
            simulate_database_query(random.choice(["SELECT", "UPDATE"]))
        except ConnectionError as e:
            main_logger.error(f"Database operation failed: {e}")
    
    main_logger.info("Application Performance Monitor Completed")

if __name__ == "__main__":
    run_monitoring_demo()
