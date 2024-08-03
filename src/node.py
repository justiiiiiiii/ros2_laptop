import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

    def __init__(self):
        super().__init__('my_node')
        # sub joy signal
        self.subscription = self.create_subscription(float[5], 'joy', self.listener_callback, 10)
        # pub cmd_vel
        self.publisher_ = self.create_publisher(String, 'cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.declare_parameter('my_param', 'default_value')

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World'
        self.publisher_.publish(msg)
        self.get_logger().info('cmd_vel: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    my_node = MyNode()
    rclpy.spin(my_node)
    my_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
