import tkinter as tk
from PIL import ImageTk, Image
import cv2
import webbrowser
import numpy as np
import math


class OpenCVLearningTool:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("640x260")
        self.window.title("OpenCV Learning Tool")
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.frame.focus_set()
        self.create()
        
    def create(self):
        self.key = ''
        self.original = tk.Label(self.frame)
        self.original.pack(side=tk.LEFT)
        self.output = tk.Label(self.frame)
        self.output.pack(side=tk.RIGHT)
        self.link = tk.Label(self.window, text="Github", fg="blue", cursor="hand2")
        self.link.pack(side=tk.BOTTOM)
        self.link.bind("<Button-1>", self.onclick_github)
        
        self.menubar = tk.Menu(self.window)
        # menu1
        self.menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="原圖", command=self.onclick_menu1_1)
        self.menu1.add_command(label="灰階", command=self.onclick_menu1_2)
        self.menu1.add_command(label="灰度二值化", command=self.onclick_menu1_3)
        self.menu1.add_command(label="區域閥值", command=self.onclick_menu1_4)
        self.menu1.add_command(label="HSV", command=self.onclick_menu1_5)
        self.menu1.add_command(label="HSV 紅色", command=self.onclick_menu1_6)
        self.menu1.add_command(label="HSV 藍色", command=self.onclick_menu1_7)
        # menu2
        self.menu2 = tk.Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="翻轉", command=self.onclick_menu2_1)
        self.menu2.add_command(label="縮放", command=self.onclick_menu2_2)
        self.menu2.add_command(label="旋轉", command=self.onclick_menu2_3)
        self.menu2.add_command(label="轉置", command=self.onclick_menu2_4)
        self.menu2.add_command(label="濾波", command=self.onclick_menu2_5)
        # menu3
        self.menu3 = tk.Menu(self.menubar, tearoff=0)
        self.menu3.add_command(label="腐蝕", command=self.onclick_menu3_1)
        self.menu3.add_command(label="膨脹", command=self.onclick_menu3_2)
        self.menu3.add_command(label="開運算", command=self.onclick_menu3_3)
        self.menu3.add_command(label="閉運算", command=self.onclick_menu3_4)
        self.menu3.add_command(label="Morphological Gradient", command=self.onclick_menu3_5)
        self.menu3.add_command(label="頂帽", command=self.onclick_menu3_6)
        self.menu3.add_command(label="黑帽", command=self.onclick_menu3_7)
        # menu4
        self.menu4 = tk.Menu(self.menubar, tearoff=0)
        self.menu4.add_command(label="二值輪廓", command=self.onclick_menu4_1)
        self.menu4.add_command(label="紅色輪廓", command=self.onclick_menu4_2)
        self.menu4.add_command(label="紅色輪廓 - 去除小面積區域", command=self.onclick_menu4_3)
        self.menu4.add_command(label="紅色輪廓 - 周長與面積", command=self.onclick_menu4_4)
        self.menu4.add_command(label="紅色輪廓 - 最小外接矩形", command=self.onclick_menu4_5)
        self.menu4.add_command(label="紅色輪廓 - 外接矩形", command=self.onclick_menu4_6)
        # menu5
        self.menu5 = tk.Menu(self.menubar, tearoff=0)
        self.menu5.add_command(label="紅色幾何圖形辨識", command=self.onclick_menu5_1)
        self.menu5.add_command(label="紅色固定寛矩形長度", command=self.onclick_menu5_2)
        
        self.menubar.add_cascade(label='顏色處理', menu=self.menu1)
        self.menubar.add_cascade(label='影像處理', menu=self.menu2)
        self.menubar.add_cascade(label='形態學處理', menu=self.menu3)
        self.menubar.add_cascade(label='邊緣辨識', menu=self.menu4)
        self.menubar.add_cascade(label='簡單應用', menu=self.menu5)
        self.window.config(menu=self.menubar)
    
    def run(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.update_frame()
        self.window.mainloop()
        
    def update_frame(self):
        _, frame = self.cap.read()
        
        self.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img = self.filter(self.image)
        
        img = ImageTk.PhotoImage(Image.fromarray(img))
        self.output.config(image=img)
        self.output.image = img
        
        original = ImageTk.PhotoImage(Image.fromarray(self.image))
        self.original.config(image=original)
        self.original.image = original
        
        self.window.after(25, self.update_frame)
    
    def onclick_github(self, event):
        print(event)
        webbrowser.open_new(r"http://github.com/supercatex")
        
    def onclick_menu1_1(self): self.key = ''
    def onclick_menu1_2(self): self.key = 'gray'
    def onclick_menu1_3(self): self.key = 'gray_thresh'
    def onclick_menu1_4(self): self.key = 'gray_adaptive_threshold'
    def onclick_menu1_5(self): self.key = 'hsv'
    def onclick_menu1_6(self): self.key = 'hsv_red'
    def onclick_menu1_7(self): self.key = 'hsv_blue'
    
    def onclick_menu2_1(self): self.key = 'flip'
    def onclick_menu2_2(self): self.key = 'resize'
    def onclick_menu2_3(self): self.key = 'rotate'
    def onclick_menu2_4(self): self.key = 'transpose'
    def onclick_menu2_5(self): self.key = 'filter'
    
    def onclick_menu3_1(self): self.key = 'erode'
    def onclick_menu3_2(self): self.key = 'dilate'
    def onclick_menu3_3(self): self.key = 'morph_open'
    def onclick_menu3_4(self): self.key = 'morph_close'
    def onclick_menu3_5(self): self.key = 'morph_granient'
    def onclick_menu3_6(self): self.key = 'morph_tophat'
    def onclick_menu3_7(self): self.key = 'morph_blackhat'
    
    def onclick_menu4_1(self): self.key = 'contour_threshold'
    def onclick_menu4_2(self): self.key = 'contour_red'
    def onclick_menu4_3(self): self.key = 'contour_red_delete_small_area'
    def onclick_menu4_4(self): self.key = 'contour_red_arclength'
    def onclick_menu4_5(self): self.key = 'contour_red_min_rect'
    def onclick_menu4_6(self): self.key = 'contour_red_rect'
    
    def onclick_menu5_1(self): self.key = 'poly_detect'
    def onclick_menu5_2(self): self.key = 'rect_length_detect'
    
    def filter(self, image):
        if self.key == '':
            return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        elif self.key == 'gray':
            return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        elif self.key == 'gray_thresh':
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            return threshold
        elif self.key == 'gray_adaptive_threshold':
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 8)
            return threshold
        elif self.key == 'hsv':
            return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        elif self.key == 'hsv_red':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            return cv2.inRange(hsv, lower, upper)
        elif self.key == 'hsv_blue':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (100, 84, 127)
            upper = (124, 255, 255)
            return cv2.inRange(hsv, lower, upper)
        elif self.key == 'flip':
            return cv2.flip(image, 1)
        elif self.key == 'resize':
            return cv2.resize(image, (160, 120), interpolation=cv2.INTER_CUBIC)
        elif self.key == 'rotate':
            (h, w) = image.shape[:2]
            center = (w / 2, h / 2)
            angle = 45
            scale = 1.0
            M = cv2.getRotationMatrix2D(center, angle, scale)
            rotated = cv2.warpAffine(image, M, (w, h))
            return rotated
        elif self.key == 'transpose':
            return cv2.transpose(image)
        elif self.key == 'filter':
            return cv2.GaussianBlur(image, (5, 5), 0)
        elif self.key == 'erode':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            return cv2.erode(image, kernel)
        elif self.key == 'dilate':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            return cv2.dilate(image, kernel)
        elif self.key == 'morph_open':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        elif self.key == 'morph_close':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        elif self.key == 'morph_granient':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
        elif self.key == 'morph_tophat':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            return cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
        elif self.key == 'morph_blackhat':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            return cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
        elif self.key == 'contour_threshold':
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
            self.image = threshold
            return img
        elif self.key == 'contour_red':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            threshold = cv2.inRange(hsv, lower, upper)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
            self.image = threshold
            return img
        elif self.key == 'contour_red_delete_small_area':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            threshold = cv2.inRange(hsv, lower, upper)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = image
            for contour in contours:
                area = cv2.contourArea(contour) 
                if area > 2000:
                    img = cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)
            self.image = threshold
            return img
        elif self.key == 'contour_red_arclength':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            threshold = cv2.inRange(hsv, lower, upper)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = image
            for contour in contours:
                area = cv2.contourArea(contour) 
                if area > 2000:
                    length = round(cv2.arcLength(contour, True))
                    cv2.putText(img, 'L:' + str(length), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3, cv2.LINE_AA)
                    cv2.putText(img, 'S:' + str(round(area)), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3, cv2.LINE_AA)
                    img = cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)
            self.image = threshold
            return img
        elif self.key == 'contour_red_min_rect':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            threshold = cv2.inRange(hsv, lower, upper)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = image
            for contour in contours:
                area = cv2.contourArea(contour) 
                if area > 2000:
                    rect = cv2.minAreaRect(contour)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
            self.image = threshold
            return img
        elif self.key == 'contour_red_rect':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            threshold = cv2.inRange(hsv, lower, upper)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = image
            for contour in contours:
                area = cv2.contourArea(contour) 
                if area > 2000:
                    rect = cv2.minAreaRect(contour)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    min_x = min(box[:, 0])
                    max_x = max(box[:, 0])
                    min_y = min(box[:, 1])
                    max_y = max(box[:, 1])
                    box = np.array([[min_x, min_y],
                                    [max_x, min_y],
                                    [max_x, max_y],
                                    [min_x, max_y]])
                    cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
            self.image = threshold
            return img
        elif self.key == 'poly_detect':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            threshold = cv2.inRange(hsv, lower, upper)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = image
            for contour in contours:
                area = cv2.contourArea(contour) 
                if area > 2000:
                    epsilon = 0.04 * cv2.arcLength(contour, True)
                    approx = cv2.approxPolyDP(contour, epsilon, True)
                    corners = len(approx)
                    cv2.putText(img, str(corners) + ' corners', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3, cv2.LINE_AA)
            self.image = threshold
            return img
        elif self.key == 'rect_length_detect':
            hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            lower = (156, 84, 127)
            upper = (180, 255, 255)
            threshold = cv2.inRange(hsv, lower, upper)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            img = image
            
            max_cnt = None
            max_area = 0
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > 2000:
                    if area > max_area:
                        max_area = area
                        max_cnt = contour
                        
            if max_area > 0:
                rect = cv2.minAreaRect(max_cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                len1 = math.sqrt((box[0][0] - box[1][0]) ** 2 + (box[0][1] - box[1][1]) ** 2)
                len2 = math.sqrt((box[0][0] - box[3][0]) ** 2 + (box[0][1] - box[3][1]) ** 2)
                a = min(len1, len2)
                b = max(len1, len2)
                scale = 8.0 / a
                b *= scale
                cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
                cv2.putText(img, 'L:' + str(b), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3, cv2.LINE_AA)
                
            self.image = threshold
            return img
        return image


if __name__ == '__main__':
    OpenCVLearningTool().run()