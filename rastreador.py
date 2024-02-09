import math


class Rastreador:
    def __init__(self):
        self.centro_de_objetos = {}
        self.id = 1

    def rastrear(self, objetos):
        # Recibe una lista de objetos detectados
        objetos_id = []
        for rect in objetos:
            # obtenemos el punto central del objeto nuevo
            x, y, w, h = rect
            centro_x = (x + x + w) // 2
            centro_y = (y + y + h) // 2
            # revisamos si el objeto fue detectado
            detectado = False
            for id_, punto in self.centro_de_objetos.items():
                distancia = math.hypot(centro_x - punto[0], centro_y - punto[1])
                if distancia < 25:
                    self.centro_de_objetos[id_] = (centro_x, centro_y)
                    objetos_id.append([x, y, w, h, id_])
                    detectado = True
                    break
            # si no fue detectado, lo agregamos a la lista
            if not detectado:
                self.centro_de_objetos[self.id] = (centro_x, centro_y)
                objetos_id.append([x, y, w, h, self.id])
                self.id += 1
        # eliminamos los objetos que no fueron detectados
        new_centro_puntos = {}
        for obj in objetos_id:
            _, _, _, _, id_ = obj
            centro = self.centro_de_objetos[id_]
            new_centro_puntos[id_] = centro

        self.centro_de_objetos = new_centro_puntos.copy()
        return objetos_id
