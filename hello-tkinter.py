'''
Este código pode ser lido dentro da documentação do TKinter!!
Apenas uma demonstração do que essa biblioteca pode fazer, eu achei muito bom pra quem tá iniciando no tk então ela vem pro windowmaker><
'''
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()