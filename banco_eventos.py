from tkinter import *
from tkinter.messagebox import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import tkinter.messagebox

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
        try:
            if int(entrada_bd.get()) == 1:
                janela_bd.destroy()
                ler_bd()

            elif int(entrada_bd.get()) == 2:
                janela_bd.destroy()
                excluir_dados()

            else:
                raise ValueError()

        except(TypeError, ValueError):
            print(showerror("Erro", 'Digite correto.'))
            entrada_bd.delete(0, END)

    img_enviar = PhotoImage(file='imagens/botao_enviar2.png')
    botao_bd = Button(janela_bd, image=img_enviar, command=bt_click, borderwidth=0)
    botao_bd.place(x='58', y='257', w='72', h='33')

    def voltar():
      janela_bd.destroy()

    img_voltar = PhotoImage(file='imagens/botao_voltar1.png')
    botao_voltar = Button(janela_bd, image=img_voltar, command = voltar, borderwidth=0)
    botao_voltar.place(x='562', y='334', w='72', h='33')

    janela_bd.mainloop()

def bancodedados():
    global conexao, cursor
    conexao = sqlite3.connect('bancos/eventos.db')

    cursor = conexao.cursor()

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

    cursor.execute("""
                    INSERT INTO eventos (nome, local, data)
                    VALUES (?,?,?)
                    """, (nome, local, data))

    conexao.commit()

    cursor.close()
    conexao.close()

def ler_bd():
    global janela_visao
    janela_visao = Tk()
    janela_visao.title('banco.dos.eventos')
    janela_visao.geometry('700x394')
    janela_visao.configure(bg = '#FBF8F0')

    def voltar():
        janela_visao.destroy()
        banco_eventos()

    img_voltar = PhotoImage(file='imagens/botao_voltar2.png')
    botao_voltar = Button(janela_visao, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='20', y='30', w='72', h='33')

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

    cursor.execute("""SELECT * FROM `eventos` ORDER BY `cod` ASC;""")

    fetch = cursor.fetchall()
    for dados in fetch:
        arvore.insert('', 'end', values=(dados[0], dados[1], dados[2], dados[3]))

    cursor.close()
    conexao.close()

    janela_visao.mainloop()

def excluir_dados():
    bancodedados()
    janela_excluir = Tk()
    janela_excluir.title('excluir.evento')
    janela_excluir.geometry('700x394')
    img = PhotoImage(file='imagens/bd_excluir1.png')
    labelimage_inicio = Label(image=img)
    labelimage_inicio.pack(side=LEFT)
    entrada_excluir = Entry(janela_excluir)
    entrada_excluir.place(x='270', y='175', w='159', h='21')

    def bt_click():
        try:
            item = int(entrada_excluir.get())
            resultado = tkinter.messagebox.askquestion("Confirmação", "Realmente quer excluir esse evento?",
                                                           icon="warning")

            if resultado == 'yes':
                cursor.execute("DELETE FROM eventos WHERE cod = ?",
                                (item,))  

                print(showinfo("Pronto", 'Evento excluído com sucesso.'))
                conexao.commit()
                conexao.close()
                janela_excluir.destroy()
                banco_eventos()

        except:
            print(showerror("Erro", 'Não existe esse usuário.'))
            janela_excluir.destroy()
            excluir_dados()

    def voltar():
        janela_excluir.destroy()
        banco_eventos()

    img_enviar = PhotoImage(file='imagens/botao_enviar1.png')
    botao = Button(janela_excluir, image=img_enviar, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='72', h='33')

    img_voltar = PhotoImage(file='imagens/botao_voltar2.png')
    botao_voltar = Button(janela_excluir, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='570', y='14', w='72', h='33')

    janela_excluir.mainloop()

