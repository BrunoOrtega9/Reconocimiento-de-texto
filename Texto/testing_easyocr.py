import cv2
import easyocr 

reader = easyocr.Reader(["es"], gpu = False)

image= cv2.imread("testing001.jpeg")

cv2.imshow("Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()
