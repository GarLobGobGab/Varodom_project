#!/usr/bin/env python
import rospy
# from robot.msg import robot_msg
from geometry_msgs.msg import Twist
import array as arr

def vel_li_x(vel_msg):
    rospy.loginfo("Vel X : {}".format(vel_msg.linear.x))
def vel_an_y(vel_msg):
    rospy.loginfo("Vel Y : {}".format(vel_msg.angular.x))
# def vel_z(vel_msg):
#     rospy.loginfo("Vel Z : {}".format(vel_msg.vel[2]))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motor_node', anonymous=True)

    rospy.Subscriber("joystick_topic", Twist, vel_li_x)
    rospy.Subscriber("joystick_topic", Twist, vel_an_y)
    # rospy.Subscriber("joystick_topic", robot_msg, vel_z)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()