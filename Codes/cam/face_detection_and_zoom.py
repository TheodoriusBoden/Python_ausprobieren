print("start")

import cv2

camera = cv2.VideoCapture("/dev/video1")
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

last_faces = (0, 0, 250, 350)

cropp_factor_w = 0.7
cropp_factor_h = 0.5

output_window_w = 650
output_window_h = round(output_window_w * 0.75)
print(output_window_h)
print(output_window_w)

while True:
    ret, frame = camera.read()
    if not ret:
        print("No camera")
        break
    #frame = cv2.flip(frame, 1)
    frame_h, frame_w = frame.shape[:2]
    frame_ratio_hw = frame_h / frame_w

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        last_faces = (x, y, w, h)
        cropped_face = frame[max(y-round(h*cropp_factor_h), 0) : min(y+h+round(h*cropp_factor_h), frame_h),   max(x-round(w*cropp_factor_w), 0) : min(x+w+round(w*cropp_factor_w), frame_w)]
        print("face detected and cropped")
    else:
        print("no face detected")
        cropped_face = frame[max(last_faces[1]-round(last_faces[3]*cropp_factor_h), 0) : min(last_faces[1]+last_faces[3]+round(last_faces[3]*cropp_factor_h), frame_h),   max(last_faces[0]-round(last_faces[2]*cropp_factor_w), 0) : min(last_faces[0]+last_faces[2]+round(last_faces[2]*cropp_factor_w), frame_w)]
        print(last_faces)
        print("cropped last_face")
    face_zoom =cv2.resize(cropped_face, (output_window_w, output_window_h))
    print("resized cropped_face")
    cv2.imshow("Gesicht", face_zoom)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    live_capture = cv2.resize(frame, (output_window_w, round(output_window_w * frame_ratio_hw)))
    cv2.imshow("Live capture", live_capture)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()