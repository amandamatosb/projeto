from calendario import Calendario
from evento import Evento
import os
import time
from tkinter import *

class Agendamento:
  def __init__(self):
    self.__data = Calendario() 
    self.__evento = Evento()

def menu_agendamento():
  janela_agendamento = Tk()
  janela_agendamento.title('Planner')
  janela_agendamento.configure(bg = a)
  janela_agendamento.geometry('400x300+200+200')
  texto_ag = Label(janela_agendamento, bg = a, fg = v, text = 'PLANNER - AGENDAMENTO')
  texto_ag.configure(font=('Times New Roman', 12, 'italic'))
  texto_ag.place(x = '150', y = '20')
  texto_eventos = Label(janela_agendamento, bg = a, fg = v, text = '1 - EVENTOS')
  texto_eventos.configure(font=('Times New Roman', 9,'italic'))
  texto_eventos.place(x = '50', y = '50')
  texto_agendamento = Label(janela_agendamento, bg = a, fg = v, text = '2 - VER AGENDAMENTOS')
  texto_agendamento.configure(font=('Times New Roman', 9, 'italic'))
  texto_agendamento.place(x = '50', y = '70')
  texto_voltar = label(janela_agendamento, bg = a, fg = v, text = '3 - VOLTAR')
  texto_voltar.configure(font=('Times Nes Roman', 9, 'italic'))
  texto_voltar.place(x = '50', y = '90')
  entrada_agendamento = Entry(janela_agendamento)
  entrada_agendamento.configure(font=('Times New Roman', 9))
  entrada_agendamento.place(x = '50', y = '140')
  ##
  def menu_agendamento1(self):
    try:
      os.system('clear')
      print('\033[0;49;35mPLANNER - AGENDA\033[m')
      print('1 - eventos \n2 - ver agendamento \n3 - voltar')
      resposta = int(input('-> '))
      if resposta == 1:
        self.adicionar_evento()
      elif resposta == 2:
        self.exibir_eventos()
      elif resposta == 3:
        os.system('clear')
        pass
      else:
        raise ValueError()

    except(ValueError, TypeError):
      print('\033[0;49;94m\n*mano que* \nvoltando...\033[m')
      time.sleep(4)
      self.menu_agendamento()
      
  def adicionar_evento(self):
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
        self.adicionar_evento()
      elif resposta == 2:
        self.__evento.modificar_evento()
        self.adicionar_evento()
      elif resposta == 3:
        self.__evento.excluir_evento()
        self.adicionar_evento()
      elif resposta == 4:
        self.menu_agendamento()
      else:
        raise ValueError()

    except(ValueError, TypeError):
      print('\033[0;49;94m\n*mano que* \nvoltando...\033[m')
      time.sleep(4)
      self.adicionar_evento()

  def exibir_eventos(self):
    os.system('clear')
    print('\033[0;49;35mPLANNER - AGENDAMENTO\033[m')
    for e in self.__evento.eventos:
      if e == ' ':
        pass
      else:
        print('-=' * 20)
        for chave, valor in e.items():
          print(f'{chave} = {valor} ', end = '')
          print()
    print('-=' * 20)  
    input('\nenter para voltar')
    self.menu_agendamento()
    