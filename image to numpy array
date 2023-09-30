#using a sample image puppisa_w234.jpg
from PIL import Image
img= Image.open(r"C:\Users\HP\Downloads\nasa space apps challenge\data\puppisa_w234.jpg")
img.show()
import cv2

img=cv2.imread(r"C:\Users\HP\Downloads\nasa space apps challenge\data\puppisa_w234.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("org.Image",img)
cv2.imshow("gray image", gray)
cv2.imwrite("gray image.jpg", gray)
cv2.waitKey(0)
from matplotlib.image import imread
img=imread(r"C:\Users\HP\Downloads\nasa space apps challenge\data\puppisa_w234.jpg")
print(type(img))
#output  <class 'numpy.ndarray'>
img
#output array([[[11, 38,  0],
        [11, 36,  0],
        [11, 32, 15],
        ...,
        [41, 37, 34],
        [40, 38, 26],
        [40, 39, 21]],

       [[12, 38,  0],
        [12, 36,  0],
        [12, 33, 18],
        ...,
        [41, 38, 33],
        [40, 38, 26],
        [40, 39, 21]],

       [[12, 37,  0],
        [12, 35,  6],
        [13, 33, 22],
        ...,
        [38, 37, 32],
        [38, 38, 26],
        [38, 39, 21]],

       ...,

       [[24, 35, 21],
        [23, 34, 20],
        [23, 34, 20],
        ...,
        [26, 27, 29],
        [25, 27, 26],
        [24, 26, 25]],

       [[26, 35, 32],
        [25, 34, 31],
        [25, 34, 31],
        ...,
        [27, 28, 32],
        [26, 27, 29],
        [25, 27, 26]],

       [[28, 35, 43],
        [27, 34, 42],
        [27, 34, 40],
        ...,
        [28, 29, 33],
        [27, 28, 30],
        [25, 27, 26]]], dtype=uint8)
from matplotlib.image import imread
gray=imread(r"gray image.jpg")
print(type(gray))
#output  <class 'numpy.ndarray'>
gray
#output  array([[25, 24, 24, ..., 38, 37, 37],
       [25, 25, 25, ..., 38, 37, 37],
       [25, 25, 26, ..., 37, 37, 37],
       ...,
       [30, 29, 29, ..., 27, 26, 25],
       [32, 32, 31, ..., 28, 27, 26],
       [34, 33, 33, ..., 29, 28, 27]], dtype=uint8)
