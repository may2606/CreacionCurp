# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 02:15:04 2023

@author: WIN 10
"""

#Elaborado por Mayra Galvez Rodriguez
#Triangulo
from tkinter import *
from tkinter import messagebox
import math

class App():
    def __init__(self):
        ventana = Tk()
        ventana.title("Calculadora de Triángulos")
        ventana.geometry("300x200")
        ventana.configure(bg='pink')

        # Widgets
        self.label1 = Label(ventana, text="Base (en cm)")
        self.label1.place(x=40, y=30)

        self.text1 = Entry(ventana, bg='blue')
        self.text1.place(x=150, y=30)

        self.label2 = Label(ventana, text="Altura (en cm)")
        self.label2.place(x=40, y=70)

        self.text2 = Entry(ventana, bg='blue')
        self.text2.place(x=150, y=70)

        self.resultado_label = Label(ventana, text="", font=("Arial", 12))
        self.resultado_label.place(x=80, y=120)

        # Botones
        self.bt_aceptar = Button(ventana, text="Aceptar", command=self.calcular)
        self.bt_aceptar.place(x=40, y=170)

        self.bt_limpiar = Button(ventana, text="Limpiar", command=self.limpiar)
        self.bt_limpiar.place(x=180, y=170)

        ventana.mainloop()

    def calcular(self):
        base = self.text1.get()
        altura = self.text2.get()

        if base == "" or altura == "":
            messagebox.showerror("Error", "Por favor, ingresa valores en ambos campos.")
            return

        try:
            ladob = float(base)
            ladoaltura = float(altura)

            # Calcular el área del triángulo
            area = ((ladob * ladoaltura) / 2) / 100

            # Calcular el perímetro del triángulo
            h = math.sqrt(ladob**2 + ladoaltura**2)
            perimetro = (ladob + ladoaltura + h) / 100

            resultado = f"Área: {area:.2f} metros cuadrados\nPerímetro: {perimetro:.2f} metros"
            self.resultado_label.config(text=resultado)

        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos en la base y la altura")

    def limpiar(self):
        self.text1.delete(0, END)
        self.text2.delete(0, END)
        self.resultado_label.config(text="")


Objeto_ventana = App()
