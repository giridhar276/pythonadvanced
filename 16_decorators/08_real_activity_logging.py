"""
Example 08: Real-World Decorator - Activity Logging

Use case:
Record actions when employees access a service.
"""

from datetime import datetime


def activity_log(function):
    def wrapper(employee_name):
        print("Action:", function.__name__)
        print("Employee:", employee_name)
        print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return function(employee_name)
    return wrapper


@activity_log
def download_report(employee_name):
    print("Report downloaded successfully for", employee_name)


download_report("Kiran")
