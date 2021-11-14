#!/usr/bin/env python
import rospy
from robot.msg import robot_msg
from geometry_msgs.msg import Twist
from pyPS4Controller.controller import Controller
motor_msg = Twist()
motor_msg.linear.x = 0
motor_msg.angular.z = 0

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        rospy.init_node('joystick_node')
        self.pub = rospy.Publisher('joystick_topic' , Twist , queue_size=10)
        self.rate = rospy.Rate(10)
    def on_up_arrow_press(self):
        motor_msg.linear.x = 1
        self.pub.publish(motor_msg)
        self.rate.sleep()
    def on_down_arrow_press(self):
        motor_msg.linear.x = 2
        self.pub.publish(motor_msg)
        self.rate.sleep()
    def on_left_arrow_press(self):
        motor_msg.angular.x = 3
        self.pub.publish(motor_msg)
        self.rate.sleep()
    def on_right_arrow_press(self):
        motor_msg.angular.x = 4
        self.pub.publish(motor_msg)
        self.rate.sleep()
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
            controller.listen(timeout=60)
    except rospy.ROSInterruptException:
        pass