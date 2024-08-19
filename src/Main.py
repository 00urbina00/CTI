import os
import sys

from detector.detector import Detector

model = 'best.pt'
# Clases de vehículos en COCO
classes = [32]
accurracy = 0.5

# Detector settings
model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models', 'COCO', model)
detector = Detector(model_path, ball_classes=classes, conf=accurracy)

"""
Este script es un ejemplo de cómo utilizar la clase Detector para detectar objetos en un video en tiempo real.
"""
model = 'pool_balls.pt'

script_dir = os.path.dirname(os.path.abspath(__file__))
detector = Detector(os.path.join(script_dir, 'models', 'COCO', model), ball_classes=[0, 1], conf=0.82)

try:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img_with_boxes, boxes, centers = detector.detect(frame)
        if img_with_boxes is not None:
            cv2.imshow('Frame', img_with_boxes)
            print("Detected", len(boxes), "balls")
        else:
            cv2.imshow('Frame', frame)

        k = cv2.waitKey(1)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

except ValueError as e:
    print(e)

except Exception as e:
    print("Ocurrió un error inesperado:", e)
