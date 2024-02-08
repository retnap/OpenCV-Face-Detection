import cv2 

img = cv2.imread("C:\\Users\\Selman\\Desktop\\Tasarim-1\\HaarCascade_dosyalar\\test_images\\face.png")

face_cascade = cv2.CascadeClassifier("C:\\Users\\Selman\\Desktop\\Tasarim-1\\HaarCascade_dosyalar\\haarCascade\\frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# It will give the coordinates of the faces on the image 
faces = face_cascade.detectMultiScale(gray, 1.3, 7) #Using the detectMultiScaele function with the face_cascade file, it will find faces from the gray tone image.
# If there is an error and faces are found elsewhere, we can increase the value to 7.

# Drawing a rectangle on the face, x y w h -> x and y coordinates, width and height
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h),(0,0,255), 2)
        #x,y upper left coordinates
        #x+w, y+h go to lower right coordinate
        #color and thickness

cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
