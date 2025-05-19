#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class PlantNode(Node):
    def __init__(self):
        super().__init__('plant_node')
        self.x = 0.0
        self.u = 0.0
        self.sub = self.create_subscription(Float64, 'control_input', self.control_callback, 10)
        self.pub = self.create_publisher(Float64, 'plant_state', 10)
        self.timer = self.create_timer(0.1, self.update)

    def control_callback(self, msg):
        self.u = msg.data

    def update(self):
        self.x += self.u * 0.1  # simple integration step
        msg = Float64()
        msg.data = self.x
        self.get_logger().info(f'Plant state: {self.x:.2f}')
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PlantNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()