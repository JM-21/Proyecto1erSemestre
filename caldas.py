import tkinter as tk
from sesion import Sesion
import valle_aburra
from tkinter import *

class Caldas(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Caldas")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/caldas.png")
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
                                 text=" Bienvenido a Caldas", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 320, y=100)

        lbl_texto = tk.Label(self, 
                             text="Es la puerta sur del Valle de Aburrá, custodiado por el Alto de \nSan Miguel, donde nace el río Medellín; el Alto \nde la Romera, que alcanza los 2.650 metros de altura; y el Alto del \nRomeral. Es la perfecta condensación entre el poblado rural \ncon el urbano, con parque amplio"
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=150)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas del Aguacero", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=270)

        lbl_texto = tk.Label(self, 
                             text="Caldas es un lugar bañado por agua, posee un seudónimo, (Cielo roto) \npor ello celebra la lluvia con las Fiestas \ndel Aguacero, que desde 1997."
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=300)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas Patronales de Nuestra Señora de las Mercedes", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=380)
        
        lbl_texto = tk.Label(self, 
                             text="El 24 de septiembre la Iglesia Universal celebra la fiesta de Nuestra \nSeñora de las Mercedes, patrona del Municipio de Caldas. \nLa Diócesis quiere rendir un homenaje a esta advocación tan \nquerida por la comunidad."
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=410)
        
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
        valle_aburra.Valle_aburra(self.ventana_anterior)