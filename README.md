# Control de Tráfico Inteligente (CTI)

Proyecto modular.

Controlador de tráfico inteligente, capaz de controlar los semáforos de una intersección para mejorar el flujo de autos. Se utiliza visión computacional para la detección de vehículos y tomar decisiones en base a ellos.

### Integrantes:

- Joanine Córdova Vázquez
- Luis Iván Rico Amezcua
- Eduardo Daniel Urbina Campos

## Requerimientos

__Nota__: se utiliza Python 3.10

Requerimientos:

- fastapi 0.110.0
- Jinja2 3.1.4
- opencv-python 4.10.0.84
- ultralytics 8.2.78
- uvicorn 0.27.1

Comando para su instalación utilizando [requirements.txt](https://github.com/00urbina00/STA/blob/main/requirements/requirements.txt):

    pip3 install -r requirements.txt

Comando para correr Uvicorn de forma local:

    uvicorn main:app --reload

