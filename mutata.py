import tkinter as tk
from sesion import Sesion
import uraba
from tkinter import *

class Mutata(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Mutata")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/mutata.png")
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
                                 text=" Bienvenido a Mutata", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 320, y=100)

        lbl_texto = tk.Label(self, 
                             text="Mutatá (La Puerta Oro de Urabá) es considerado un rincón mágico \nque lleva consigo una carga de histórica de valor sin igual, \npuesto que su gran diversidad de fauna, flora y multiculturalidad lo catalogan \ncomo el municipio donde las montañas y el verdor de la \nnaturaleza se funden en un río."
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=150)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas del Río", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=270)

        lbl_texto = tk.Label(self, 
                             text="En el mes de Junio y Julio se celebra en el pueblo las fiestas \ndel Rio y todos los habitantes del municipio como turistas van\n a disfrutar en el Rio de las fiestas y las calurosas tardes que hacen de estas \nfiestas un excelente destino para disfrutar. "
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=300)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas del Campesino", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=375)

        lbl_texto = tk.Label(self, 
                             text="Se celebran en Julio, en este evento patrimonial los campesinos \naprovechan para sacar a la venta toda su produccion. \ncomo manualidades, mercados y prendas, \nhechas por ellos mismos."
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