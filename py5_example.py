import py5

def setup():
    py5.size(500, 500)  # Establece el tamaño de la ventana (500x500 píxeles)

def draw():
    py5.background(200)  # Establece el fondo de la ventana en un color gris (valor 200)
    py5.ellipse(py5.mouse_x, py5.mouse_y, 50, 50)  # Dibuja un círculo donde está el ratón

py5.run_sketch()  # Inicia el ciclo de animación de py5
