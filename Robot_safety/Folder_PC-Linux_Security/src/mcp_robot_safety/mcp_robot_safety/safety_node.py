#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped, Twist
from std_msgs.msg import Bool

class RobotnikSafetyFilter(Node):
    def __init__(self):
        super().__init__('robotnik_safety_filter')
        
        self.MAX_LINEAR_SPEED = 0.4
        self.MAX_ANGULAR_SPEED = 0.8
        self.emergency_stop = False
        self.current_linear = 0.0
        self.current_angular = 0.0

        # Subscriber Nav2
        self.sub_ai_cmd = self.create_subscription(
            TwistStamped,
            '/robot/robotnik_base_control/cmd_vel_raw',
            self.cmd_callback,
            10)
        
        # Subscriber téléop directe
        self.sub_teleop_cmd = self.create_subscription(
            Twist,
            '/robot/robotnik_base_control/cmd_vel_unstamped',
            self.teleop_callback,
            10)

        # Subscriber arrêt d'urgence
        self.sub_emergency = self.create_subscription(
            Bool,
            '/robot/safety_filter/emergency_stop',
            self.emergency_callback,
            10)
            
        # Publisher vers les moteurs
        self.pub_real_cmd = self.create_publisher(
            TwistStamped, 
            '/robot/robotnik_base_control/cmd_vel', 
            10)

        # Timer arrêt d'urgence (10 Hz)
        self.emergency_timer = self.create_timer(0.1, self.emergency_loop)

        # Timer tableau de bord (1 Hz — toutes les secondes)
        self.dashboard_timer = self.create_timer(5.0, self.dashboard_loop)
        
        self.get_logger().info('🛡️ Robotnik interceptor successfully activated !')

    def emergency_callback(self, msg):
        self.emergency_stop = msg.data
        if self.emergency_stop:
            self.get_logger().warn('🚨 EMERGENCY STOP ACTIVATED ! Robot halted.')
        else:
            self.get_logger().info('✅ Emergency stop released. Robot can move again.')

    def emergency_loop(self):
        if self.emergency_stop:
            stop_msg = TwistStamped()
            stop_msg.header.stamp = self.get_clock().now().to_msg()
            self.pub_real_cmd.publish(stop_msg)

    def dashboard_loop(self):
        emergency_status = "🚨 ACTIVE" if self.emergency_stop else "✅ INACTIVE"
        self.get_logger().info(
            f"\n"
            f"╔══════════════════════════════════╗\n"
            f"║       🤖 SAFETY FILTER DASHBOARD  ║\n"
            f"╠══════════════════════════════════╣\n"
            f"║ 🚀 Linear speed  : {self.current_linear:+.3f} m/s     ║\n"
            f"║ 🔄 Angular speed : {self.current_angular:+.3f} rad/s   ║\n"
            f"║ 🛑 Emergency     : {emergency_status:<20}║\n"
            f"╚══════════════════════════════════╝"
        )

    def cmd_callback(self, msg):
        if self.emergency_stop:
            return

        new_secure = TwistStamped()
        new_secure.header = msg.header 
        
        # Bridage vitesse linéaire
        if msg.twist.linear.x > self.MAX_LINEAR_SPEED:
            new_secure.twist.linear.x = self.MAX_LINEAR_SPEED
            self.get_logger().warn(f"⚠️ Intercepted speed ! Restricted to {self.MAX_LINEAR_SPEED} m/s")
        elif msg.twist.linear.x < -self.MAX_LINEAR_SPEED:
            new_secure.twist.linear.x = -self.MAX_LINEAR_SPEED
            self.get_logger().warn(f"⚠️ Intercepted retreat ! Restricted to {-self.MAX_LINEAR_SPEED} m/s")
        else:
            new_secure.twist.linear.x = msg.twist.linear.x

        # Bridage vitesse angulaire
        if abs(msg.twist.angular.z) > self.MAX_ANGULAR_SPEED:
            sign = 1 if msg.twist.angular.z > 0 else -1
            new_secure.twist.angular.z = self.MAX_ANGULAR_SPEED * sign
        else:
            new_secure.twist.angular.z = msg.twist.angular.z

        # Mise à jour des valeurs pour le dashboard
        self.current_linear = new_secure.twist.linear.x
        self.current_angular = new_secure.twist.angular.z

        self.pub_real_cmd.publish(new_secure)

    def teleop_callback(self, msg):
        stamped = TwistStamped()
        stamped.header.stamp = self.get_clock().now().to_msg()
        stamped.twist = msg
        self.cmd_callback(stamped)

def main(args=None):
    rclpy.init(args=args)
    node = RobotnikSafetyFilter()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
