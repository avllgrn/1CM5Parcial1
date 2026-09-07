from subprocess import run
import tkinter

if __name__== '__main__':
    run('cls', shell='True')

    # Se construyen ventana
    Ventana = tkinter.Tk()
    Ventana.title('Mi ventana')

    # Se construye elemento
    CajaDeTexto = tkinter.Entry()
    # Se empaqueta elemento
    CajaDeTexto.pack()

    # Se construye elemento
    Etiqueta = tkinter.Label(text='Etiqueta')
    # Se empaqueta elemento
    Etiqueta.pack()

    # Se construye elemento
    Boton = tkinter.Button(text='Presiona Botón')
    # Se empaqueta elemento
    Boton.pack()

    # Se muestra la vantana
    Ventana.mainloop()
