import os
import cv2 as cv

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "testVideos")
imagename = os.path.join(dirname, "testImages")

vidcap = cv.VideoCapture(os.path.join(os.path.join(filename, "Stanford Drone"), "video.mp4"))
success, image = vidcap.read()
counter = 0
success = True
while success:

    cv.imwrite(os.path.join(os.path.join(imagename, "Stanford Drone/images"), "Stanford Drone " + str(counter) + ".png"), image)
    success, image = vidcap.read()
    counter = counter + 1
    print(counter)