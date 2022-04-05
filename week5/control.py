import rospy
from math import isinf
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def publish_velocity(linear_x, angular_z):
    while publisher.get_num_connections() < 1:
        pass
    move_message = Twist()
    move_message.linear.y = move_message.linear.z = 0.0
    move_message.angular.z = move_message.angular.y = 0.0
    move_message.linear.x = linear_x
    move_message.angular.z = angular_z
    publisher.publish(move_message)

def callback(data):
    rospy.loginfo(rospy.get_caller_id () + ": Object is %s meters away", data.ranges[0])
    if not isinf(data.ranges[0]) and data.ranges[0] <= 0.3:
        rospy.loginfo(rospy.get_caller_id () + ": Stopped robot")
        publish_velocity(0, 0)
    else:
        rospy.loginfo(rospy.get_caller_id () + ": Moving robot")
        publish_velocity(0.2, 0)

if __name__ == "__main__":
    rospy.init_node("listener", anonymous=True)
    publisher = rospy.Publisher("cmd_vel", Twist , queue_size = 100)
    rospy.Subscriber("scan", LaserScan , callback)
    rospy.spin()