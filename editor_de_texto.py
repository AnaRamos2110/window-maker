#Em algumas aulas anteriores fizemos algumas coisas com TKinter na matéria de algoritmos e na matéria de integração de banco com python
#No script de hoje, faremos um editor de texto simples

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

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

