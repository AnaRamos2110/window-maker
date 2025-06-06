'''
import tkinter as Tk
from tkinter import *
master = Tk()
Label(master, text='Nome: ').grid(row=0)
Label(master, text='Sobrenome').grid(row=1)
entrada1 = Entry(master)
entrada2 = Entry(master)
entrada1.grid(row=0, column=1)
entrada2.grid(row=1, column=1)



mainloop()
'''

#Melhorando  o exercicío utilizando classe

import tkinter as Tk #Chamando a biblioteca e renomeando
from tkinter import * #Usando o import * para chamar tudo da biblioteca sem declarar o nome dela toda vez que for usar uma função.

class FormularioSimples:
    def __init__(self, master): #Criando uma classe e atribuindo a função mestre dentro do parâmetro
        self.master = master
        master.title('Formulário Simples') #Título da tela

        Label(master, text='Nome: ').grid(row=0) #Criando os botões e posicionando na 'grade' da tela
        Label(master, text='Sobrenome: ').grid(row=1)

        self.entrada1 = Entry(master)
        self.entrada2 = Entry(master)
        self.entrada1.grid(row=0, column=1)
        self.entrada2.grid(row=1, column=1)

        Button(master, text="Enviar", command=self.enviar).grid(row=2, column=0, pady=10)
        Button(master, text="Apagar", command=self.apagar).grid(row=2, column=1, pady=10)
        Button(master, text="Sair", command=self.sair).grid(row=2, column=2, pady=10)
    
    def enviar(self):
        nome = self.entrada1.get()
        sobrenome = self.entrada2.get()
        print(f"Nome completo: {nome} {sobrenome}")
        self.entrada1.delete(0, END)
        self.entrada2.delete(0, END)

    def apagar(self):
        self.entrada1.delete(0, END)
        self.entrada2.delete(0, END)

    def sair(self):
        self.master.destroy()


#Chamando a classe para rodar a aplicação
if __name__ == "__main__":
    root = Tk()
    app = FormularioSimples(root)
    root.mainloop()