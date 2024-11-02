#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):  # Constructor
        super().__init__("first_node")
        self.get_logger().info("Hello from ROS2!")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()  # Create an instance of MyNode
    rclpy.spin(node)  # Keep the node running until manually interrupted
    node.destroy_node()  # Clean up the node
    rclpy.shutdown()

if __name__ == '__main__':
    main()
