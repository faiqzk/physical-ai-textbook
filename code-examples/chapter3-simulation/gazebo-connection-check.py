# Conceptual Gazebo Connection Checker
# Environment: Python 3.10+
# Required: No external dependencies (conceptual only)

class GazeboTopicChecker:
    """Simulates checking if Gazebo is publishing sensor data."""

    def __init__(self):
        self.topics = {
            "/camera/image": False,
            "/scan": False,  # Lidar data
            "/odom": False   # Odometry (position/velocity)
        }

    def check_topic(self, topic_name: str):
        """Simulate checking if topic is active."""
        print(f"[Checker] Listening to {topic_name}...")
        self.topics[topic_name] = True
        print(f"[Checker] ✓ {topic_name} is active (receiving data from Gazebo)")

    def run_checks(self):
        """Check all expected topics."""
        print("=== Gazebo Connection Check ===\n")
        for topic in self.topics.keys():
            self.check_topic(topic)
        print("\n[Checker] All sensors connected successfully!")

# Usage
checker = GazeboTopicChecker()
checker.run_checks()

# Expected output:
# === Gazebo Connection Check ===
#
# [Checker] Listening to /camera/image...
# [Checker] ✓ /camera/image is active (receiving data from Gazebo)
# [Checker] Listening to /scan...
# [Checker] ✓ /scan is active (receiving data from Gazebo)
# [Checker] Listening to /odom...
# [Checker] ✓ /odom is active (receiving data from Gazebo)
#
# [Checker] All sensors connected successfully!
