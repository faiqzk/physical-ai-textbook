# Simple Robot Decision-Making Demo
# Environment: Python 3.10+
# Required: No external dependencies

import random

class SimpleRobot:
    """A robot that avoids obstacles using sense-think-act cycle."""

    def __init__(self, name: str):
        self.name = name
        self.position = 0  # Robot's position on a line

    def sense(self):
        """Sense: Check if obstacle is ahead (simulated with random)."""
        distance_to_obstacle = random.randint(1, 10)
        print(f"[SENSE] {self.name} detects obstacle {distance_to_obstacle} units ahead")
        return distance_to_obstacle

    def think(self, distance: int):
        """Think: Decide action based on sensor data."""
        if distance < 3:
            decision = "stop"
            print(f"[THINK] Too close! Decision: {decision}")
        elif distance < 6:
            decision = "slow_down"
            print(f"[THINK] Getting close. Decision: {decision}")
        else:
            decision = "move_forward"
            print(f"[THINK] Path is clear. Decision: {decision}")
        return decision

    def act(self, decision: str):
        """Act: Execute the decision."""
        if decision == "move_forward":
            self.position += 2
            print(f"[ACT] Moving forward to position {self.position}")
        elif decision == "slow_down":
            self.position += 1
            print(f"[ACT] Slowing down, now at position {self.position}")
        else:  # stop
            print(f"[ACT] Stopping at position {self.position}")

    def run_cycle(self):
        """Run one sense-think-act cycle."""
        distance = self.sense()        # Step 1: Sense
        decision = self.think(distance) # Step 2: Think
        self.act(decision)              # Step 3: Act
        print()  # Blank line for readability

# Create and run robot for 3 cycles
robot = SimpleRobot("WallE")
print("=== Running 3 Sense-Think-Act Cycles ===\n")
for cycle in range(1, 4):
    print(f"--- Cycle {cycle} ---")
    robot.run_cycle()

# Expected output (random, so varies):
# === Running 3 Sense-Think-Act Cycles ===
#
# --- Cycle 1 ---
# [SENSE] WallE detects obstacle 7 units ahead
# [THINK] Path is clear. Decision: move_forward
# [ACT] Moving forward to position 2
#
# --- Cycle 2 ---
# [SENSE] WallE detects obstacle 2 units ahead
# [THINK] Too close! Decision: stop
# [ACT] Stopping at position 2
#
# --- Cycle 3 ---
# [SENSE] WallE detects obstacle 5 units ahead
# [THINK] Getting close. Decision: slow_down
# [ACT] Slowing down, now at position 3
