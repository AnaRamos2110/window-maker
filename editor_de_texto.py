#Em algumas aulas anteriores fizemos algumas coisas com TKinter na matéria de algoritmos e na matéria de integração de banco com python
#No script de hoje, faremos um editor de texto simples e baseado no que aprendi até agora, comentarei as linhas do código para melhor compreensão e como aprimoramento de boas práticas!

import tkinter as tk #Chamando a biblioteca e fazendo alteração usando AS para abreviar o nome da biblioteca deixando mais intuitivo e fácil.
from tkinter.filedialog import askopenfilename, asksaveasfilename #importando a class filedialog --Li umas partes da documentação e vi que essa classe abrange bastante coisa-- --askopenfilename E, asksaveasfilename: para o usuário escolher um arquivo para abrir no editor, e para o usuário escolher o nome do arquivo e em que diretório será salvo!--

def abrir(): 
    #Para abrir os arquivos
    caminho = askopenfilename(
        filetypes=[("Arquivo de texto", "*.txt"), ("Salvar como: ", "*.*")]
    )
    
    if not caminho:
         return
    txt_edit.delete("1.0", tk.END)
    with open(caminho, mode="r", encoding="utf-8") as entrada:
        text = entrada.read()
        txt_edit.insert(tk.END, text)
    window.title(f'---Editor de Texto--- {caminho}')

"""
Resposta- ainda estou aprendendo sobre tkinter então peço ajuda pro chat sobre as funções e parâmetros pra entender melhor o que cada código faz no tkinter! obs: o legal de copiar é que ele joga tudo de volta formatado em MARKDOWN então já da pra estudar duas coisas de uma vez kkkk...

#filetypes é um parâmetro que define quais tipos de arquivos o diálogo de seleção de arquivos irá mostrar.


 Vamos analisar o argumento `filetypes` passado para a função `askopenfilename`:

```python
caminho = askopenfilename(
    filetypes=[("Arquivo de texto", "*.txt"), ("Salvar como: ", "*.*")]
)
```

### O que é `filetypes`?

- `filetypes` é um parâmetro que define quais tipos de arquivos o diálogo de seleção de arquivos irá mostrar.
- Ele espera uma **lista de tuplas**.
- Cada tupla tem dois elementos:
  1. Uma descrição legível para o usuário (ex: `"Arquivo de texto"`).
  2. Um padrão de extensão de arquivo (ex: `"*.txt"`).

### Por que uma lista de tuplas?

- **Lista**: Permite que você ofereça múltiplas opções de filtro no diálogo. Por exemplo, o usuário pode escolher ver apenas arquivos `.txt` ou todos os arquivos.
- **Tupla**: Cada tupla representa uma opção de filtro, com a descrição e o padrão de extensão juntos.

### Exemplo visual

No diálogo, aparecerá algo assim:
- Arquivo de texto (*.txt)
- Salvar como: (*.*)

O usuário pode escolher qual filtro usar para visualizar os arquivos.

### Resumindo

- **Lista**: Para múltiplas opções.
- **Tupla**: Para agrupar descrição e padrão de extensão.

Se precisar de um exemplo prático ou quiser ver como ficaria com outros tipos de arquivos, só pedir!

"""


def salvar():
    #Salva o arquivo atual
    caminho = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de texto", "*.txt"), ("Salvar como: ", "*.*")],
    )

    if not caminho:
        return
    with open(caminho, mode='w', encoding='utf-8') as saida:
        text = txt_edit.get('1.0', tk.END)
        saida.write(text)
    window.title(f"---Editor de Texto--- {caminho}")

window = tk.Tk()
window.title('---Editor de Texto---')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
button_open = tk.Button(frame_buttons, text='Abrir', command=abrir)
button_save = tk.Button(frame_buttons, text='Salvar', command=salvar)

button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5)

frame_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

