import cv2
from ultralytics import YOLO
import torch
import os

"""
Este script contiene la clase Detector que se encarga de detectar objetos en un frame de video.
"""

class Detector:
    def __init__(self, model_path='models/COCO/yolov8s.pt', ball_classes=None, conf=0.5):
        # Verificar si hay GPU disponible
        if ball_classes is None:
            ball_classes = [32]
        if torch.cuda.is_available():
            print("GPU está disponible.")
            self.device = torch.device("cuda:0")
        else:
            print("GPU no está disponible, se utilizará la CPU.")
            self.device = torch.device("cpu")

        self.model = YOLO(model_path)
        self.ball_classes = ball_classes
        self.conf = conf

    def detect(self, frame):
        results = self.model.predict(frame, device=self.device, verbose=False, conf=self.conf)
        boxes = results[0].boxes  # Objeto Boxes para las salidas de bbox
        img_with_boxes = frame.copy()  # Crear una copia del frame para dibujar las cajas
        cls = None
        filtered_boxes = []
        centers = []

        for box in boxes:
            cls = int(box.cls[0])  # Obtener la clase del objeto detectado
            if cls in self.ball_classes:  # Verificar si la clase está en la lista de clases de pelotas
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Obtener las coordenadas de la caja
                conf = box.conf[0]  # Obtener la confianza de la detección
                label = f"Ball: {conf:.2f}"  # Crear la etiqueta de la caja

                # Dibujar la caja y la etiqueta en la imagen
                cv2.rectangle(img_with_boxes, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img_with_boxes, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # Calcular el centro del bbox
                x_center = (x1 + x2) / 2
                y_center = (y1 + y2) / 2
                centers.append((x_center, y_center))

                # Guardar las cajas filtradas
                filtered_boxes.append(box)

        if filtered_boxes:
            return img_with_boxes, filtered_boxes, centers
        return None, None, None
