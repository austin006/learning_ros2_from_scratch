#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PingNode(Node):
    def __init__(self):
        super().__init__('ping_node')
        self.publisher_ = self.create_publisher(String, 'ping', 10)
        self.subscription = self.create_subscription(String, 'pong', self.pong_callback, 10)
        self.timer = self.create_timer(2.0, self.send_ping)

    def send_ping(self):
        msg = String()
        msg.data = 'ping'
        self.get_logger().info('Sent: ping')
        self.publisher_.publish(msg)

    def pong_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PingNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()