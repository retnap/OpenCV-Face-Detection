import cv2 

vid = cv2.VideoCapture("C:\\Users\\Selman\\Desktop\\Tasarim-1\\HaarCascade_dosyalar\\test_videos\\faces.mp4")

face_cascade = cv2.CascadeClassifier("C:\\Users\\Selman\\Desktop\\Tasarim-1\\HaarCascade_dosyalar\\haarCascade\\frontalface.xml")

while 1:
    ret, frame = vid.read()
    #vid.read() returns us two values, one is frame and the other is rejection
    #If it read the frames correctly, reject is true, if it is read incorrectly, reject is false.

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Find the coordinates of the frames converted to grayscale and assign them to a variable
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)

    #Draw a rectangle for each frame
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0),2)
        #The reason we draw on the frame is that we find the coordinates more clearly on the gray.


        cv2.imshow("Image", frame)
        if cv2.waitKey(3) & 0xFF == ord('q'):
            break

vid.release()
cv2.destroyAllWindows()

