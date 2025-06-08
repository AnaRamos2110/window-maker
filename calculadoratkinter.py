from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.win = win
        self.lbl1 = Label(win, text='Primeiro número:')
        self.lbl2 = Label(win, text='Segundo valor:')
        self.lbl3 = Label(win, text='Total:')
        self.button_exit = Button(win, text='Sair', command=win.destroy)
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.button1 = Button(win, text='Adição', command=self.add)
        self.button2 = Button(win, text='Subtração', command=self.sub)
        self.button3 = Button(win, text='Multiplicação', command=self.mul)
        self.button4 = Button(win, text='Divisão', command=self.div)

        #Definindo posição dos botões:
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.button1.place(x=115, y=150)
        self.button2.place(x=170, y=150)
        self.button3.place(x=240, y=150)
        self.button4.place(x=330, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        self.button_exit.place(x=200, y=240)

#Criando a função de operadores aritméticos:
    def add(self):
        self.t3.delete(0, END)
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            resultado = num1 + num2
            self.t3.insert(END, str(resultado))
        except ValueError:
            self.t3.insert(END, "Erro")

    def sub(self):
        self.t3.delete(0, END)
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            resultado = num1 - num2
            self.t3.insert(END, str(resultado))
        except ValueError:
            self.t3.insert(END, "Erro")

    def mul(self):
        self.t3.delete(0, END)
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            resultado = num1 * num2
            self.t3.insert(END, str(resultado))
        except ValueError:
            self.t3.insert(END, "Erro")

    def div(self):
        self.t3.delete(0, END)
        try:
            num1 = float(self.t1.get())
            num2 = float(self.t2.get())
            if num2 != 0:
                resultado = num1 / num2
                self.t3.insert(END, str(resultado))
            else:
                self.t3.insert(END, "Erro: Divisão por zero")
        except ValueError:
            self.t3.insert(END, "Erro")

#Chamando classe para calculadora funcionar:
window = Tk()
window.title('Calculadora')
mywin = MyWindow(window)
window.geometry("450x300+10+10")
window.mainloop()
