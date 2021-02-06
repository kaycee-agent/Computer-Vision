import cv2

face_casade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#
while True:
    _, image = cap.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    #Draw Rectangles around faces
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0 , 0), 2)
    
    cv2.imshow('image', image)
    #Bresk loop
    stop = cv2.waitKey(30) &0xff
    if stop ==27:
        break


cap.release()
    
    