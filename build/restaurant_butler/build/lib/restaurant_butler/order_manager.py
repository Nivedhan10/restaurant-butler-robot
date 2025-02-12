import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class OrderManager(Node):
    def __init__(self):
        super().__init__('order_manager')
        self.publisher_ = self.create_publisher(String, 'order_topic', 10)
        self.get_logger().info('Order Manager Ready. Waiting for orders...')

    def send_order(self, table_number):
        msg = String()
        msg.data = f"Order received for Table {table_number}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Sent order for Table {table_number}")

def main(args=None):
    rclpy.init(args=args)
    node = OrderManager()

    # Simulating orders
    node.send_order(1)
    node.send_order(2)
    node.send_order(3)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
