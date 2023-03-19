import tkinter as tk
from sesion import Sesion
import bajo_cauca
from tkinter import *

class Caucacia(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Caucacia")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/caucacia.png")
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
                                 text=" Bienvenido a Caucacia", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 320, y=100)

        lbl_texto = tk.Label(self, 
                             text="Caucasia es una ciudad intermedia, reconocida por muchos como \nla capital del Bajo Cauca antioqueño. Es un territorio caluroso, rico \nen ganadería y pesca, gracias a sus ciénagas y corrientes de agua;\n por su margen occidental pasa el río Cauca."
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=150)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas de la Corraleja (Diciembre - Enero)", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=270)

        lbl_texto = tk.Label(self, 
                             text="Donde se aprecia el manteo a los toros criollos y de media \ncasta. Estas festividades nacen de los quehaceres rurales cotidianos,\nque fueron llevados a las plazas de los pueblos para \nconvertirlos en espectáculo público. "
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=300)

        lbl_titulo = tk.Label(self,
                                 text="Feria Agropecuaria (diciembre).", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=390)
        """
        lbl_texto = tk.Label(self, 
                             text="Es la fiesta tradicional más importante del municipio de \nSan Pedro de los Milagros. El nombre de las fiestas se dio como reconocimiento \nal producto más representativo de la región; la leche y sus derivados."
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=405)
        """
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
        bajo_cauca.BajoCauca(self.ventana_anterior)

