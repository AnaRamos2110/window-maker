#Hoje é dia 13/06 e meu professor está fazendo aniversário ! Para desejar parabéns em grande estilo, faremos uma aplicação simples em formato de tkinter já que ele está nos ensinando, nada mais justo não é :)



import tkinter as tk

#Criando função para chama-la com mais facilidade ao invés de chamar várias variáveis

def main():
    root = tk.Tk() #Chamando a principal função da biblioteca e atribuindo a variavel 'root'
    root.title('Happy birthday !') #Titulo da minha tela.

    root.geometry('700x450') #Tamanho da tela o primeiro número é para largura, o segundo valor para a altura da tela.
    root.configure(bg="#c8b0d1") #Cor de fundo

    mensagem = "Não poderia esquecer do seu aniver né?? \nProf. Santorsula, obrigada por tanto! Te desejamos sucesso, felicidades, saúde,\nmuito pix e camisas estilosas feitas pela dona Maria!! \nObrigada por ser meu mentor e um Feliz aniversário <3 " #Mensagem que será exibida na tela
    label = tk.Label(root, text=mensagem, font=('Arial', 12, "bold"), bg="#c8b0d1", fg="#13074b", justify='center') #Definindo a caixa de texto e atribuindo a variável à função Label (caixa de texto), tipo de fonte, cor de fundo e cor da fonte; redimensionando para o centro da tela;
    label.pack(expand=True) #Expand para deixar o alinhamento da string mais bem direcionado e 'bonito'

    root.mainloop() #Chamando a variável principal dentro do código

if __name__ == "__main__":
    main() #Por fim, chamando a função para ser executada!! 


#TMJ, Santorsula! você é o cara <8) 