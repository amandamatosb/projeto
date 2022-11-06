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
        janela_agendamento.title('agendamento')
        janela_agendamento.configure(bg=a)
        janela_agendamento.geometry('400x300+200+200')
        texto_ag = Label(janela_agendamento, bg=a, text='PLANNER - AGENDAMENTO')
        texto_ag.place(x='130', y='20')
        texto_eventos = Label(janela_agendamento, bg=a, text='1 - eventos')
        texto_eventos.place(x='50', y='50')
        texto_agendamento = Label(janela_agendamento, bg=a, text='2 - ver agendamentos')
        texto_agendamento.place(x = '50', y='70')
        texto_voltar = Label(janela_agendamento, bg=a, text='3 - voltar')
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
      janela_eventos.title('Agendamento')
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
          botao_voltar.place(x = '90'  , y='150')
          

          janela_eventos.mainloop()
          
          try:
            os.system('clear')
            print('\033[0;49;35mPLANNER - EVENTO\033[m')
            print('1 - adicionar evento \n2 - modificar evento \n3 - excluir evento \n4 - voltar')
            resposta = int(input('-> '))
            if resposta == 1:
              self.__evento.agendar_evento()
              os.system('clear')
              print('- evento marcado')
              input('enter para voltar')
              self.eventos()
            elif resposta == 2:
              self.__evento.modificar_evento()
              self.eventos()
            elif resposta == 3:
              self.__evento.excluir_evento()
              self.eventos()
            elif resposta == 4:
              self.menu_agendamento()
            else:
             raise ValueError()
          except(ValueError, TypeError):
            print('\033[0;49;94m\n*mano que* \nvoltando...\033[m')
            time.sleep(4)
            self.eventos()

    def exibir_eventos(self):
        os.system('clear')
        print('\033[0;49;35mPLANNER - AGENDAMENTO\033[m')
        for e in self.__evento.eventos:
            if e == ' ':
                pass
            else:
                print('-=' * 20)
                for chave, valor in e.items():
                    print(f'{chave} = {valor} ', end='')
                    print()
        print('-=' * 20)
        input('\nenter para voltar')
        self.menu_agendamento()
