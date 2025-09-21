print("start")

import cv2

camera = cv2.VideoCapture(0)
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = camera.read()
    if not ret:
        print("No camera")
        break
    frame = cv2.flip(frame, 1)
    frame_h, frame_w = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        cropped_face = frame[max(y-round(h/3), 0) : min(y+h+round(h/3), frame_h),   max(x-round(w/1.5), 0) : min(x+w+round(w/1.5), frame_w)]
        face_zoom =cv2.resize(cropped_face, (frame_w, frame_h))
        cv2.imshow("Gesicht", face_zoom)
    else:
        cv2.imshow("Gesicht", frame)


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)

    cv2.imshow("Gesichtserkennung", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()