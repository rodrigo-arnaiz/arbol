import re
# from turtle import forward
import turtle
import click
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
t=turtle.Turtle()
t.left(90)
turtle.screensize(30000, 30000)
turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()
#t = turtle.Pen()
posicion=[]
angulo=[]
turtle.speed(10)
iteraciones = 10
tamanio_hoja=10/iteraciones
tamanio_tronco=5/iteraciones
angle=45

def giro_izq(angle):
    posicion.append(t.pos())
    angulo.append(t.heading())
    t.left(angle)

def giro_der(angle):
    posicion_guardada=posicion.pop()
    angulo_guardado=angulo.pop()
    t.up()
    t.goto(posicion_guardada,y=None)
    t.seth(angulo_guardado)
    t.down()
    t.right(angle)

def dibujar_hoja(tamanio_hoja):
    t.color('green')
    t.pensize(4)
    t.forward(tamanio_hoja)

def dibujar_tronco(tamanio_tronco):
    t.color('brown')
    t.pensize(4)
    t.forward(tamanio_tronco)

funciones = {'0':  lambda tamanio_hoja,tamanio_tronco,angle: dibujar_hoja(tamanio_hoja),
             '1':  lambda tamanio_hoja,tamanio_tronco,angle: dibujar_tronco(tamanio_tronco),
             '[':  lambda tamanio_hoja,tamanio_tronco,angle: giro_izq(angle),
             ']':  lambda tamanio_hoja,tamanio_tronco,angle: giro_der(angle),
            }

cadena = '0'

for i in range(iteraciones):
    cadena=cadena.replace('1','11')
    cadena=cadena.replace('0','1[0]0')
    

# for i in range(iteraciones):  
#     print('#'*20)
#     print(cadena)
#     resultado=''
#     for caracter in cadena:
#         if(caracter == '1'):
#             resultado+='11'
#         if(caracter == '0'):
#             resultado+='1[0]0'
#         if(caracter == '[' or caracter == ']'):
#             resultado+=caracter
    
#     cadena=resultado

for caracter in cadena:
    funciones[caracter](tamanio_hoja,tamanio_tronco,angle)

# for caracter in cadena:
#     if (caracter == '0'):
#         t.color('green')
#         t.pensize(4)
#         t.forward(hoja)
#     if (caracter == '1'):
#         t.color('brown')
#         t.pensize(4)
#         t.forward(tronco)
#     if (caracter == '['):
#         posicion.append(t.pos())
#         angulo.append(t.heading())
#         #angulo.append(t.towards(t.xcor(),t.ycor()))
#         t.left(45)
#     if (caracter == ']'):
#         posicion_guardada=posicion.pop()
#         angulo_guardado=angulo.pop()
#         t.up()
#         t.goto(posicion_guardada,y=None)
#         t.seth(angulo_guardado)
#         t.down()
#         t.right(45)

pausa = input()


