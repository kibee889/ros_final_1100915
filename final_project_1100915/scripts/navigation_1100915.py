#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from math import radians


class Navigation:
    def __init__(self):
        rospy.init_node('navigation', anonymous=False)
        self.cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel.publish(Twist())

    def move(self, distance, speed=0.2):
        move_cmd = Twist()
        move_cmd.linear.x = speed if distance > 0 else -speed

        rospy.loginfo(f"Moving {distance} meters")
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(abs(distance) / speed)
        self.cmd_vel.publish(Twist())
        rospy.sleep(0.1)

    def turn(self, angle, speed=0.8):
        move_cmd = Twist()
        move_cmd.angular.z = speed if angle > 0 else -speed

        rospy.loginfo(f"Turning {angle} degrees")
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(radians(abs(angle)) / speed + 0.6)
        self.cmd_vel.publish(Twist())
        rospy.sleep(0.1)

    def navigate_to_A(self):
        rospy.loginfo("Starting to navigate to A.")
        self.move(-0.2)
        self.turn(-90)
        self.move(2.44)
        self.turn(-90)
        self.move(1.44)
        rospy.loginfo("Arrived at A point.")

    def navigate_to_B(self):
        rospy.loginfo("Starting to navigate to B.")
        self.turn(90)
        self.turn(90)
        self.move(1.44)
        self.turn(90)
        self.move(5)
        self.turn(-90)
        self.move(1.6)
        self.turn(-90)
        self.move(0.5)
        rospy.loginfo("Arrived at B point.")

    def navigate_to_C(self):
        rospy.loginfo("Starting to navigate to C.")
        self.turn(-90)
        self.turn(-90)
        self.move(0.5)
        self.turn(90)
        self.move(1.6)
        self.turn(90)
        self.move(2)
        self.turn(-90)
        self.move(1.7)
        self.turn(-90)
        self.move(1.2)
        rospy.loginfo("Arrived at C point.")

    def shutdown(self):
        rospy.loginfo("Shutting down.")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        nav = Navigation()
        nav.navigate_to_A()
        nav.navigate_to_B()
        nav.navigate_to_C()
        rospy.loginfo("Navigation completed.")
    except rospy.ROSInterruptException:
        pass
