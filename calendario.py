import calendar
import os
from datetime import date, time, datetime, timedelta
import time

class Calendario:
  def __init__(self):
    self.__dia = None
    self.__mes = None
    self.__ano = None
    self.__hora = None
    self.datas = []

  def definir_data(self):
    os.system('clear')
    print('\033[7;97;35m             IMPORTANTE!                 \033[m')
    print('\033[7;97;35m tipos de dados que aceitamos:           \033[m')
    print('\033[7;97;35m ano -> YYYY                             \033[m')
    print('\033[7;97;35m mês -> 1-12                             \033[m')
    print('\033[7;97;35m dia -> dias disponíveis no mês escolhido\033[m')
    print('\033[7;97;35m horas -> hh:mm                          \033[m')
    input('\033[7;97;35m       enter para continuar              \033[m')
    
    while True:
      os.system('clear')
      self.__ano = input('ano: ')
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
    print('data:', data)
    
    time.sleep(3)
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
