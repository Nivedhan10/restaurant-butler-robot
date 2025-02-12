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
        self.get_logger().info('Butler Node is running...')

    def handle_order(self, msg):
        order_info = msg.data
        self.get_logger().info(f"Received: {order_info}")

        # Extract table number
        table_number = int(order_info.split()[-1])

        # Move to kitchen
        self.get_logger().info("Moving to Kitchen...")
        time.sleep(2)

        # Simulate kitchen confirmation
        kitchen_confirmed = True
        if kitchen_confirmed:
            self.get_logger().info(f"Picked up food for Table {table_number}")

            # Move to customer table
            self.get_logger().info(f"Moving to Table {table_number}...")
            time.sleep(2)

            # Simulate customer confirmation
            customer_confirmed = True
            if customer_confirmed:
                self.get_logger().info(f"Delivered order to Table {table_number}")

                # Return to home
                self.get_logger().info("Returning to home position...")
                time.sleep(2)
                self.get_logger().info("Back at home position.")
            else:
                self.get_logger().info(f"No response at Table {table_number}, returning food to kitchen.")
                time.sleep(2)
        else:
            self.get_logger().info("No response from kitchen, returning to home.")
            time.sleep(2)

def main(args=None):
    rclpy.init(args=args)
    node = ButlerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
