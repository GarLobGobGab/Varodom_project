#!usr/bin/env python
# from robot import msg
import rospy
# from robot.msg import robot_msg
from geometry_msgs.msg import Twist


def joy_function():
    rospy.init_node('joystick_node')
    pub = rospy.Publisher('joystick_topic' , Twist , queue_size=10)
    rate = rospy.Rate(10) #10hz
    motor_msg = Twist()
    motor_msg.linear.x = 2
    motor_msg.angular.z = 3
    pub.publish(motor_msg)
    rate.sleep()



if __name__ == '__main__':
    while not rospy.is_shutdown():
        joy_function()
        