import cv2

'''
1. Read image by path.

cv2.imread(filename, channel)
--- filename: image file path string.
--- channel: 
        cv2.IMREAD_UNCHANGED    BGR / BGR-A
        cv2.IMREAD_COLOR        BGR
        cv2.IMREAD_GRAYSCALE    Gray
'''
im = cv2.imread("../rsrc/1.jpg", cv2.IMREAD_UNCHANGED)

'''
2. Get image shape.

Image size:
--- h: image height
--- w: image width
'''
h = im.shape[0]
w = im.shape[1]
print("height: %d, width: %d" % (h, w))

'''
3. Get image channel value.

im[y, x] return the colors at point(x, y)
In gray channel -> Integer (0 ~ 255)
In color channel -> [b, g, r] (0 ~ 255)
In unchanged channel -> [b, g, r, a] (0 ~ 255)
'''
point_y = 100
point_x = 100
print("color channel:", im[point_y, point_x])
