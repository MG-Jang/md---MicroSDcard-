#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('my_node', anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

msg = Twist()
msg.linear.x = 2.0
msg.linear.y = 0.0
msg.linear.z = 0.0
msg.angular.x = 0.0
msg.angular.y = 0.0
msg.angular.z = 1.55

rate = rospy.Rate(0.98)

while not rospy.is_shutdown():
	for i in range(4):
		pub.publish(msg)
		rate.sleep()
	else: msg.angular.z *= -1