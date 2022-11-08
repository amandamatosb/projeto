from tkinter import *
from tkinter.messagebox import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import tkinter.messagebox

a = '#BCD2EE'

def banco():
  janela_bd = Tk()
  janela_bd.title('cadastros.dos.usuarios')
  janela_bd.config(bg=a)
  janela_bd.geometry('400x300+200+200')
  texto_inicio_bd = Label(janela_bd, bg=a, text='- BANCO DE DADOS DOS CADASTROS -')
  texto_inicio_bd.place(x='100', y='20')
  texto_ver = Label(janela_bd, bg=a, text='1 - Ver banco de dados')
  texto_ver.place(x='50', y='50')
  texto_excluir = Label(janela_bd, bg=a, text='2 - Excluir algum usuário do BD')
  texto_excluir.place(x='50', y='70')
  texto_voltar = Label(janela_bd, bg=a, text='3 - Voltar')
  texto_voltar.place(x='50', y='90')
  entrada_bd = Entry(janela_bd)
  entrada_bd.place(x='50', y='120')

  def bt_click():
    if int(entrada_bd.get()) == 1:
      ler_bd()

    elif int(entrada_bd.get()) == 2:
      janela_bd.destroy()
      excluir_dados()

    elif int(entrada_bd.get()) == 3:
      janela_bd.destroy()
      janela_visao.destroy()

    else:
      print(showerror("erro", 'não existe essa opção'))

  botao_bd = Button(janela_bd, text = 'enviar', command = bt_click)
  botao_bd.place(x='50', y='150')
  janela_bd.mainloop()

def bancodedados():
  global conexao, cursor
    # conectando
  conexao = sqlite3.connect('usuarios.db')

   # definindo um cursor
  cursor = conexao.cursor()

  # criando tabela
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS usuarios (
       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
          email TEXT NOT NULL
   );
  """)
def cadastrar(nome, email):
  bancodedados()

  # inserindo dados
  cursor.execute("""
                  INSERT INTO usuarios (nome, email)
                  VALUES (?,?)
                  """, (nome, email))

  conexao.commit()

  # desconectando
  cursor.close()
  conexao.close()

def ler_bd():
  global janela_visao
  janela_visao = Tk()
  janela_visao.title('cadastros.dos.usuarios')
  janela_visao.configure(bg=a)
  janela_visao.geometry('500x300')

  scrollbary = Scrollbar(janela_visao, orient=VERTICAL)
  scrollbarx = Scrollbar(janela_visao, orient=HORIZONTAL)

  global arvore
  arvore = ttk.Treeview(janela_visao, columns=("id", "nome", "email"), selectmode="extended", height=300,
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=arvore.yview)
  scrollbary.pack(side=RIGHT, fill=Y)
  scrollbarx.config(command=arvore.xview)
  scrollbarx.pack(side=BOTTOM, fill=X)
  arvore.heading('id', text="ID", anchor=W)
  arvore.heading('nome', text="NOME", anchor=W)
  arvore.heading('email', text="E-MAIL", anchor=W)
  arvore.column('#0', stretch=NO, minwidth=0, width=0)
  arvore.column('#1', stretch=NO, minwidth=0, width=80)
  arvore.column('#2', stretch=NO, minwidth=0, width=80)
  arvore.pack()
  arvore.delete(*arvore.get_children())
  bancodedados()

      # lendo dados
  cursor.execute("""SELECT * FROM `usuarios` ORDER BY `id` ASC;""")

  fetch = cursor.fetchall()  # retorna os resultados como tuplas e armazena em fetch
  for dados in fetch:  # insere tuplas do fetch na árvore
      arvore.insert('', 'end', values=(dados[0], dados[1], dados[2]))

  cursor.close()
  # desconectando
  conexao.close()

def excluir_dados():
  bancodedados()
  janela_excluir = Tk()
  janela_excluir.title('excluir.usuário')
  janela_excluir.config(bg=a)
  janela_excluir.geometry('400x300+200+200')
  texto_excluir = Label(janela_excluir, bg=a, text='- Digite o id do usuário -')
  texto_excluir.place(x='50', y='50')
  entrada_excluir = Entry(janela_excluir)
  entrada_excluir.place(x='50', y='80')
  texto_esquecer = Label(janela_excluir, bg=a, text='*caso tenha esquecido, aperte esse botão para voltar*')
  texto_esquecer.place(x='50', y='150')

  def bt_click():
    try:
      item = int(entrada_excluir.get())
      resultado = tkinter.messagebox.askquestion("confirmação", "realmente quer excluir aluno?",
                                                     icon="warning")

      if resultado == 'yes':
        cursor.execute("DELETE FROM usuarios WHERE id = ?",
                        (item,))  # apaga item selecionado do banco

        print(showinfo("pronto", 'usuário excluído com sucesso'))
        conexao.commit()
        conexao.close()
        janela_excluir.destroy()
        banco()

    except:
      print(showerror("erro", 'não existe esse usuário'))
      janela_excluir.destroy()
      excluir_dados()

  def bt_click1():
    janela_excluir.destroy()
    banco()  

  botao = Button(janela_excluir, text='enviar', command=bt_click)
  botao.place(x='50', y='110')

  botao_esquecer = Button(janela_excluir, text='voltar', command=bt_click1)
  botao_esquecer.place(x='50', y='180')

  janela_excluir.mainloop()
