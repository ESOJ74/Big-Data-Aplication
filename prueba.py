import cv2

# Leer la imagen de entrada
img = cv2.imread('gato2.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar el algoritmo Canny
edges = cv2.Canny(gray, 100, 200)

# Superponer la imagen de bordes en la imagen original en color
output = cv2.bitwise_and(img, img, mask=edges)

# Mostrar la imagen resultante
cv2.imshow('Bordes', output)
cv2.waitKey(0)
cv2.destroyAllWindows()