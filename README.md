# Restaurant Butler Robot 🤖🍽️

This is a **ROS2-based restaurant butler robot** designed to automate food delivery in The French Door Café. The robot efficiently moves between the home position, kitchen, and customer tables (Table 1, 2, and 3), ensuring smooth and autonomous service.

## Features 🚀
- 🏠 Autonomous Navigation: Moves between home, kitchen, and tables.  
- 📦 Order Management: Handles multiple orders efficiently.  
- ⏳ Timeout Handling: Returns to home if no confirmation is received.  
- ❌ Order Cancellation: Returns to home or kitchen if an order is canceled.

- Installation & Running the Code ⚙️

Prerequisites

Ensure you have ROS 2 Humble installed and set up.

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/restaurant-butler-robot.git
cd restaurant-butler-robot

2. Build and Source the Workspace

cd ~/ros2_ws
colcon build
source install/setup.bash

3. Run the Order Manager Node

ros2 run restaurant_butler order_manager

4. Run the Butler Robot Node

ros2 run restaurant_butler butler_node

Future Improvements 🌟

✅ Navigation Stack: Implement path planning using SLAM & Nav2.

✅ Obstacle Avoidance: Add LiDAR or sensor-based obstacle detection.

✅ Voice Commands: Allow users to control the robot using voice.

Author 🤖

Nivedhan TS

Contact: tsnivedhan0@gmail.com

