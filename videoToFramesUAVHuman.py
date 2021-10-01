import os
import cv2 as cv

dirpath = os.path.dirname(__file__)
filepath = os.path.join(dirpath, "testVideos/UAV Human/all_rgb/all_rgb")
imagename = os.path.join(dirpath, "testImages/UAV Human")
for file in os.listdir(filepath):

    vidcap = cv.VideoCapture(os.path.join(os.path.join(filepath, file)))
    success, image = vidcap.read()
    counter = 0
    success = True
    while success:

        if (counter % 60 == 0):

            cv.imwrite(os.path.join(imagename, file + str(int(counter / 60)) + ".png"), image)

        success, image = vidcap.read()
        counter = counter + 1
        print(counter)



