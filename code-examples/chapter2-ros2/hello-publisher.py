# Conceptual ROS 2 Publisher Example
# Environment: Python 3.10+
# Required: No external dependencies

import time

class SimplePublisher:
    """Simulates a ROS 2 publisher that sends messages to a topic."""

    def __init__(self, topic_name: str):
        self.topic = topic_name
        print(f"[Publisher] Started publishing to topic: {self.topic}")

    def publish(self, message: str):
        """Publish a message to the topic."""
        print(f"[Publisher → {self.topic}] {message}")

# Usage
publisher = SimplePublisher("/robot/status")
for i in range(5):
    publisher.publish(f"Robot is running: cycle {i+1}")
    time.sleep(1)  # Publish once per second

# Expected output:
# [Publisher] Started publishing to topic: /robot/status
# [Publisher → /robot/status] Robot is running: cycle 1
# [Publisher → /robot/status] Robot is running: cycle 2
# [Publisher → /robot/status] Robot is running: cycle 3
# [Publisher → /robot/status] Robot is running: cycle 4
# [Publisher → /robot/status] Robot is running: cycle 5
