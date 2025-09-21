import cv2

# Kamera öffnen (0 = Standardkamera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera konnte nicht geöffnet werden!")
    exit()

# Frame einlesen
ret, frame = cap.read()
if not ret:
    print("Konnte kein Bild von der Kamera lesen!")
    cap.release()
    exit()

# Breite und Höhe auslesen
hoehe, breite = frame.shape[:2]  # Nur die ersten beiden Werte (Höhe, Breite)
print("Breite:", breite)
print("Höhe:", hoehe)

cap.release()


