# Conceptual ROS 2 Subscriber Example
# Environment: Python 3.10+
# Required: No external dependencies

class SimpleSubscriber:
    """Simulates a ROS 2 subscriber that listens to a topic."""

    def __init__(self, topic_name: str):
        self.topic = topic_name
        print(f"[Subscriber] Listening to topic: {self.topic}")

    def callback(self, message: str):
        """Called when a message arrives on the topic."""
        print(f"[Subscriber ← {self.topic}] Received: {message}")

# Usage
subscriber = SimpleSubscriber("/robot/status")

# Simulate receiving messages
messages = ["Robot is running: cycle 1", "Robot is running: cycle 2", "Robot is running: cycle 3"]
for msg in messages:
    subscriber.callback(msg)

# Expected output:
# [Subscriber] Listening to topic: /robot/status
# [Subscriber ← /robot/status] Received: Robot is running: cycle 1
# [Subscriber ← /robot/status] Received: Robot is running: cycle 2
# [Subscriber ← /robot/status] Received: Robot is running: cycle 3
