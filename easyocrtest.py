import cv2
import easyocr 

reader = easyocr.Reader(["es"], gpu = False)

image= cv2.imread("imagen001.jpg")

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
