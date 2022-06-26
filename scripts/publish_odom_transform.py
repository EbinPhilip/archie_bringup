#!/usr/bin/python3

import rospy

# Because of transformations
import tf_conversions

import tf2_ros
from nav_msgs.msg import Odometry
import geometry_msgs
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import PoseStamped

def handle_cb(odom_msg):
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()

    msg = odom_msg

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "odom"
    t.child_frame_id = "base_footprint"
    t.transform.translation.x = msg.pose.position.x
    t.transform.translation.y = msg.pose.position.y
    t.transform.translation.z = 0.0
    orientation = msg.pose.orientation
    (roll, pitch, yaw) = tf_conversions.transformations.euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation. w])
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, yaw)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('publish_odom_transform')
    rospy.Subscriber('/mavros/local_position/pose',
                     PoseStamped,
                     handle_cb)

    rospy.spin()