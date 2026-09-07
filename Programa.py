from subprocess import run
import tkinter

if __name__== '__main__':
    run('cls', shell='True')

    # Se construyen ventana
    Ventana = tkinter.Tk()
    Ventana.title('Mi ventana')

    # Se construye elementos
    Etiqueta1 = tkinter.Label(text='A')
    Caja1 = tkinter.Entry()
    # Se agregan elementos
    Etiqueta1.grid(row=0, column=0)
    Caja1.grid(row=0, column=1)

    # Se construye elementos
    Etiqueta2 = tkinter.Label(text='B')
    Caja2 = tkinter.Entry()
    # Se agregan elementos
    Etiqueta2.grid(row=1, column=0)
    Caja2.grid(row=1, column=1)

    # Se construye elementos
    Etiqueta3 = tkinter.Label(text='C')
    Caja3 = tkinter.Entry()
    # Se agregan elementos
    Etiqueta3.grid(row=2, column=0)
    Caja3.grid(row=2, column=1)

    # Se construye elementos
    Boton1 = tkinter.Button(text='Suma')
    Boton2 = tkinter.Button(text='Limpia')
    # Se agregan elementos
    Boton1.grid(row=3, column=0)
    Boton2.grid(row=3, column=1, sticky='nsew')


    # Se muestra la vantana
    Ventana.mainloop()
