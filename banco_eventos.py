from tkinter import *
from tkinter.messagebox import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import tkinter.messagebox

a = '#BCD2EE'

def banco_eventos():
    janela_bd = Tk()
    janela_bd.title('bd.eventos')
    janela_bd.geometry('700x394')
    img = PhotoImage(file='imagens/banco_eventos.png')
    labelimage_inicio = Label(image=img)
    labelimage_inicio.pack(side=LEFT)
    entrada_bd = Entry(janela_bd)
    entrada_bd.place(x='58', y='197')

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

    img_enviar = PhotoImage(file='imagens/botao_enviar2.png')
    botao_bd = Button(janela_bd, image=img_enviar, command=bt_click, borderwidth=0)
    botao_bd.place(x='58', y='257', w='72', h='25')

    def voltar():
      janela_bd.destroy()
      janela_visao.destroy()

    img_voltar = PhotoImage(file='imagens/botao_voltar1.png')
    botao_voltar = Button(janela_bd, image=img_voltar, command = voltar, borderwidth=0)
    botao_voltar.place(x='562', y='334', w='72', h='25')

    janela_bd.mainloop()

def bancodedados():
    global conexao, cursor
      # conectando
    conexao = sqlite3.connect('bancos/eventos.db')

     # definindo um cursor
    cursor = conexao.cursor()

    # criando tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eventos (
         cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         nome TEXT NOT NULL,
         local TEXT NOT NULL,
         data  TEXT NOT NULL  
         
     );
    """)
def cadastrar(nome, data, local):
    bancodedados()

    # inserindo dados
    cursor.execute("""
                    INSERT INTO eventos (nome, local, data)
                    VALUES (?,?,?)
                    """, (nome, local, data))

    conexao.commit()

    # desconectando
    cursor.close()
    conexao.close()

def ler_bd():
    global janela_visao
    janela_visao = Tk()
    janela_visao.title('cadastros.dos.eventos')
    janela_visao.geometry('700x394')

    scrollbary = Scrollbar(janela_visao, orient=VERTICAL)
    scrollbarx = Scrollbar(janela_visao, orient=HORIZONTAL)

    global arvore
    arvore = ttk.Treeview(janela_visao, columns=("cod", "nome", "local", "data"), selectmode="extended", height=300,
                              yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=arvore.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=arvore.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    arvore.heading('cod', text="COD", anchor=W)
    arvore.heading('nome', text="NOME", anchor=W)
    arvore.heading('data', text="DATA", anchor=W)
    arvore.heading('local', text="LOCAL", anchor=W)
    arvore.column('#0', stretch=NO, minwidth=0, width=0)
    arvore.column('#1', stretch=NO, minwidth=0, width=80)
    arvore.column('#2', stretch=NO, minwidth=0, width=80)
    arvore.column('#3', stretch=NO, minwidth=0, width=80)
    arvore.pack()
    arvore.delete(*arvore.get_children())
    bancodedados()

        # lendo dados
    cursor.execute("""SELECT * FROM `eventos` ORDER BY `cod` ASC;""")

    fetch = cursor.fetchall()  # retorna os resultados como tuplas e armazena em fetch
    for dados in fetch:  # insere tuplas do fetch na árvore
        arvore.insert('', 'end', values=(dados[0], dados[1], dados[2], dados[3]))

    cursor.close()
    # desconectando
    conexao.close()

def excluir_dados():
    bancodedados()
    janela_excluir = Tk()
    janela_excluir.title('excluir.evento')
    janela_excluir.config(bg=a)
    janela_excluir.geometry('700x394')
    img = PhotoImage(file='imagens/bd_excluir1.png')
    labelimage_inicio = Label(image=img)
    labelimage_inicio.pack(side=LEFT)
    entrada_excluir = Entry(janela_excluir)
    entrada_excluir.place(x='270', y='175', w='159', h='21')

    def bt_click():
        try:
            item = int(entrada_excluir.get())
            resultado = tkinter.messagebox.askquestion("confirmação", "realmente quer excluir esse evento?",
                                                           icon="warning")

            if resultado == 'yes':
                cursor.execute("DELETE FROM eventos WHERE cod = ?",
                                (item,))  # apaga item selecionado do banco

                print(showinfo("pronto", 'evento excluído com sucesso'))
                conexao.commit()
                conexao.close()
                janela_excluir.destroy()
                banco_eventos()

        except:
            print(showerror("erro", 'não existe esse usuário'))
            janela_excluir.destroy()
            excluir_dados()

    def voltar():
        janela_excluir.destroy()
        banco_eventos()

    img_enviar = PhotoImage(file='imagens/botao_enviar1.png')
    botao = Button(janela_excluir, image=img_enviar, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='72', h='25')

    img_voltar = PhotoImage(file='imagens/botao_voltar2.png')
    botao_voltar = Button(janela_excluir, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='570', y='14', w='72', h='25')

    janela_excluir.mainloop()