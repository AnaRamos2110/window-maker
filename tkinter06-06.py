from tkinter import *  
# O * (asterisco) no comando from tkinter import * significa que você está importando **tudo** do módulo tkinter para o seu código.

top = Tk()
botaomenu = Menubutton(top, text='Menu principal')
botaomenu.grid()
botaomenu.menu = Menu(botaomenu, tearoff=0)
botaomenu["Menu"] = botaomenu.menu
cVar = IntVar()
aVar = IntVar