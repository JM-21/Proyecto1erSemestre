import tkinter as tk
from sesion import Sesion
import Oriente
from tkinter import *

class Abejorral(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Abejorral")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/abejorral.png")
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
                                 text=" Bienvenido a Abejorral", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 320, y=100)

        lbl_texto = tk.Label(self, 
                             text="Abejorral, es encantador, con diferentes pisos térmicos que permiten \n adentrarse en la diversidad de la producción agraria, es un lugar propicio para \n el senderismo donde se disfruta de su riqueza en fauna y flora, las montañas y los atardeceres \n hacen de este pueblo colonial, una fotografía desde cualquier ángulo.\nAbejorral es llamada “La Tierra de Los Cien Señores” debido a la \n caudalosa nómina de hombres y mujeres de gran importancia y protagonismo \n en el desarrollo del país."
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=180)

        lbl_titulo = tk.Label(self,
                                 text="Fiesta #1", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=360)

        lbl_texto = tk.Label(self, 
                             text="Semana del Café (10 al 13 Octubre)"
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=400)

        lbl_titulo = tk.Label(self,
                                 text="Fiesta #2", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=470)

        lbl_texto = tk.Label(self, 
                             text="Semana de la Palabra (28 al 30 Abril)"
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=510)

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
        Oriente.oriente(self.ventana_anterior)