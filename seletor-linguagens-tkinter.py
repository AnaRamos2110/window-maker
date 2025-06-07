'''
import tkinter as Tk from tkinter import * top = Tk()
Listboxx = Listbox(top) 
Listboxx = (1, 'Python')
Listboxx = (2, 'Java')
Listboxx =(3, 'C++')
Listboxx = [4, 'PHP'] 
Listboxx = [5, 'JavaScript'] 
Listboxx = [6, 'Ruby'] 
Listboxx.pack() 
top.mainloop()
'''
#Correções no código-- não tava compilando pois pras tuplas percorrerem melhor precisariam estar dentro de uma lista. 
#Para conhecer a opção de listagem no tkinter :)
'''
import tkinter as tk
from tkinter import *

top = tk.Tk()
listboxx = tk.Listbox(top)
linguagens = [(1, 'Python'), (2, 'Java'), (3, 'C++'), (4, 'PHP'),(5, 'JavaScript'), (6, 'Ruby')]
#Gerando iteração pra percorrer na lista
for linguas in linguagens:
    listboxx.insert(tk.END, f"{linguas[0]} - {linguas[1]}")

listboxx.pack()
top.mainloop()
'''
#Para incrementar: Funcionalidade de alguns botões, adição e remoção de linguagem e sair do programa. Também uma barra de rolagem para melhor experiência e correção de índices para nenhum se repetir usando um contador para indice.

import tkinter as tk
from tkinter import messagebox

#Contador global para os índices únicos
contador_indice = 6 #Começamos a lista com 5 índices.
 
def mostrar_linguagem_selecionada(): #Função para o usuário ver o que escolheu na tela.
    indice_selecionado = lista_linguagens.curselection()
    if indice_selecionado:
        linguagem = lista_linguagens.get(indice_selecionado)
        messagebox.showinfo("Linguagem Selecionada", f"Você selecionou: {linguagem}")
    else:
        messagebox.showwarning("Aviso!", "Selecione uma linguagem da lista!")

def adicionar_nova_linguagem(): #função para o usuário escolher nova linguagem.
    global contador_indice #Chamando o contador de fora da função.
    nome_linguagem = entrada_nome_linguagem.get().strip()
    if nome_linguagem:
        contador_indice += 1 #Aqui garante que nenhum índice vai repetir na lista da nossa tela
        lista_linguagens.insert(tk.END, f"{contador_indice} - {nome_linguagem}")
        entrada_nome_linguagem.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso!", "Digite o nome da linguagem!")

def remover_linguagem_selecionada(): #Função para remover linguagem selecionada.
    indice_selecionado = lista_linguagens.curselection()
    if indice_selecionado:
        lista_linguagens.delete(indice_selecionado) #Se você chamar o índice, ele vai ser deletado
    else:
        messagebox.showwarning("Aviso", "Selecione uma linguagem para remover!") #Senão selecionar a mensagem, gera um aviso pedindo pra você escolher a linguagem.

#Janela principal:
janela_principal = tk.Tk()
janela_principal.title("Lista de linguagens de programação: ")

#Frame para agrupar o listbox e a barra de rolagem:
quadro_lista = tk.Frame(janela_principal)
quadro_lista.pack(pady=10)

#Barra de rolagem(Scrollbar):
barra_de_rolagem = tk.Scrollbar(quadro_lista)
barra_de_rolagem.pack(side=tk.RIGHT, fill=tk.Y)

#Listbox com a barra de rolagem integrada:
lista_linguagens = tk.Listbox(quadro_lista, width=40, yscrollcommand=barra_de_rolagem.set)
lista_linguagens.pack(side=tk.LEFT)

barra_de_rolagem.config(command=lista_linguagens.yview)

#Dados iniciais
lista_inicial = [
    (1, 'Python'),
    (2, 'Java'),
    (3, 'C++'),
    (4, 'PHP'),
    (5, 'Javascript'),
    (6, 'Ruby')
]

for identificador, nome in lista_inicial:
    lista_linguagens.insert(tk.END, f"{identificador} - {nome}")

# Botões de ação
botao_mostrar = tk.Button(janela_principal, text="Mostrar Selecionado",command=mostrar_linguagem_selecionada)
botao_mostrar.pack(pady=5)

botao_remover = tk.Button(janela_principal, text="Remover Selecionado", command=remover_linguagem_selecionada)
botao_remover.pack(pady=5)

#Campo para adicionar nova linguagem
quadro_adicao = tk.Frame(janela_principal)
quadro_adicao.pack(pady=10)

entrada_nome_linguagem = tk.Entry(quadro_adicao)
entrada_nome_linguagem.pack(side=tk.LEFT, padx=5)

botao_adicionar = tk.Button(quadro_adicao, text="Adicionar Linguagem: ", command=adicionar_nova_linguagem)
botao_adicionar.pack(side=tk.LEFT)

#Iniciar o loop da interface
janela_principal.mainloop()