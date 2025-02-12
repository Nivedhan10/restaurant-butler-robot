import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class OrderManager(Node):
    def __init__(self):
        super().__init__('order_manager')
        self.publisher_ = self.create_publisher(String, 'orders', 10)
        self.get_logger().info('Order Manager Ready. Waiting for orders...')
        
        # Simulating orders
        for table in range(1, 4):
            time.sleep(1)
            msg = String()
            msg.data = f'Order received for Table {table}'
            self.publisher_.publish(msg)
            self.get_logger().info(f'Sent order for Table {table}')

class ButlerNode(Node):
    def __init__(self):
        super().__init__('butler_node')
        self.subscription = self.create_subscription(
            String,
            'orders',
            self.order_callback,
            10)
        self.get_logger().info('Butler Node is running...')

    def order_callback(self, msg):
        table_number = msg.data.split()[-1]  # Extract table number
        self.get_logger().info(f'Received: {msg.data}')
        self.execute_order(table_number)

    def execute_order(self, table):
        steps = [
            "Moving to Kitchen...",
            f"Picked up food for Table {table}",
            f"Moving to Table {table}...",
            f"Delivered order to Table {table}",
            "Returning to home position...",
            "Back at home position."
        ]
        for step in steps:
            time.sleep(2)
            self.get_logger().info(step)

# ROS2 Entry Point
def main(args=None):
    rclpy.init(args=args)
    order_manager = OrderManager()
    butler_node = ButlerNode()
    
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(order_manager)
    executor.add_node(butler_node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        order_manager.destroy_node()
        butler_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
