# Combined Publisher-Subscriber Example
# Environment: Python 3.10+
# Required: No external dependencies

import time
from typing import List, Callable

class Topic:
    """Represents a message topic."""

    def __init__(self, name: str):
        self.name = name
        self.subscribers: List[Callable] = []

    def publish(self, message: str):
        """Send message to all subscribers."""
        print(f"[Topic {self.name}] Broadcasting: {message}")
        for callback in self.subscribers:
            callback(message)

    def subscribe(self, callback: Callable):
        """Register a subscriber."""
        self.subscribers.append(callback)

# Create topic
status_topic = Topic("/robot/status")

# Create subscribers
def display_callback(msg: str):
    """Subscriber 1: Display messages."""
    print(f"  [Display] Showing: {msg}")

def logger_callback(msg: str):
    """Subscriber 2: Log messages."""
    print(f"  [Logger] Logging: {msg}")

# Register subscribers
status_topic.subscribe(display_callback)
status_topic.subscribe(logger_callback)

# Publish messages
print("=== Starting Pub-Sub Demo ===\n")
for i in range(3):
    status_topic.publish(f"Cycle {i+1} complete")
    time.sleep(1)
    print()  # Blank line for readability

# Expected output:
# === Starting Pub-Sub Demo ===
#
# [Topic /robot/status] Broadcasting: Cycle 1 complete
#   [Display] Showing: Cycle 1 complete
#   [Logger] Logging: Cycle 1 complete
#
# [Topic /robot/status] Broadcasting: Cycle 2 complete
#   [Display] Showing: Cycle 2 complete
#   [Logger] Logging: Cycle 2 complete
#
# [Topic /robot/status] Broadcasting: Cycle 3 complete
#   [Display] Showing: Cycle 3 complete
#   [Logger] Logging: Cycle 3 complete
