import cv2

# Leer imagen
img = cv2.imread("butterfly.jpg")

# Mostrar imagen a color
cv2.imshow("Mostrar imagen",img)

# Convertir imágenes a color en escala de grises
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Mostrar imagen en escala de grises
cv2.imshow("Escala de grises", gray_img)

#print(img) #imagen 3D a colores tiene tres '[' al inicio y tres ']' al final
print(gray_img) #imagen 2D escala grises tiene dos '[' al inicio y dos ']' al final

#cv2.waitKey(0) # Tiempo infinito: 0 milisegundos
cv2.waitKey(1000) # Tiempo definido: mayor a 0 milisegundos (1seg = 1000 milisegundos)
