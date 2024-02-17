import cv2
import time
import math

video = cv2.VideoCapture("footvolleyball.mp4")
#load tracker 
tracker = cv2.TrackerCSRT_create()

#read the first frame of the video
success,img = video.read()

while success:
    #selct the bounding box on the image
    bbox = cv2.selectROI("tracking",img,False)

    if bbox[2] > 0 and bbox[3] > 0:  # Check if the bounding box has a valid size
        #initialise the tracker on the img and the bounding box
        tracker.init(img,bbox)

        break

    cv2.putText(img, "Please select a valid ROI", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("tracking", img)
    cv2.waitKey(0)
    success,img = video.read()

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

while True:
    #Write the code inside loop here
    success,img = video.read() 

    if not success:
        break

    #update the tracker on the img and the bounging box
    success,bbox=tracker.update(img)  

    if success :
        drawBox(img,bbox)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break

video.release()
cv2.destroyAllWindows()
