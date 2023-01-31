import os
import cv2


path = "Images/"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame =cv2.imread(images[0])
hight,width,channels= frame.shape
size= (width,hight)
print(size)

out= cv2.VideoAlbum('project.avi',cv2.VideoAlbum_fourcc(*'xvid'),0.8,size)

for i in range ('count-1,0,-1'):
    frame= cv2.imread(images[i])
    out.write(frame)

out.release()
print("done")
