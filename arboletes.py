import tkinter as tk
from sesion import Sesion
import uraba
from tkinter import *

class Arboletes(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Arboletes")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/arboletes.png")
        self.fondo1 = tk.Label(self,
                               bg='gray',
                               image=self.fondo)
        self.fondo1.place(  x=0,
                            y=30,
                            relwidth=1,
                            relheight=1)

        self.cabecera = tk.Label(self,
                                     text="Usuario conectado: "+Sesion.usuario,
                                     bg='green',
                                     fg='black',
                                     font=("Monotype Corsiva ", 10, "bold")
                                     )
        self.cabecera.place(x=550,y=5)

        lbl_titulo = tk.Label(self,
                                 text=" Bienvenido a Arboletes", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 320, y=100)

        lbl_texto = tk.Label(self, 
                             text="Arboletes es uno de los municipios jóvenes del departamento de\n Antioquia y su origen se remonta a una disputa de territorios con el \nvecino departamento de Córdoba, que terminó hacia 1920; aunque\n inicialmente fue un corregimiento ubicado entre los \nmunicipio de Turbo (Antioquia) y Montería."
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=150)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas del Mar y del Volcan", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=270)

        lbl_texto = tk.Label(self, 
                             text="En el mes de Junio es una tradicion en el pueblo, se hacen \nvarios eventos de deportes, fiestas y culturales. "
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=300)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas en Corraleja", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=375)

        lbl_texto = tk.Label(self, 
                             text="Se celebran las corridas de toros"
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=405)

        # Botones
        self.botonVolver = tk.Button(self,
                                      text="Volver",
                                      cursor="hand2",
                                      command=self.volver,
                                      bg='green',
                                      foreground='#000000',
                                      relief="flat",
                                      font=("Monotype Corsiva", 15, "bold"))
        self.botonVolver.place(x=80, y=15)

        

        self.botonDudas = tk.Button(self,
                                    text="?",
                                    cursor="hand2",
                                    width=3,
                                    height=1,
                                    bg='green',
                                    foreground='#000000',
                                    relief="flat",
                                    font=("Monotype Corsiva ", 15, "bold"))
        self.botonDudas.place(x=30, y=10)

 

    def volver(self):
        self.destroy()
        uraba.Uraba(self.ventana_anterior)