import calendar
import os
from datetime import date, time, datetime, timedelta
import time
from tkinter import *

b = '#FFFFFF'
a = '#BCD2EE'
v = '#B22222'


class Calendario:
  def __init__(self):
    self.__dia = None
    self.__mes = None
    self.__ano = None
    self.__hora = None
    self.datas = []

  def definir_data():
##akali e larissa que tao fazendo se tiver errado sorry a gente nao sabe direito
    def menu_agendamento(self):
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

  def definir_data1(self)
    while True:
      os.system('clear')
      self.__ano = input('ano(YYY): ')
      try:
        ano = datetime.strptime(self.__ano, '%Y').date()
      except(ValueError, TypeError):
        print('\033[0;49;94m\n*digite certo pls* \nvoltando...\033[m')
        time.sleep(4)
      else:
        break

    ano = int(self.__ano)
    
    while True:
      os.system('clear')
      print(calendar.calendar(ano))
      self.__mes = input('número do mês: ')
      try:
        mes = datetime.strptime(self.__mes, '%m').date()
      except(ValueError, TypeError):
        print('\033[0;49;94m\n*digite certo pls* \nvoltando...\033[m')
        time.sleep(4)
      else:
        break

    mes = int(self.__mes)
    
    while True:
      os.system('clear')
      print(calendar.month(ano, mes))
      self.__dia = input('dia: ')
      try:
        dia = datetime.strptime(self.__dia, '%d').date()
      except(ValueError, TypeError):
        print('\033[0;49;94m\n*digite certo pls* \nvoltando...\033[m')
        time.sleep(4)
      else:
        break

    dia = int(self.__dia)

    while True:
      os.system('clear')
      print(f'{dia}/{mes}/{ano}')
      self.__hora = input('hora(hh:mm): ')
      try:
        hora = datetime.strptime(self.__hora, '%H:%M').date()
      except(ValueError, TypeError):
        print('\033[0;49;94m\n*digite certo pls* \nvoltando...\033[m')
        time.sleep(4)
      else:
        break

    hora = str(self.__hora)
    
    data = f"{dia}/{mes}/{ano} às {hora}"
    os.system('clear')
    self.data_ocupada(data)
    return self.datas[len(self.datas)-1]

  def data_ocupada(self, data):
    if data not in self.datas:
      self.datas.append(data)

    else:
      os.system('clear')
      print(f'já tem evento marcado para {data}, mude a data...')
      time.sleep(5)
      self.definir_data()
