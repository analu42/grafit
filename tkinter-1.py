import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

root = tk.Tk() #inicializa a primeira janela do tkinter

#EXIBIR MENSAGEM
messagebox.showinfo("Hello World", "Hello World") #messagebox de informação
messagebox.showwarning("Hello World", "Hello World")#messagebox de aviso
messagebox.showerror("Hello World", "Hello World") #messagebox de erro
#obs: os avisos aparecem em ordem, e não simultaneamente! ou seja, pelo código acima, o aviso só aparece
#quando eu fecho a janela da informação!!

#CAIXA DE INPUT
nome = simpledialog.askstring("Nome", "Nome:")  #pergunta uma string
cpf = simpledialog.askinteger( "CPF", "CPF:")  #pergunta um int
mass = simpledialog.askfloat("Massa", "Massa:") #pergunta um float

if nome:
    print("Bem vindo, ", nome)

if cpf:
    print("CPF: ", cpf)

if mass:
    print("Massa: ", mass)

#ESCOLHER ARQUIVO
arquivo = filedialog.askopenfilename() #abre arquivo
pasta = filedialog.askdirectory() #abre uma pasta
lista_arquivos = filedialog.askopenfilenames() #abre uma lista de arquivos

#PERSONALIZAR O FILEDIALOG
arquivo2 = filedialog.askopenfilename(
    title = "Selecione o arquivo desejado", #titulo do selecionador de arquivos
    filetypes = [("Arquivos de texto", "*.txt"), ("Planilha Excel", "*.xlsx")] #lista com todos os tipos de arquivo que o user pode selecionar
)
