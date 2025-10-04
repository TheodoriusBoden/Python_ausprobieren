import os
import cv2

img_folder = "/img_dead_victim"
augmented_folder = "/augmented_dead_victim"
os.makedirs(augmented_folder, exist_ok=True)

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = ( ( (i / 255.0) ** invGamma ) * 255 for i in range(256) )
    table = [min(255, max(0, int(v))) for v in table]
    table = bytearray(table)
    return cv2.LUT(image, table)

for img_name in os.listdir(img_folder):
    if img_name.endswith((".jpg", ".png")):
        img_path = os.path.join(img_folder, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Horizontal flip
        flipped = cv2.flip(img, 1)
        flip_name = os.path.splitext(img_name)[0] + "_flip.jpg"
        cv2.imwrite(os.path.join(augmented_folder, flip_name), flipped)

        # Brightness adjustment via gamma correction
        bright = adjust_gamma(img, gamma=1.5)
        bright_name = os.path.splitext(img_name)[0] + "_bright.jpg"
        cv2.imwrite(os.path.join(augmented_folder, bright_name), bright)