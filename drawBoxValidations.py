# Python program to explain cv2.rectangle() method

# importing cv2
import cv2

# path
import os

def open_file(path):
    with open(path, "r") as file:
        for line in file:
            arr = line.split()
            start_point, end_point = convert_coords(arr, 640, 640)
            draw_rectangle(start_point, end_point)

def convert_coords(textArray, w, l):
    start_point = (round(float(textArray[1]) * w), round(float(textArray[2]) * l))
    end_point = (round((float(textArray[1]) + float(textArray[3])) * w), round((float(textArray[2]) + float(textArray[4]))* l))
    return start_point, end_point
def draw_rectangle(start_point, end_point):
    testImage = os.path.join(path, "test/images/image10.png").replace("/", "\\")
    print(testImage)
    # Reading an image in default mode
    image = cv2.imread(testImage)

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    image = cv2.rectangle(image, start_point, end_point, color, thickness)

    # Window name in which image is displayed
    window_name = 'Image'
    # Displaying the image
    cv2.imshow(window_name, image)
    cv2.waitKey()

directory = os.path.dirname(__file__)
path = os.path.join(directory, "testImages/Stanford Drone/finishedProduct")

testLabels = os.path.join(path, "test/labels/image10.txt").replace("/", "\\")

open_file(testLabels)











