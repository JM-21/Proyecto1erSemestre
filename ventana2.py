import tkinter as tk
from sesion import Sesion
import ventana1
from tkinter import messagebox

class Ventana2(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Antioquia es fiesta")
        self.anchoVentana = 1000
        self.altoVentana = 600

        self.puntoDerecha = int(self.winfo_screenwidth()/2 - self.anchoVentana/2)
        self.puntoArriba = int(self.winfo_screenheight()/2 - self.altoVentana/2)

        self.geometry("{}x{}+{}+{}".format(self.anchoVentana,self.altoVentana,self.puntoDerecha,self.puntoArriba))
        self.resizable(width=True, height=True)
        self.configure(bg='#ffffff')
        self.iconbitmap("images/icon.ico")
        self.fondo = tk.PhotoImage(file="images/fondologin.png")
        self.fondo1 = tk.Label(self,
                               bg='#ffffff',
                               image=self.fondo)
        self.fondo1.place(  x=0,
                            y=30,
                            relwidth=1,
                            relheight=1)

        self.cabecera = tk.Label(self,
                                     text="Usuario conectado: "+Sesion.usuario,
                                     bg='green',
                                     fg='black',
                                     font=("Monotype Corsiva ", 12, "bold")
                                     )
        self.cabecera.place(x=650,y=5)

        # Botones
        self.botonVolver = tk.Button(self,
                                      text="Volver",
                                      cursor="hand2",
                                      command=self.volver,
                                      bg='green',
                                      foreground='black',
                                      relief="flat",
                                      font=("Monotype Corsiva ", 20, "bold"))
        self.botonVolver.place(x=100, y=70)

        

        self.botonDudas = tk.Button(self,
                                    text="?",
                                    cursor="hand2",
                                    width=3,
                                    height=1,
                                    bg='green',
                                    foreground='black',
                                    relief="flat",
                                    font=("Monotype Corsiva ", 15, "bold"))
        self.botonDudas.place(x=50, y=70)
        
        #Comentario
        self.Comentario = tk.StringVar()
       

        # Label Comentario
        self.labelComentario = tk.Label(self,
                                    text="Haznos saber qué piensas respecto a la app",
                                    bg="green",
                                    foreground="black",
                                    font=("Comc sans MS ", 13, "bold")
                                    )
        self.labelComentario.place(x=350, y=150)
        # entradas Comentario
        self.entradaComentario = tk.Entry(self, highlightthickness=2,
                                      textvariable=self.Comentario,
                                      relief="flat",
                                      bg="#F5F5F5",
                                      font=("Comc sans MS ", 12, "bold"))
        self.entradaComentario.place(width=300, height=100)                              
        self.entradaComentario.place(x=370, y=200)
        
        self.botonEnviar = tk.Button(self,
                                    text="Enviar",
                                    cursor="hand2",
                                    command=self.enviar,
                                    width=5,
                                    height=1,
                                    bg='green',
                                    foreground='black',
                                    relief="flat",
                                    font=("Monotype Corsiva ", 12, "bold"))
        self.botonEnviar.place(x=465, y=350)


    def volver(self):
        self.destroy()
        ventana1.Ventana1(self.ventana_anterior)

    def enviar(self):
        try:
            with open("datos/usuarios/comentarios.txt", 'r') as f: # Leyendo a todos los comentarios
                filas = f.readlines()  # crea una lista de comentarios

                comentarios = []  #creamos una lista vacia de comentarios



                for fila in filas:
                    comentarios = fila.split(";")
                    comentarios.append(comentarios)
                f.close()
        
        except Exception as ex: 
                print()
   
        messagebox.showinfo(message="Su comentario se ha enviado, Muchas gracias")
        self.entradaComentario.delete(0, tk.END)