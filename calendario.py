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
    os.system('clear')
    
    self.__ano = int(input('ano: '))
    print(calendar.calendar(self.__ano))

    self.__mes = int(input('número do mês: '))
    os.system('clear')
    print(calendar.month(self.__ano, self.__mes))

    self.__dia = int(input('dia: '))
    os.system('clear')

    self.__hora = input('hora(hh:mm): ')

    data = f"{self.__dia}/{self.__mes}/{self.__ano} às {self.__hora}"
    datetime.strptime(data, "%d/%m/%Y às %H:%M")
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
