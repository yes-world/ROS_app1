#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s", data.data)

def subscriber():
    rospy.init_node("firstAppSubscriber")
    rospy.Subscriber("firstApp", String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()