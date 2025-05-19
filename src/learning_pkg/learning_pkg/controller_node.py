#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        self.target = 10.0  # desired position
        self.K = 1.0        # proportional gain
        self.state = 0.0
        self.pub = self.create_publisher(Float64, 'control_input', 10)
        self.sub = self.create_subscription(Float64, 'plant_state', self.state_callback, 10)

    def state_callback(self, msg):
        self.state = msg.data
        error = self.target - self.state
        u = self.K * error
        msg_out = Float64()
        msg_out.data = u
        self.get_logger().info(f'Sending control: {u:.2f}')
        self.pub.publish(msg_out)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()