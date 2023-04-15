import cv2
import easyocr 

#dentro de los corchetes va o van los idiomas que usaremos para leer
reader = easyocr.Reader(["es"], gpu = False)

image= cv2.imread("imagen001.jpg")

#con readtext nos regresa lo que escribimos y al ponerle detail = 0 nos regresa solo los textos reconocidos
#si usamos paragraph = True nos arroja un parrafo 
#result = reader.readtext(image, detail=0)
#result

#mostrar la imagen 
cv2.imshow("Image", image)
cv2.waitKey(0)

#destruimos las ventanas creadas durante la ejecución del script
cv2.destroyAllWindows()
