from re import X
import rospy
from geometry_msgs.msg import Twist
from math import pi

def talker ():
    pub = rospy.Publisher("chatter", Twist , queue_size =100)
    rospy.init_node("talker", anonymous=True)
    rate = rospy.Rate (1) # 10hz
    while not rospy.is_shutdown ():
        message = Twist()
        message.linear.x = 0
        message.angular.z = pi
        pub.publish(message)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass