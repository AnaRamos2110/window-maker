'''
import tkinter as tk #Chamando a biblioteca
class App(tk.Frame):
    def __init__(self, master): #Inicializando a class com um método e chamando a função 'mestre' no parâmetro
        super().__init__(master)
        self.pack()

        # Criando a variável do app (variável ligada ao texto do Entry)
        self.contents= tk.StringVar()
        
        #Define o valor do campo (texto)
        self.contents.set('')


        #Criando o widget Entry e vinculando à variável self.contents
        self.entrythingy = tk.Entry(self, textvariable=self.contents)
        self.entrythingy.pack()
       
    
        #Liga o evento da tecla Enter (Return) para chamar o método print_contents
        self.entrythingy.bind('<Key-Return>', self.print_contents)

         
        #Imprime p valor atuial da variável.
    def print_contents(self, event):
        print('A palavra digitada foi:',
              self.contents.get())
    
    def clear_text(self):
        # Limpa o conteúdo do Entry
        self.contents.set('')
        





root = tk.Tk()
myapp = App(root)
myapp.mainloop()
'''


#Agora com adições de comandos novos
#O código anterior foi o exemplo visto em sala, porém, houve novos botões como o botão apagar e sair da janela.

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.contents =tk.StringVar()
        #Deixar o campo vazio

        # Cria um widget Entry (campo de texto) dentro do Frame (self)
        # A variável self.contents (StringVar) fica vinculada ao texto do Entry,
        # permitindo sincronizar o conteúdo entre código e interface
        self.entrythingy = tk.Entry(self, textvariable=self.contents)

        # Posiciona o Entry na interface usando pack, com espaçamento vertical (pady) de 10 pixels
        # Isso evita que o widget fique grudado em outros elementos acima ou abaixo
        self.entrythingy.pack(pady=10)


        #Foca o cursor no campo de texto assim que inicia para deixar o campo mais intuitivo
        self.entrythingy.focus_set()
        self.entrythingy.bind('<Return>', self.print_contents)

        button_frame = tk.Frame(self)
        button_frame.pack()

        self.button_enter = tk.Button(button_frame, text="Entrada", command=self.print_contents_button) #Criando botão para o usuário identificar onde confirma entrada de dados
        self.button_enter.pack(side=tk.LEFT, padx=5)

        self.button_clear = tk.Button(button_frame, text="Apagar", command=self.clear_text) #Criando botão para apagar texto
        self.button_clear.pack(side=tk.LEFT, padx=5)

        self.button_exit = tk.Button(button_frame, text="Sair", command=self.exit_app) #Criando botão para sair da tela
        self.button_exit.pack(side=tk.LEFT, padx=5)
    
    def print_contents(self, event):
        print("A palavra digitada foi: ", self.contents.get())

    def print_contents_button(self):
        print('A palavra digitada foi: ', self.contents.get())
    
    def clear_text(self): #Chamando o botão --botton_clear--
        self.contents.set('')
        self.entrythingy.focus_set()

    def exit_app(self):  #Chamando o botão --sair--
        self.master.destroy() 


root = tk.Tk()
myapp = App(root)
myapp.mainloop()