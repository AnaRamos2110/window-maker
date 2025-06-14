'''Projeto-- Gerenciador de notas
UM SOFTWARE SIMPLES QUE PERMITE ADICIONAR, VISUALIZAR E GERENCIAR NOTAS (BLOCOS DE ANOTAÇÕES).
FUNCIONALIDADES -- ADICIONAR, EDITAR E EXCLUIR NOTAS.
SALVAR NOTAS EM ARQUIVOS DE TEXTO.

DOCUMENTAÇÃO-- OBJETIVO: DESENVOLVER UM GERENCIADOR DE NOTAS QUE PERMITA SALVAR E VISUALIZAR ANOTAÇÕES USANDO TKINTER.

INSTRUÇÕES -- CRIAR JANELA PRINCIPAL NO TKINTER
IMPLEMENTAR A FUNÇÃO DE ADICIONAR UMA NOVA NOTA E SALVAR EM UM  ARQUIVO DE TEXTO.
CRIAR UMA LISTA QUE EXIBA AS NOTAS JÁ SALVAS.
PERMITIR AO USUÁRIO REMOVER E EDITAR NOTAS.
'''

#Importação das bibliotecas do tkinter
#tk: é a biblioteca principal do tkinter para criar a interface gráfica.
#simpledialog: permite criar caixas de diálogo simples para solicitar entradas do usuário.
#messagebox: usada para exibir mensagens, como alertas ou avisos.

import tkinter as tk
from tkinter import simpledialog, messagebox, Button

#Função para adicionar uma nova nota
#Essa função abre uma caixa de diálogo  pedindo ao usuário que insira uma nova nota.
#Se o usuário inserir uma nota, ela será adicionada à listbox (a lista de notas na interface).

def add_note():
    note = simpledialog.askstring("Nota", "Digite sua nota: ") #Abre uma caixa de diálogo para digitar a nota
    if note: #Verifica se o usuário digitou alguma coisa
        listbox.insert(tk.END, note) #Insere a nota ao final da listbox

#Função para deletar a nota selecionada
#O usuário deve selecionar uma nota na lista. Se nenhuma nota for selecionada, um aviso aparecerá.
#Caso uma nova nota seja selecionada, ela será removida da listbox.

def delete_note():
    try:
        selected_note = listbox.curselection()[0] #Obtém o índice da nota selecionada
        listbox.delete(selected_note) #Remove a nota com base no índice selecionado
    except:
        messagebox.showwarning("Aviso", "Nenhuma nota selecionada. ") #Exibe uma mensagem de aviso  se nada estiver selecionado

   
#Criação da janela principal da aplicação
root = tk.Tk() #Inicializa a janela principal
root.title("Gerenciador de notas ") #Define o título da janela principal


#Criação da listbox (lista onde as notas serão executadas):
#Configuramos a fonte, a altura e a largura da listbox.
listbox = tk.Listbox(root, font="Arial 14", height=10, width=50)
listbox.pack(pady=10) #Define o espaçamento vertical ao redor da listbox

#Criação do botão 'Adicionar nota'
#Quando clicado, ele chama a função add_note:
add_button = tk.Button(root, text="Adicionar nota", command=add_note, font="Arial 14")
add_button.pack(pady=5) #Define o espaçamento vertical ao redor do botão

#Criação do botão remover_nota
#Quando clicado, ele chama a função delete_note
delete_button = tk.Button(root, text="Remover nota?", command=delete_note, font='Ariual 14')
delete_button.pack(pady=5)

#criação do botão 'sair' para fechar a aplicação:
add_button = tk.Button(root, text="Sair", command=root.destroy, font='Arial, 14')
add_button.pack(pady=5)


#Inicia o loop principal da interface gráfica, permitindo que a janela seja exibida e interativa
root.mainloop()