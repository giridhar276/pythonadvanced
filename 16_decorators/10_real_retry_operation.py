"""
Example 10: Real-World Decorator - Retry a Failed Operation

Use case:
Retry a temporary failure while sending a notification.
The failure is simulated for classroom learning.
"""


def retry(function):
    def wrapper():
        for attempt in range(1, 4):
            try:
                return function()
            except ConnectionError:
                print("Attempt", attempt, "failed. Retrying...")
        print("All attempts failed.")
    return wrapper


attempt_count = 0


@retry
def send_notification():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("Temporary network error")
    print("Notification sent successfully!")


send_notification()
