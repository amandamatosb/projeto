from calendario import Calendario
from evento import Evento
import os
import time
from tkinter import *
from tkinter.messagebox import *

a = '#BCD2EE'

class Agendamento:
    def __init__(self):
        self.__data = Calendario()
        self.__evento = Evento()

    def menu_agendamento(self):
        janela_agendamento = Tk()
        janela_agendamento.title('PLANNER - AGENDAMENTO')
        janela_agendamento.configure(bg=a)
        janela_agendamento.geometry('400x300+200+200')
        texto_ag = Label(janela_agendamento, bg=a, text='PLANNER - AGENDAMENTO')
        texto_ag.place(x='130', y='20')
        texto_eventos = Label(janela_agendamento, bg=a, text='1 - Eventos')
        texto_eventos.place(x='50', y='50')
        texto_agendamento = Label(janela_agendamento, bg=a, text='2 - Ver agendamentos')
        texto_agendamento.place(x = '50', y='70')
        texto_voltar = Label(janela_agendamento, bg=a, text='3 - Voltar')
        texto_voltar.place(x='50', y='90')
        entrada_agendamento = Entry(janela_agendamento)
        entrada_agendamento.place(x='50', y='120')

        def bt_click():
            if int(entrada_agendamento.get()) == 1:
                self.eventos()
            elif int(entrada_agendamento.get()) == 2:
                self.exibir_eventos()
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
      janela_eventos.title('PLANNER - AGENDAMENTO')
      janela_eventos.configure(bg = a)
      janela_eventos.geometry('400x300+200+200')
      texto_ae = Label(janela_eventos, text = '1 - Adicionar evento')
      texto_ae.place(x='50', y ='50')
      texto_me = Label(janela_eventos, text = '2 - Modificar evento')
      texto_me.place(x = '50', y = '70')
      texto_ev = Label(janela_eventos, text = '3 - Excluir evento')
      texto_ev.place(x = '50', y= '90')
      entrada_eventos = Entry(janela_eventos)
      entrada_eventos.place(x = '50', y = '120')
      def bt_click():      
        if int(entrada_eventos.get()) == 1:
          self.__agendar_evento()
        elif int(entrada_eventos.get()) == 2:
          self.__modificar_evento()
        elif int(entrada_eventos.get()) == 3:
          self.__excluir_evento()
        else:
          print(showerror("erro, digite uma das opções"))

          botao_enviar = Button(janela_eventos, text = 'enviar', command=bt_click)
          botao_enviar.place(x = '50', y = '150')

          botao_voltar = Button(janela_eventos, text = 'Voltar', command = menu_agendamento)
          botao_voltar.place(x = '90', y = '150')
          

          janela_eventos.mainloop()

    def exibir_eventos(self):
      janela_exibir = Tk()
      janela_exibir.title('PLANER _ AGENDAMENTO')
      janela_exibir.configure(bg = a)
      janela_exibir.geometry('400x300+200+200')
      texto_exibir =Label(janela_exibir, bg = a, text = '1 - Exibir eventos')
      texto_exibir.place(x = '50', y = '50')
      entrada_exibir = Entry(janela_exibir)
      entrada_exibir.place(x = '50', y = '120')

      botao_voltar =Button(janela_eventos, text = 'Voltar', command = eventos)
      botao_voltar.place(x = '90', y = '150')
      self.menu_agendamento()
      janela_exibir.mainloop()