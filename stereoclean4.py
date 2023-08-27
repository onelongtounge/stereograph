from PIL import Image
from numpy import asarray
import numpy as np
import os
from tqdm import tqdm

# list folders
#sorcepath="/home/pi/Downloads/"
sorcepath="/home/pi/Pictures/archive/"
d=0
for root, dirs, files in os.walk(sorcepath):
    for file in files:
        p=os.path.join(root,file)
        print(file)
        print(p)
        print(os.path.abspath(p))
        
        

        print("converting {file}")
        
        image = Image.open(p).convert("L")# monochromw
        imageleft = Image.open(p) 
        # convert image to 2 numpy arrays
        data = asarray(image)
        imgl = asarray(imageleft)
        imgr = asarray(imageleft)
        print(type(data))
        # summarize shape
        print(data.shape)

        # creat Pillow image
        image2 = Image.fromarray(data)
        image3 = Image.fromarray(imgl)
        image4 = Image.fromarray(imgr)
        print(type(image2))

        #image2.show()
        #image3.show()
        #image4.show()
        pics=0
        w,h = image2.size
        print("width ",w,"hight ",h)

        # converting 2d to 3d

        for x in range (w-52):
            for y in range(h):
                n=int(data[y,x]/20)
                #n=int(data[y,x]/10)
                n=x+n
                #if data[y,x]<data[y,n]:
                imgr[y,x]=imgl[y,n]
                    
            
        d+=1

        #image4 = Image.fromarray(imgr)
        #imagel = Image.fromarray(imgl)
        #print(type(image4))
        #image4.show()
        #image3.show()
        imagesbs = np.hstack((imgl,imgr))
        image5 = Image.fromarray(imagesbs).save(f'/home/pi/Pictures/archive/%d.jpg' %(d))
        #image6 = Image.fromarray(imagesbs).save(f'/home/pi/download/{file}')
        print("{file} complette")
        print("{d}")