import rospy
from geometry_msgs.msg import Twist
from math import pi

def turn_left():
    print("Turning left (Spin 90 degrees - Pi radian)")
    publish_velocity(0, pi / 2)
    rate = rospy.Rate(1)
    rate.sleep()

def move_forward(distance):
    print("Moving forward " + str(distance) + "m")
    publish_velocity(distance, 0)
    rate = rospy.Rate(1)
    rate.sleep()

def publish_velocity(linear_x, angular_z):
    while publisher.get_num_connections() < 1:
        pass
    move_message = Twist()
    move_message.linear.y = move_message.linear.z = 0.0
    move_message.angular.z = move_message.angular.y = 0.0
    move_message.linear.x = linear_x
    move_message.angular.z = angular_z
    publisher.publish(move_message)

rospy.init_node("controller", anonymous=False)
publisher = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10000)
while publisher.get_num_connections() < 1:
    pass
for i in range(4):
    move_forward(2)
    turn_left()

