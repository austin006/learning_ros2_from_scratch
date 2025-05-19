#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PongNode(Node):
    def __init__(self):
        super().__init__('pong_node')
        self.subscription = self.create_subscription(String, 'ping', self.ping_callback, 10)
        self.publisher_ = self.create_publisher(String, 'pong', 10)

    def ping_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')
        if msg.data == 'ping':
            reply = String()
            reply.data = 'pong'
            self.publisher_.publish(reply)
            self.get_logger().info('Sent: pong')

def main(args=None):
    rclpy.init(args=args)
    node = PongNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()