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
    janela_agendamento.configure(bg=a)
    janela_agendamento.geometry('400x300+200+200')
    texto_ag = Label(janela_agendamento, bg=a, text='PLANNER - AGENDAMENTO')
    texto_ag.place(x='130', y='20')
    texto_eventos = Label(janela_agendamento, bg=a, text='1 - Eventos')
    texto_eventos.place(x='50', y='50')
    texto_agendamento = Label(janela_agendamento, bg=a, text='2 - Ver agendamentos')
    texto_agendamento.place(x='50', y='70')
    texto_voltar = Label(janela_agendamento, bg=a, text='3 - Voltar')
    texto_voltar.place(x='50', y='90')
    entrada_agendamento = Entry(janela_agendamento)
    entrada_agendamento.place(x='50', y='120')

    def bt_click():
      if int(entrada_agendamento.get()) == 1:
        janela_agendamento.destroy()
        self.eventos()
        self.menu_agendamento()
      elif int(entrada_agendamento.get()) == 2:
        janela_agendamento.destroy()
        self.exibir_eventos()
        self.menu_agendamento()
      elif int(entrada_agendamento.get()) == 3:
        janela_agendamento.destroy()
        pass
      else:
        print(showerror("erro", "digite uma das opções"))

    botao_enviar = Button(janela_agendamento, text='enviar', command=bt_click)
    botao_enviar.place(x='50', y='150')

    janela_agendamento.mainloop()

  def eventos(self):
    janela_eventos = Tk()
    janela_eventos.title('menu.eventos')
    janela_eventos.configure(bg=a)
    janela_eventos.geometry('400x300+200+200')
    texto_inicio = Label(janela_eventos, bg=a, text='PLANNER - EVENTOS')
    texto_inicio.place(x='150', y='20')
    texto_ae = Label(janela_eventos, bg=a, text='1 - Adicionar Evento')
    texto_ae.place(x='50', y='50')
    texto_me = Label(janela_eventos, bg=a, text='2 - Excluir Evento')
    texto_me.place(x='50', y='70')
    texto_ev = Label(janela_eventos, bg=a, text='3 - Voltar')
    texto_ev.place(x='50', y='90')
    entrada_eventos = Entry(janela_eventos)
    entrada_eventos.place(x='50', y='120')

    def bt_click():
      if int(entrada_eventos.get()) == 1:
        janela_eventos.destroy()
        self.__evento.agendar_evento()
      elif int(entrada_eventos.get()) == 2:
        janela_eventos.destroy()
        self.__evento.excluir_evento()
      elif int(entrada_eventos.get()) == 3:
        janela_eventos.destroy()
        pass
      else:
        print(showerror("erro", 'digite uma das opções'))

    botao_enviar = Button(janela_eventos, text='enviar', command=bt_click)
    botao_enviar.place(x='50', y='150')

    janela_eventos.mainloop()

  def exibir_eventos(self):
    janela_planner = Tk()
    janela_planner.title('agendamento')
    janela_planner.geometry('860x300+200+100')
    janela_planner.configure(bg=a)

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

    def bt_click():
      janela_planner.destroy()
      self.menu_agendamento()

    botao = Button(janela_planner, text='voltar', command=bt_click)
    botao.place(x='50', y='240')

    janela_planner.mainloop()
