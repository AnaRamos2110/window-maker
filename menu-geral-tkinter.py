#Para estes códigos, eu resolvi juntar os slides que continham várias partes, vou escreve-los separadamente e depois junta-los e fazer um menu só! 

#Janela 1
'''
from tkinter import *

#Cria a janela principal
top = Tk()

#Cria o Menubutton
mb = Menubutton(top, text='Menu principal')
mb.pack()  #pack() para exibir o Menubutton

#Cria o menu associado ao Menubutton
mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu

#Variáveis para os checkbuttons
cVar = IntVar()
aVar = IntVar()

#Adiciona opções ao menu
mb.menu.add_checkbutton(label='Contato', variable=cVar)
mb.menu.add_checkbutton(label='Sobre', variable=aVar)

# Inicia o loop principal da interface
top.mainloop()
'''

#Janela 2--
'''
import tkinter as tk
from tkinter import *

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Arquivo', menu=filemenu)
filemenu.add_command(label='Novo')
filemenu.add_command(label='Abrir...')
filemenu.add_separator() #Insere o separador de Menu--
filemenu.add_command(label='Sair', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Ajuda', menu=helpmenu)
helpmenu.add_command(label='Sobre: ')
mainloop()
'''

#Aprimorando os códigos: --Para obter melhorias, será feita a junção das duas janelas para ter o menu completo:

from tkinter import *

#Criando a janela principal com uma nova variável:
root = Tk()
root.title("Menu completo") #Renomeando o nome da janela

#Menu principal:
menu = Menu(root)
root.config(menu=menu)

#Menu de arquivos:
filemenu = Menu(menu, tearoff=0) #O  comando tearoff faz algum comando ser aberto em outra janela, por estar configurado como 0, faz o comando se manter na mesma janela.
menu.add_cascade(label='Arquivo', menu=filemenu)
filemenu.add_command(label='Novo')
filemenu.add_command(label='Abrir...')
filemenu.add_separator() #Separador de comandos
filemenu.add_command(label='Sair', command=root.quit) #Fecha a janela e sai da aplicação

#Menu de ajuda:
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Ajuda', menu=helpmenu)
helpmenu.add_command(label='Sobre:')

#Pra chamar os comandos como botões:
menubottonn = Menubutton(root, text='Menu principal', relief=RAISED)
menubottonn.pack(pady=20)

menubottonn.menu = Menu(menubottonn, tearoff=0)
menubottonn['menu'] = menubottonn.menu

cVar = IntVar()
aVar = IntVar()

menubottonn.menu.add_checkbutton(label='Contato', variable=cVar)
menubottonn.menu.add_checkbutton(label='Sobre', variable=aVar)

root.mainloop()