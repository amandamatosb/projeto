from calendario import Calendario
from evento import Evento
import tkinter as tk
from banco_eventos import *
from usuario import *

a = '#BCD2EE'


class Agendamento:
  def __init__(self):
   self.__data = Calendario()
   self.__evento = Evento()

  def menu_agendamento(self):
    janela_agendamento = Tk()
    janela_agendamento.title('menu.agendamento')
    janela_agendamento.geometry('700x394')
    img = PhotoImage(file='imagens/agendamento.png')
    labelimage_inicio = Label(image=img)
    labelimage_inicio.pack(side=LEFT)
    entrada_agendamento = Entry(janela_agendamento)
    entrada_agendamento.place(x='58', y='197')

    def bt_click():
      if int(entrada_agendamento.get()) == 1:
        janela_agendamento.destroy()
        self.eventos()
        self.menu_agendamento()
      elif int(entrada_agendamento.get()) == 2:
        janela_agendamento.destroy()
        self.exibir_eventos()
        self.menu_agendamento()
      else:
        print(showerror("erro", "digite uma das opções"))

    img_enviar = PhotoImage(file='imagens/botao_enviar2.png')
    botao_bd = Button(janela_agendamento, image=img_enviar, command=bt_click, borderwidth=0)
    botao_bd.place(x='58', y='257', w='72',  h='33')

    def voltar():
      janela_agendamento.destroy()

    img_voltar = PhotoImage(file='imagens/botao_voltar1.png')
    botao_voltar = Button(janela_agendamento, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='562', y='334', w='72', h='33')

    janela_agendamento.mainloop()

  def eventos(self):
    janela_eventos = Tk()
    janela_eventos.title('menu.eventos')
    janela_eventos.geometry('700x394')
    img = PhotoImage(file='imagens/eventos.png')
    labelimage_inicio = Label(image=img)
    labelimage_inicio.pack(side=LEFT)
    entrada_eventos = Entry(janela_eventos)
    entrada_eventos.place(x='58', y='197')

    def bt_click():
      if int(entrada_eventos.get()) == 1:
        janela_eventos.destroy()
        self.__evento.agendar_evento()
      elif int(entrada_eventos.get()) == 2:
        janela_eventos.destroy()
        self.__evento.excluir_evento()
      else:
        print(showerror("erro", 'digite uma das opções'))

    img_enviar = PhotoImage(file='imagens/botao_enviar2.png')
    botao_bd = Button(janela_eventos, image=img_enviar, command=bt_click, borderwidth=0)
    botao_bd.place(x='58', y='257', w='72', h='33')

    def voltar():
      janela_eventos.destroy()

    img_voltar = PhotoImage(file='imagens/botao_voltar1.png')
    botao_voltar = Button(janela_eventos, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='562', y='334', w='72', h='33' )

    janela_eventos.mainloop()

  def exibir_eventos(self):
    janela_planner = Tk()
    janela_planner.title('agendamento')
    janela_planner.geometry('860x300+200+100')
    janela_planner.configure(bg='#FBF8F0')

    columns = ('codigo', 'nome', 'data', 'local')

    agendamentos = ttk.Treeview(janela_planner, columns=columns, show='headings')

    agendamentos.heading('codigo', text='CÓDIGO')
    agendamentos.heading('nome', text='NOME')
    agendamentos.heading('data', text='DATA')
    agendamentos.heading('local', text='LOCAL')

    for e in self.__evento.eventos:
      agendamentos.insert('', tk.END, values=e)

    def item_selected():
      for selected_item in agendamentos.selection():
        item = agendamentos.item(selected_item)
        record = item['values']
        showinfo(title='Information', message=','.join(record))

        agendamentos.bind('<<TreeviewSelect>>', item_selected)

    agendamentos.grid(row=0, column=0, sticky='nsew')

    scrollbar = Scrollbar(janela_planner, orient=tk.VERTICAL, command=agendamentos.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')

    def voltar():
      janela_planner.destroy()

    img_voltar = PhotoImage(file='imagens/botao_voltar2.png')
    botao_voltar = Button(janela_planner, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='50', y='240', w='72', h='33')

    janela_planner.mainloop()
