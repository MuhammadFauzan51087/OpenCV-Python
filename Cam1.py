import cv2
import imutils
from imutils.video import VideoStream
from imutils.video import FPS
import time
import redis
import math
import os


vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()
while True:
    frame = vs.read()
    frame = imutils.resize(frame,width=500)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    fps.update()
fps.stop()
cv2.destroyAllWindows()
vs.stop()

