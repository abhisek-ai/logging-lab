# Python Logging Lab - Application Performance Monitor

A comprehensive Python logging tutorial that demonstrates advanced logging techniques through building a performance monitoring system.

## Features
- Performance monitoring decorators
- Multiple log handlers and formatters
- Custom log filters for sensitive data
- Log analysis and reporting
- Simulated database and API operations

### What It Demonstrates

1. **Database Operations Monitoring**
   - Simulates SELECT, UPDATE, INSERT queries
   - Tracks query execution times
   - Logs slow queries exceeding thresholds

2. **API Call Tracking**
   - Monitors REST API endpoints
   - Logs HTTP status codes
   - Tracks request/response times

3. **Security Logging**
   - Authentication attempt logging
   - Sensitive data masking
   - Failed login tracking with IP addresses

4. **Performance Analysis**
   - Identifies slow operations
   - Generates performance summaries
   - Creates detailed error reports

## 📁 Output Files

After running, the following log files are created:

- `performance_monitor.log` - Complete application logs with all levels
- `errors.log` - Error-level logs only for debugging

## 🎓 Learning Objectives

- Configure Python's logging module for production use
- Implement performance monitoring in applications
- Create custom log formatters and filters
- Handle sensitive data in logs securely
- Analyze logs programmatically
- Use decorators for aspect-oriented programming
- Implement context managers for resource tracking

## 📊 Sample Output

INFO: Application Performance Monitor Started
INFO: UPDATE query affected 20 rows
WARNING: Slow function: simulate_database_query took 133.42ms (threshold: 50ms)
INFO: [REQ-5054] GET /users Success: 200
INFO: Authentication attempt for user: admin
INFO: Total Errors: 0 | Total Warnings: 2 | Slow Functions: 6

## Requirements
- Python 3.6+
- No external dependencies (uses standard library)

## Files Generated
- `performance_monitor.log` - Detailed application logs
- `errors.log` - Error-level logs only
