import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class ButlerNode(Node):
    def __init__(self):
        super().__init__('butler_node')
        self.subscription = self.create_subscription(
            String,
            'order_topic',
            self.handle_order,
            10)
        self.orders = []  
        self.get_logger().info('Butler Node is running...')

    def handle_order(self, msg):
        """Handles new orders and adds them to the list."""
        order_info = msg.data
        self.get_logger().info(f"Received: {order_info}")
        table_number = int(order_info.split()[-1])  
        self.orders.append(table_number)  


        if len(self.orders) == 1:
            self.process_orders()

    def process_orders(self):
        """Processes all orders one by one."""
        while self.orders:
            table_number = self.orders.pop(0)  
            self.get_logger().info(f"Processing order for Table {table_number}")

            # Simulate movement to kitchen and table
            self.get_logger().info("Moving to Kitchen...")
            time.sleep(2)

            # Simulate waiting for kitchen confirmation
            if not self.wait_for_confirmation("Kitchen"):
                self.get_logger().info("No response from kitchen, returning to home.")
                continue  

            self.get_logger().info(f"Picked up food for Table {table_number}")

            # Simulate movement to customer table
            self.get_logger().info(f"Moving to Table {table_number}...")
            time.sleep(2)

            # Simulate waiting for customer confirmation
            if not self.wait_for_confirmation(f"Table {table_number}"):
                self.get_logger().info(f"No response at Table {table_number}, returning food to kitchen.")
                self.return_to_kitchen()
                continue

            self.get_logger().info(f"Delivered order to Table {table_number}")

            # Return to home position
            self.get_logger().info("Returning to home position...")
            time.sleep(2)
            self.get_logger().info("Back at home position.")

    def wait_for_confirmation(self, location, timeout=5):
        """Simulates waiting for confirmation with timeout."""
        self.get_logger().info(f"Waiting for confirmation at {location}...")
        for _ in range(timeout):
            time.sleep(1)
            if self.simulate_confirmation(): 
                return True
        return False

    def simulate_confirmation(self):
        """Simulate confirmation (Always returns True here)."""
        return True  

    def return_to_kitchen(self):
        """Handles the return to kitchen if customer doesn't confirm."""
        self.get_logger().info("Returning food to kitchen...")
        time.sleep(2)
        self.get_logger().info("Food returned to kitchen.")

def main(args=None):
    rclpy.init(args=args)
    node = ButlerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

