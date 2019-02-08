import cv2


'''
1. Read image by path.
'''
im = cv2.imread("../rsrc/1.jpg", cv2.IMREAD_COLOR)

'''
2. Crop the image.

im[ from_y : to_y, from_x : to_x ]
--- h: 380 - 110 = 270
--- w: 480 - 210 = 270 
'''
cropped_img = im[110:380, 210:480]

'''
3. Show image.
'''
cv2.imshow("original image", im)
cv2.imshow("cropped image", cropped_img)
cv2.waitKey(0)

'''
4. Change image color.

[0, 0, 0] => [B, G, R] => black
[255, 255, 255] => white
[255, 0, 0] => Blue
[0, 255, 0] => Green
[0, 0, 255] => Red
'''
im[110:380, 210:480] = [0, 0, 0]

'''
5. Show image again.
'''
cv2.imshow("original image", im)
cv2.imshow("cropped image", cropped_img)
cv2.waitKey(0)
