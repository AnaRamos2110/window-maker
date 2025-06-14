import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def save_client_data():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()

    #Verifica se todos os campos estão preenchidos
    if name and email and phone:
        #Formata os dados em uma string para serem salvos no arquivo:
        data = f"Nome : {name}, Email: {email}, Telefone: {phone}\n"
        #Abre o arquivo clientes.txt no modo de adição ("a") e escreve os dados
        with open("clientes.txt", "a") as file: #-->Substitui "clientes.txt" pela localização correta do seu arquivo.txt
            file.write(data)
        #Exibe uma mensagem de sucesso após salvar os dados
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        #Limpa os campos de entrada após salvar
        clear_fields()


    else:
        #Exibe uma mensagem de aviso se algum campo estiver vazio
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")

#Função para limpar os campos de entrada de texto
#Após salvar os dados, os campos de nome, email e telefone são apagados para uma nova entrada

def search_client():
    search_name = entry_search.get().lower() #Pega o nome a ser buscado e converte para minúsculas para evitar problemas com maiúsculas/minúsculas
    if not search_name: #Se o campo de busca estiver vazio, exibe um aviso
        messagebox.showwarning("Aviso", "Digite um nome para buscar!")

    try:
        #Tenta abrir o arquivo clientes.txt para leitura
        with open("clientes.txt", "r") as file:
            found = False #Variável para verificar se o cliente foi encontradso
        #Laço de iteração que vai percorrer cada linha do arquivo
        for line in file:
                #Se o nome buscado estiver na linha, exibe os dados do cliente
                if search_name in line.lower():
                    messagebox.showinfo("Cliente encontrado", f"Dados: {line}")
                    found = True #Marca que o cliente foi encontrado
                    break
            #Se o cliente não for encontrado, exibe uma mensagem informando
        if not found:
            messagebox.showinfo("Cliente Não Encontrado", "Nenhum cliente encontrado com esse nome.")
    except FileNotFoundError:
         #Se o arquivoclientes.txt não for encontrado, exibe uma mensagem de erro
         messagebox.showwarning("Erro", "O arquivo de clientes não foi encontrado.")

#Função para aplicar um estilo moderno aos widgets (botões, entradas de texto, etc.)
#Aqui personalizamos o visual da interface, usando o tema "clam" e configurando fontes, cores, etc.
def apply_style():
    style = ttk.Style()
    style.theme_use('clam') #Define o tema "clam", que é um tema moderno e clean

    #Configurações para os botões (TButton), como fonte, cor de fundo e estilo
    style.configure("TButton", font=("Segoe UI",10), padding=6, relief='flat', background="#0078D7", foreground="white")
    style.map("TButton", background=[("active", "#005A9E")]) #Muda a cor do botão ao ser clicado
   
    #Configurações para os rótulos (TLabel)
    style.configure("TLabel", font=('Segoe UI', 11), padding=5, background="#F3F3F3", foreground="#333")
    #Configurações para os campos de entrada de texto (TEntry)
    style.configure("TEntry", font=("Segoe UI", 11), padding=5, relief="solid", borderwidth=1)

    #configuração para o fundo dos frames
    style.configure("TFrame", background="#F3F3F3")

    #Criação da janela principal da aplicação
    root = tk.TK() #Inicializa a janela principal
    root.title("Cadastro de Cliente") #Define o título da janela
    root.geometry("440x460") #Define o tamanho da janela (largura x altura)
    root.resizable(False, False) #Impede que a janela seja redimensionada
    root.configure(bg="#F3F3F3") #Define a cor de fundo da janela

    #Aplica o estilo moderno aos widgets da interface
    apply_style()

    #Frame principal que centraliza 
    