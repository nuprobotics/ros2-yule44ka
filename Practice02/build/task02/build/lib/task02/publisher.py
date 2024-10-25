import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')

        # Get topic name from parameters
        topic_name = self.declare_parameter('topic_name', '/spgc/receiver').get_parameter_value().string_value
        self.publisher = self.create_publisher(String, topic_name, 10)

        # Get text parameter with default value
        self.text = self.declare_parameter('text', 'Hello, ROS2!').get_parameter_value().string_value

        # Set a timer for publishing messages
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Publish the message with the text from parameter
        msg = String()
        msg.data = self.text
        self.publisher.publish(msg)
        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
