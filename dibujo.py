import turtle, click
import pandas as pd


"""Args linea de comandos"""
@click.command()
@click.option('--i', default=1, prompt='Iteraciones',help='Numero de iteraciones.')
@click.option('--v', default=0, prompt='Velocidad',help='Velocidad.')
def main_(i,v):
    """inicio del programa"""
    click.echo(f"inicio del programa!")
    main(i,v)

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


"""Configuracion de turtle"""
def config_turtle(tortuga,v):
    tortuga.left(90)
    turtle.screensize(30000, 30000)
    turtle.speed(v)
    turtle.delay(v)
    turtle.hideturtle()

def construir_cadena(hoja,tronco, iteraciones, libro):#crea un diccionario de diccionarios para recorrer el automata
    cadena = "0"
    prod1=str(libro['produccion'].values[0])
    prod2=str(libro['produccion'].values[1])
    print(f'prod 1 {prod1} , prod 2 {prod2}')
    for i in range(iteraciones):
            cadena = cadena.replace(tronco, str(libro['produccion'].values[0]))
            cadena = cadena.replace(hoja, str(libro['produccion'].values[1]))
    return cadena

"""Funcion principal"""
def main(iteraciones, velocidad):

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
    print(libro)
    
    tortuga=turtle.Turtle()

    config_turtle(tortuga, velocidad)

    posicion=[]
    angulo=[]
    turtle.speed(10)
    tamanio_hoja=10/iteraciones
    tamanio_tronco=10/iteraciones
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

    # cadena = '0'
    h = str(hoja(libro))
    t = str(tronco(libro))
 

    cadena = construir_cadena(h, t, iteraciones, libro)

    print(cadena)

    for caracter in cadena:
        funciones[caracter](tamanio_hoja,tamanio_tronco,angle)

    turtle.done()
    pausa = input()


if __name__ == "__main__":
    main_()