import cv2
from rastreador import *

seguimiento = Rastreador()
nombre_archivo = "video5.mp4"
cap = cv2.VideoCapture(nombre_archivo)

deteccion = cv2.createBackgroundSubtractorMOG2(history=10000, varThreshold=500)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    # Video 1
    # zona = frame[150: 500, 460: 890]
    # Video 2
    zona = frame[235: 560, 330: 900]

    mascara = deteccion.apply(zona)
    _, mascara = cv2.threshold(mascara, 254, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    objetos = []    # lista de objetos detectados
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 400:
            x, y, w, h = cv2.boundingRect(c)
            objetos.append([x, y, w, h])

    objetos = seguimiento.rastrear(objetos)
    for obj in objetos:
        x, y, w, h, id_ = obj
        cv2.putText(zona, str(id_), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255, 255), 2)
        cv2.rectangle(zona, (x, y), (x + w, y + h), (255, 255, 0), 3)

    print(objetos)
    cv2.imshow("Zona de interes", zona)
    cv2.imshow("Mascara", mascara)
    cv2.imshow("Calle", frame)

    key = cv2.waitKey(5)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
