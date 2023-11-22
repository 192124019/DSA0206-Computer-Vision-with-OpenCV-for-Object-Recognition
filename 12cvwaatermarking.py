import cv2

img = cv2.imread(r"C:\Users\USER\Downloads\cvimages.jpg")

watermark = cv2.imread(r"C:\Users\USER\Downloads\images.jpg")

watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))

blended = cv2.addWeighted(watermark, 0.5, img, 0.5, 0)

cv2.imwrite('blended.jpg', blended)
cv2.imshow('Blended Image', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
