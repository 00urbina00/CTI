from ultralytics import YOLO
import torch
import os
import cv2

"""
Este script es la implementación de entrenamiento de un modelo YOLOv8
"""

if torch.cuda.is_available():
    print("GPU está disponible.")
    Device = torch.device("cuda:0")
else:
    print("GPU no está disponible, se utilizará la CPU.")
    Device = torch.device("cpu")

script_dir = os.path.dirname(os.path.abspath(__file__))

yaml_path = os.path.join(script_dir, 'models', 'datasets', 'data.yaml')

model_path = os.path.join(script_dir, 'models', 'COCO', 'yolov8m.pt')

output_path = os.path.join(script_dir, 'models', 'COCO', 'output')

def get_max_stride(size, stride=32):
    h, w = size
    h = (h // stride) * stride  # Ajusta la altura al múltiplo de 32 más cercano
    w = (w // stride) * stride  # Ajusta el ancho al múltiplo de 32 más cercano
    return (w, h)

def main():
    original_img_size = (350, 193)

    ImgSize = get_max_stride(original_img_size)

    if not os.path.exists(model_path):
        print("El modelo pre-entrenado no existe.")
        return
    
    # Cargar el modelo pre-entrenado
    model = YOLO(model_path)

    # Entrenar el modelo
    model.train(data=yaml_path, project=output_path, epochs=50, imgsz=ImgSize, batch=50, device=Device)

if __name__ == '__main__':
    main()
