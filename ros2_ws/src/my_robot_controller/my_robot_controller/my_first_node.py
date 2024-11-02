#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):  # Constructor
        super().__init__("first_node")
        self.create_timer(1.0,self.timer_callback)


        def timer_callback(self):
            self.get_logger().info("Hello")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()  # Create an instance of MyNode
    rclpy.spin(node)  # Keep the node running until manually interrupted
    node.destroy_node()  # Clean up the node
    rclpy.shutdown()

if __name__ == '__main__':
    main()


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