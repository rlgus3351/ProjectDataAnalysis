import cv2


image_path = 'F:/reusable-trash-images/selectstar-reusable-trash-image/3403540.jpg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

cv2.circle(image, (926,1682), 25, (0,0,0),3)
cv2.circle(image, (1247,2283), 25, (0,0,255),3)
cv2.imwrite('test.png',image)
