# coding=utf-8
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, numpy.ndarray)): 
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img) 
        fontStyle = ImageFont.truetype( "FreeSans.ttf", textSize, encoding="utf-8") 
        draw.text((left, top), text, textColor, font=fontStyle)
        return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

if __name__ == '__main__':
    src = cv2.imread('img1.jpg')
    cv2.imshow('src',src)
    cv2.waitKey(0)
    
    img = cv2ImgAddText(src, "Python programmers taking a walk", 10, 35, (255, 255 , 255), 20)
    cv2.imshow('show', img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        
