import cv2
import pandas as pd

img_loc = "colorpic.jpg"
img = cv2.imread(img_loc,-1)
cv2.imshow("img", img)


cv2.waitKey(3000)

cv2.destroyAllWindows()