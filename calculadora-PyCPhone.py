#ESTA CALCULADORA SERÁ COM UMA INTERFACE MAIS COMPLEXA DO QUE A ANTERIOR QUE TAMBÉM ESTÁ NESTE REPOSITÓRIO!
#É PARECIDA COM A CALCULADORA DE UMA DAS INTERFACES DO PYPHONE(INCLUSIVE A COR)!

#CHAMANDO O MÓDULO TKINTER PARA A GUI- (GRAPIHC USER INTERFACE)

import tkinter as tk

#função que será chamada quando o usuário clicar em um botão da calculadora
def click(event):
    #captura o texto do botão que foi clicado
    text = event.widget.cget('text')

    #Verifica se o botão clicado foi o '=' (para calcular o resultado)
    if text == "=":
        try:
            #avalia a expressão contida na tela (usando eval)
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            #Caso haja erro na expressão (ex: divisão por zero), exibe "erro" na tela.
            screen.set("Erro")

    #Se o botão clicado foi "C", limpa a tela da calculadora
    elif text == "c":
        screen.set("")
    
    #Caso contrário (para qulquer outro botão), adiciona o texto do botão à expressão na tela
    else:
        screen.set(screen.get() + text)

#Configuração da janela principal da calculadora
root = tk.Tk() #Criau uma nova janela
root.title("Calculadora - PyCPhone") #Define o titulo da janela
root.geometry("350x500") #Define o tamanho da janela (largura x altura)
root.config(bg='#F0F0F0') #Configura a cor de fundo da janela (cinza claro, estilo windows)

#Variável para armazenar o texto que será exibido na tela da calculadora
screen = tk.StringVar()

#Caixa de entrada onde as expressões e resultados serão exibidos
entry = tk.Entry(root, textvar=screen, font="Arial 24", bd=10, insertwidth=2, width=14, justify='right')
#Configura a parência da caixa de entrada (fonte, borda, alinhamento à direita):
entry.pack(fill="both", ipadx=10, pady=20) #Posiciona a caixa na interface

#Lista de botões da calculadora, organizados por linha
buttons = [
    ['7', '8', '9','/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['c', '0', '=', '+'],
]

#Função para criar os botões com o estilo especifíco
def create_button(frame, text, color="#FFFFFF", bg="#C0C0C0"):
    #Cria um botão com o texto, cor do texto, cor de fundo, e estilo desejado
    button = tk.Button(frame, text=text, font='Arial 20', padx=20, pady=20, bg=bg, fg=color, borderwidth=0)
    #Posiciona o botão no frame(linha) e ajusta o tamanho para preencher o espaço disponivel
    button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
    #Associa a função click ao evento clique do botão
    button.bind('<Button-1>', click)
    return button

#Laço para criar e organizar os botões na interface
for row in buttons:
    #Cria um frame (linha) para organizar os botões da calculadora
    frame = tk.Frame(root, bg="#F0F0F0") #Cor de fundo similar à calculadora do Windows
    frame.pack(expand=True, fill="both") #Ajusta o frame para preencher o espaço disponíuvel

#Para cada botão na linha, cria o botão com as cores e comportamentos apropriados
    for button_text in row:
        if button_text in ['+', '-', '*', '/', '=']:
            #Botões de operações (+,-,*, /, =) têm cor laranja
            create_button(frame, button_text, color='#FFFFFF', bg='#FFA500')
        elif button_text == "c":
            #O botão de limpar ('c) é vermelho
            create_button(frame, button_text, color="#FFFFFF", bg='#FF6347')
        else:
            #Botões numéricos (0-9) tem o estilo padrão (cinza claro)
            create_button(frame, button_text)

#Inicia o loop principal da interface gráfica
root.mainloop()