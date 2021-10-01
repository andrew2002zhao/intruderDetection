import os
import cv2 as cv

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "testVideos")
imagename = os.path.join(dirname, "testImages")
for file in os.listdir(filename):
    vidcap = cv.VideoCapture(os.path.join(os.path.join(filename, file), "video.mp4"))
    success, image = vidcap.read()
    counter = 0
    success = True
    while success:

        if(counter % 30 == 0) :

            cv.imwrite(os.path.join(os.path.join(imagename, file), file + str(int(counter/30)) + ".png"), image)

        success, image = vidcap.read()
        counter = counter + 1
        print(counter)