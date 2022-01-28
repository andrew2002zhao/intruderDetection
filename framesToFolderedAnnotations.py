#steps


#make a new text file
#convert the annotation to a yolo format
#store the annotation it in a folder with the original image'
import random
from shutil import copyfile
from PIL import Image
import os


directory = os.path.dirname(__file__)
dataSetDirectory = os.path.join(directory, "testImages/Stanford Drone").replace("\\", "/")
finishedProductDirectory = os.path.join(dataSetDirectory, "finishedProduct").replace("\\", "/")
annotationsDirectory = os.path.join(dataSetDirectory, "annotations/annotations.txt").replace("\\", "/")
imageDirectory = os.path.join(dataSetDirectory, "images").replace("\\", "/")

def convert(id, size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0])
    y = (box[2])
    w = (box[1] - box[0])
    h = (box[3] - box[2])
    x = x * dw
    w = w * dw
    y = y*dh
    h = h*dh
    return [str(0),str(x),str(y),str(w),str(h)]

def traintestsplit():
    x = random.random()
    if(x < 0.1):
        return "test"
    elif(x < 0.7):
        return "train"
    else:
        return "validation"
image_number = 0
for filename in os.listdir(imageDirectory):

    frame = "a"
    # for each image take the image number, (this is the frame count)
    for s in filename.split():

        # find the annotations
        if ".png" in s:
            frame = s.replace(".png", "")
            type = traintestsplit()
            with open(annotationsDirectory, "r") as a_file:
                saved_lines = []
                labelNo = 0
                for line in a_file:
                    stripped_line = line.strip()
                    ar = stripped_line.split()

                    if (ar[5] == frame and ar[6] != "1" and ar[7] != "1" and ar[9] == "\"Pedestrian\""):

                        # convert to yolo format before appending

                        # hardcoded too lazy to find dimensions so opened image since each image is constant
                        w = 1417
                        h = 2019
                        b = [float(ar[1]), float(ar[3]), float(ar[2]), float(ar[4])]
                        bb = convert(labelNo, [w, h], b)
                        labelNo = labelNo + 1

                        stripped_line = ' '.join(bb)
                        # append string
                        saved_lines.append(stripped_line)
                


                with open(os.path.join(os.path.join(os.path.join(finishedProductDirectory, type), "labels"), "image" +  str(image_number) + ".txt").replace("\\", "/"), "w") as f:
                    print(saved_lines)
                    f.writelines('\n'.join(saved_lines))
                    f.close()
                a_file.close()
            img = Image.open(os.path.join(imageDirectory, "Stanford Drone" + " " + frame + ".png").replace("\\", "/"))
            img = img.resize((640, 640), Image.ANTIALIAS)
            img.save((os.path.join(os.path.join(os.path.join(finishedProductDirectory, type), "images"), "image" + str(image_number) + ".png").replace("\\", "/")))
            image_number = image_number + 1



