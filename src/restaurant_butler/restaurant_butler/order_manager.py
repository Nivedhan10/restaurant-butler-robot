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

    while rclpy.ok():
        table_number = input("Enter table number (1-3) or 'exit' to quit: ")
        if table_number.lower() == 'exit':
            break
        if table_number.isdigit() and int(table_number) in [1, 2, 3]:
            node.send_order(int(table_number))
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
