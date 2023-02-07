import numpy as np
import cv2

# Crear una imagen en negro
black = np.zeros([600,600])

#f_row = black[1:2]
#print(f_row)

#f_col = black[:,1:2]
#print(f_col)

black[200:400,200:400] = 255
print(black)

cv2.imshow("En negro",black)
cv2.waitKey(0)


