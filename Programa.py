from subprocess import run
import turtle

if __name__== '__main__':
    run('cls', shell='True')

    # Se construyen los objetos
    Ventana = turtle.Screen()
    Tortuga = turtle.Turtle()

    # Se usa un objeto Turtle para dibujar
    Tortuga.color('red')
    Tortuga.forward(100)
    Tortuga.left(90)

    Tortuga.color('green')
    Tortuga.forward(100)
    Tortuga.left(90)

    Tortuga.color('blue')
    Tortuga.forward(100)
    Tortuga.left(90)

    Tortuga.color('purple')
    Tortuga.forward(100)
    Tortuga.left(90)

    Ventana.exitonclick()
