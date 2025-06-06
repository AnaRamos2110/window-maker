#Criando uma checkbox para definir genêro
'''
import tkinter as tk #Renomeando o tkinter
from tkinter import * #Para selecionar o que quiser sem ficar chamando o tk toda hora...

master = Tk()
var1 = IntVar()
Checkbutton(master, text='Masculino', variable=var1).grid(row=0, sticky=W) #Definindo uma das opções da checkbox como valor da variável, e posicionamento com row e sticky.
var2 = IntVar()
Checkbutton(master, text='Feminino', variable=var2).grid(row=1, sticky=W)

mainloop()
'''

#Agora que escrevemos o exercicío vamos incrementar com mais opções. Sabemos que na maioria de preenchimento de formulários, além de masculino e feminino incluem também a opção de 'não-binário' ou a opção de 'prefiro não dizer'... Portando, iremos adicionar ao nosso menu e aprimorar o código com botões para apagar caso escolha a opção incorreta e o botão de entrada para confirmar escolha:

import tkinter as tk
from tkinter import *

#Vamos criar uma nova função para chamar nossos botões

def enviar():
    genero = var.get()
    if genero == 1:
        print('Selecionado: Feminino')
    elif genero == 2:
        print('Selecionado: Masculino')
    elif genero == 3:
        print('Selecionado: Não Binário')
    else:
        print('Nenhuma opção selecionada')

def apagar():
    var.set(0) #Reseta a seleção 

master = Tk()
master.title("Seleção de gênero")

var = IntVar() #Chamando as variáveis pré-definidas acima para prosseguir com a criação do menu

Radiobutton(master, text='Feminino', variable=var, value=1).grid(row=0, sticky=W)
Radiobutton(master, text='Masculino', variable=var, value=1).grid(row=1, sticky=W)
Radiobutton(master, text='Não Binário', variable=var, value=1).grid(row=2, sticky=W)
Radiobutton(master, text='Prefiro não informar.', variable=var, value=1).grid(row=3, sticky=W)

Button(master, text='Enviar', command=enviar).grid(row=4, column=0, pady=3)
#pady vem de "padding Y" —- espaçamento vertical. para ajudar os botõesnão ficarem grudados uns nos outros.
Button(master, text='Apagar', command=apagar).grid(row=4, column=1, pady=3)

mainloop()