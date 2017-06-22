'''
Captures an image from webcam every N seconds using OpenCV
'''
import time
from cv2 import *

# Use /dev/video1
# If using another device, change 1 to device number
cam = VideoCapture(0)

def capture(index, name):
    s, img = cam.read()
    if s:
        #namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        #imshow("cam-test",img)
        #waitKey(0)
        #destroyWindow("cam-test")
        imwrite("evolvingai/"+name+"/image-"+index+".jpg",img)

if __name__ == '__main__':
    # Name of the person that's getting their photos taken
    name = "anh2"
    # Run this for 6 hours
    for i in range(0,21600):
        # Take photo every 10 seconds
        print(i)
        if i%1 == 0:
	    #print("captured!")
            capture(str(i/1),name)
        time.sleep(1)
	
