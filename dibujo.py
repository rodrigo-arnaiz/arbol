import turtle, click
import pandas as pd


"""Args linea de comandos"""
@click.command()
@click.option('--i', default=1, prompt='Iteraciones',help='Numero de iteraciones.')
@click.option('--v', default=0, help='Velocidad.')
@click.option('--d', default=0, help='Retraso.')
def main_(i,v,d):
    """inicio del programa"""
    click.echo(f"inicio del programa!")
    main(i,v,d)

"""Pandas"""
def leer_libro(path): #Lee el archivo
    return pd.read_excel(path)

def hoja(libro): 
    return round(libro["hoja"].values[0])

def tronco(libro): 
    return round(libro["tronco"].values[0])

def velocidad(libro):
    return libro["velocidad"].values[0]

def apilar(libro): 
    return libro["apilar"].values[0]

def desapilar(libro): 
    return libro["desapilar"].values[0]
"""Pandas"""

"""
Configuracion de turtle
"""
def config_turtle(v,d):
    turtle.screensize(30000, 30000)
    turtle.speed(v)
    turtle.delay(d)
    turtle.hideturtle()

"""
Crea una cadena a partir de la produccion de la gramatica dada
"""
def construir_cadena(hoja,tronco, iteraciones, libro):
    cadena = "0"
    # prod1=str(libro['produccion'].values[0])
    # prod2=str(libro['produccion'].values[1])
    # print(f'prod 1 {prod1} , prod 2 {prod2}')
    for i in range(iteraciones):
            cadena = cadena.replace(tronco, str(libro['produccion'].values[0]))
            cadena = cadena.replace(hoja, str(libro['produccion'].values[1]))
    return cadena

"""
Funcion principal
"""
def main(iteraciones, velocidad, delay):

    """
    No terminales: 0,1
    Terminales: [,]
    Cadena inicial: 0
    Reglas de produccion: (1 -> 11), (0 -> 1[0]0)
    Interpretacion:
    0: Dibujar un segmento de linea hoja.
    1: Dibujar un segmento de linea.
    [: Apilar (guardar) posicion y angulo actual, luego girar 45° a la izquierda.
    ]: Desapilar (restaurar) posicion y angulo guardados, luego girar 45° a la derecha.
    """

    libro = leer_libro("./prueba.xlsx")
    
    print(f'Lectura de datos del libro excel:\n{libro}')
    
    tortuga=turtle.Turtle()

    config_turtle(velocidad, delay)

    posicion=[]
    angulo=[]
    tortuga.left(90)
    tamanio_hoja=30/iteraciones
    tamanio_tronco=25/iteraciones
    angle=45

    def giro_izq(angle):
        posicion.append(tortuga.pos())
        angulo.append(tortuga.heading())
        tortuga.left(angle)

    def giro_der(angle):
        posicion_guardada=posicion.pop()
        angulo_guardado=angulo.pop()
        tortuga.up()
        tortuga.goto(posicion_guardada,y=None)
        tortuga.seth(angulo_guardado)
        tortuga.down()
        tortuga.right(angle)

    def dibujar_hoja(tamanio_hoja):
        tortuga.color('green')
        tortuga.pensize(4)
        tortuga.forward(tamanio_hoja)

    def dibujar_tronco(tamanio_tronco):
        tortuga.color('brown')
        tortuga.pensize(4)
        tortuga.forward(tamanio_tronco)

    funciones = {str(hoja(libro)):  lambda tamanio_hoja,tamanio_tronco,angle: dibujar_hoja(tamanio_hoja),
                str(tronco(libro)):  lambda tamanio_hoja,tamanio_tronco,angle: dibujar_tronco(tamanio_tronco),
                apilar(libro) :  lambda tamanio_hoja,tamanio_tronco,angle: giro_izq(angle),
                desapilar(libro) :  lambda tamanio_hoja,tamanio_tronco,angle: giro_der(angle),
                }

    h = str(hoja(libro))
    t = str(tronco(libro))
 

    cadena = construir_cadena(h, t, iteraciones, libro)

    print(f'Cadena producida:\n{cadena}\ncon {iteraciones} iteraciones')

    for caracter in cadena:
        funciones[caracter](tamanio_hoja,tamanio_tronco,angle)

    turtle.done()
    turtle.exitonclick()


if __name__ == "__main__":
    main_()