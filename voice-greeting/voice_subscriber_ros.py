#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import os
import random

greeted = True
greet_count = 0

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    prediction, confidence = data.data.split(",")
    prediction = prediction.translate(None, "[']")
    confidence = confidence.translate(None, "[']")
    global greet_count
    if greet_count == 0:
        greeted = sound_play(prediction, confidence)
	greet_count = 10
    else:
	greet_count = greet_count - 1
    #if greeted:
        #rospy.sleep(5.)
	#greet_count = 5

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("predicter", String, callback)
    #rospy.sleep(5.)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def sound_play(prediction, confidence):
    #try:
    if float(confidence) < float(0.80):
        #os.system("mpg123 audio/guest.mp3")
	os.system("espeak 'hello guest'")
        return True
    else:
	#rand = random.choice([1,2])
        #command = "mpg123 audio/"+str(prediction)+str(rand)+".mp3"
	if str(prediction) == "anh":
		prediction = "ahn"
	command = "espeak 'hello "+str(prediction)+"'"
	print command
        os.system(command)
        return True
    #except:
        #return False;
    return False;

if __name__ == '__main__':
    listener()
