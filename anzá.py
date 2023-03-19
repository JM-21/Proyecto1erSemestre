import tkinter as tk
from sesion import Sesion
import occidente
from tkinter import *

class Anzá(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Anzá")
        self.anchoVentana = 800
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/anzá.png")
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
                                 text=" Bienvenido a Anzá", fg="black", 
                                 bg="green", font=("Monotype Corsiva", 20))
        lbl_titulo.pack
        lbl_titulo.place(x= 320, y=100)

        lbl_texto = tk.Label(self, 
                             text="Anzá el mirador del Río Cauca, es un Pueblo antioqueño tradicional, \n de buenas costumbres y personas honradas, donde todo el mundo te saluda, \n rodeado de exuberante naturaleza en pleno bosque seco tropical, rico en aguas limpias \n y cristalinas para tomar frescos baños, gracias a su agradable \n clima caliente; Municipio agrícola, ganadero, de minería tradicional y barequeo, \n aún vestido de historia indígena y colonial, con caminos riales y de herradura \n que nos harán viajar en el tiempo. Además fue y es, el epicentro histórico de la obra de \n costumbrismo mágico, llamado “Villa Maga” del maestro pintor, escritor, \n diseñador gráfico, compositor, músico y ahora muralista León Octavio Osorno Aguirre."
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
                             text="Fiestas del Cacique Curumé"
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
                             text="Fiestas de la Integración y del Café Corregimiento Güíntar"
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
        occidente.Occidente(self.ventana_anterior)