#!/usr/bin/env python3  # Shebang line to specify the script should be run with Python 3

import rclpy  # Import the rclpy library for ROS 2 Python client library
from rclpy.node import Node  # Import the Node class from the rclpy.node module

class MyNode(Node):  # Define a new class MyNode that inherits from the Node class
    def __init__(self):  # Constructor for the MyNode class
        super().__init__("first_node")  # Call the constructor of the parent class with the node name "first_node"
        # Create a timer that triggers the timer_callback function every 1 second (1.0 seconds)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):  # Callback function that gets called every time the timer expires
        self.get_logger().info("Hello")  # Log "Hello" to the console

def main(args=None):  # Define the main function
    rclpy.init(args=args)  # Initialize the ROS 2 client library
    node = MyNode()  # Create an instance of MyNode, which initializes the node and starts the timer
    rclpy.spin(node)  # Keep the node alive and processing callbacks until the program is terminated
    node.destroy_node()  # Clean up and destroy the node when spinning is done
    rclpy.shutdown()  # Shutdown the ROS 2 client library

if __name__ == '__main__':  # Check if the script is being run directly (not imported)
    main()  # Call the main function


'''
***************************first node program**********************************

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):  # Constructor
        super().__init__("first_node")
        self.get_logger().info("ROS2!")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()  # Create an instance of MyNode
    rclpy.spin(node)  # Keep the node running until manually interrupted
    node.destroy_node()  # Clean up the node
    rclpy.shutdown()

if __name__ == '__main__':
    main()

'''