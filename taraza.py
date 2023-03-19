import tkinter as tk
from sesion import Sesion
import bajo_cauca
from tkinter import *

class Taraza(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Taraza")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/taraza.png")
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
                                 text=" Bienvenido a Taraza", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 320, y=100)

        lbl_texto = tk.Label(self, 
                             text="Tarazá es un municipio de Colombia, localizado en la subregión\n del Bajo Cauca del departamento de Antioquia. Limita por el norte \ncon el departamento de Córdoba y el municipio de Cáceres,\n por el este con el municipio de Cáceres, por el sur con los municipios \nde Valdivia e Ituango, y por el oeste con el departamento de Córdoba.\nSu cabecera está a 222 kilómetros de la ciudad de Medellín, capital de Antioquia"
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=150)

        lbl_titulo = tk.Label(self,
                                 text="Feria Ganadera y del campesino", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=280)

        lbl_texto = tk.Label(self, 
                             text="Del 9 al 11 de Junio se realizan unas actividades en homenaje \na la Ganadería y al Campesino de Tarazá"
                             , bg="white",
                             font=("Arial", 12)
                             )
        lbl_texto.place(x=190, y=310)

        lbl_titulo = tk.Label(self,
                                 text="Fiestas del río", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 14))
        lbl_titulo.pack
        lbl_titulo.place(x= 190, y=375)
        
        lbl_texto = tk.Label(self, 
                             text=" Del 5 al 8 de Enero se celebra el aniversario de vida municipal, \ncon reinado, festividades deportivas y culturales. Se convoca a \nartistas de talla nacional."
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
        bajo_cauca.BajoCauca(self.ventana_anterior)