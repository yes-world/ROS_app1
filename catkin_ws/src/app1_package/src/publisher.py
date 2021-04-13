#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

pub = rospy.Publisher("firstApp", String, queue_size=10)
rospy.init_node("firstAppPublisher")
m1 = "Hello"
m2 = "World!"
rospy.loginfo("Send: " + m1)
pub.publish(m1)
rospy.loginfo("Send: " + m2)
pub.publish(m2)