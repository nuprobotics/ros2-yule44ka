import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class ReceiverNode(Node):
    def __init__(self):
        # Initialize the node with the name 'receiver'
        super().__init__('receiver')
        # Create a subscriber to listen to the '/spgc/sender' topic
        self.subscriber = self.create_subscription(
            String,
            '/spgc/sender',  # Topic name
            self.subscriber_callback,
            qos_profile=10  # Quality of Service profile
        )

    def subscriber_callback(self, msg):
        # Log the received message at INFO level
        self.get_logger().info(f"Received: {msg.data}")

def main():
    rclpy.init()
    node = ReceiverNode()  # Create an instance of ReceiverNode
    rclpy.spin(node)  # Keep the node running
    rclpy.shutdown()  # Shutdown ROS2 when finished

if __name__ == '__main__':
    main()

