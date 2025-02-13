# Restaurant Butler Robot 🤖🍽️


This is a ROS 2-based autonomous restaurant butler robot designed to streamline food delivery operations at The French Door Café. By leveraging ROS 2 Humble, this robot automates food orders, moving seamlessly between the home position, kitchen, and customer tables (Table 1, Table 2, and Table 3). With simple yet effective task management, it ensures timely and efficient service.

Features 🚀
🏠 Autonomous Navigation: Efficiently moves between the home, kitchen, and customer tables using ROS 2's navigation stack.

📦 Order Management: Handles multiple orders, ensuring accurate delivery to the right table in sequence.

⏳ Timeout Handling: If no confirmation is received from the kitchen or customer table, the robot returns to its home position after a timeout.

❌ Order Cancellation: If an order is canceled, the robot returns to the kitchen or home, based on the task stage.

Installation & Running the Code ⚙️

Prerequisites

Ensure ROS 2 Humble is installed and properly configured on your system.
Clone the Repository
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Nivedhan10/restaurant-butler-robot.git 
cd restaurant-butler-robot
Build and Source the Workspace
Make sure you build and source your workspace:

bash
Copy
Edit
cd ~/ros2_ws
colcon build
source install/setup.bash
Running the Code
Run the Order Manager Node (Simulates order placement):
bash
Copy
Edit
ros2 run restaurant_butler order_manager
Run the Butler Robot Node (Executes the robot's food delivery tasks):
bash
Copy
Edit
ros2 run restaurant_butler butler_node
Future Improvements 🌟
✅ Navigation Stack: Implement advanced path planning using SLAM and Nav2 for dynamic environments.

✅ Obstacle Avoidance: Integrate LiDAR or other sensor-based solutions for real-time obstacle detection and avoidance.

✅ Voice Commands: Enable voice control for an enhanced user experience and better interactivity with the robot.

Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/restaurant-butler-robot.git
cd restaurant-butler-robot
Build and Source the Workspace
bash
Copy
Edit
cd ~/ros2_ws
colcon build
source install/setup.bash
Run the Nodes
Start the Order Manager Node

bash
Copy
Edit
ros2 run restaurant_butler order_manager
Start the Butler Robot Node

bash
Copy
Edit
ros2 run restaurant_butler butler_node
Test Cases 🧪
1️⃣ Basic Order Delivery: Robot moves from home → kitchen → table → home.
2️⃣ No Confirmation at Kitchen: Returns home after timeout.
3️⃣ No Confirmation at Table: Returns food to the kitchen before going home.
4️⃣ Order Cancellation Before Kitchen: Returns home immediately.
5️⃣ Order Cancellation Before Table: Returns food to kitchen, then goes home.
6️⃣ Multiple Orders: Collects all orders and delivers them sequentially.
7️⃣ Skipped Table: If a table does not confirm, it moves to the next one.

Future Improvements 🌟
🚀 Navigation Stack: Implement path planning using Nav2.
🔍 Obstacle Avoidance: Add LiDAR for dynamic path adjustments.
🗣️ Voice Commands: Control the robot via voice input.

Demo Video 🎥
A demo video showcasing all 7 test cases is recorded using Snipping Tool and included in the repository.



Author 🤖

Nivedhan TS

Email: tsnivedhan0@gmail.com

LinkedIn: https://www.linkedin.com/in/nivedhan-ts/

GitHub:  https://github.com/Nivedhan10


