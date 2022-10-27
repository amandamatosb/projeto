import os
from calendario import Calendario
evento = {}

class Evento:
  def __init__(self):
    self.__cod_evento = 0
    self.__nome_evento = ''
    self.__data_evento = Calendario()
    self.__local_evento = ''
    self.eventos = []

  def agendar_evento(self):
    self.__cod_evento += 1
    evento['código'] = self.__cod_evento
    os.system('clear')
    print('EVENTO')
    evento['nome'] = self.__nome_evento = input('nome: ')
    os.system('clear')
    evento['data'] = self.__data_evento.definir_data()
    os.system('clear')
    evento['local'] = self.__local_evento = input('local: ')

    self.eventos.append(evento.copy())

  def modificar_evento(self):
    os.system('clear')
    print('*caso esqueça do código do seu evento, digite 0 para a pergunta.')
    codigo = int(input('digite o código do evento que deseja modificar: '))

    if codigo == 0:
      for e in self.eventos:
        print('-=' * 30)
        for chave, valor in e.items():
          print(f'{chave} = {valor} ', end = '')
          print()

      print('-=' * 30)
      input('\nenter para voltar')
      self.modificar_evento()

    elif codigo > len(self.eventos):
      print('não existe esse código de evento no sistema.')
      print('1 - tentar novamente \n2 - voltar ao agendamento ')
      resposta = int(input('-> '))
      if resposta == 1:
        self.modificar_evento()
      else:
        pass
          
    else:
      self.eventos.pop(codigo-1)
      self.__cod_evento = codigo
      evento['código'] = self.__cod_evento
      os.system('clear')
      print('EVENTO')
      evento['nome'] = self.__nome_evento = input('nome: ')
      os.system('clear')
      evento['data'] = self.__data_evento.definir_data()
      os.system('clear')
      evento['local'] = self.__local_evento = input('local: ')

      self.eventos.append(evento.copy())

  def excluir_evento(self):
    os.system('clear')
    print('*caso esqueça do código do seu evento, digite 0 para a pergunta.')
    codigo = int(input('digite o código do evento que deseja excluir: '))
    if codigo == 0:
      for e in self.eventos:
        print('-=' * 30)
        for chave, valor in e.items():
          print(f'{chave} = {valor} ', end = '')
          print()
          
      print('-=' * 30)
      input('\nenter para voltar')
      self.excluir_evento()        
    elif codigo > len(self.eventos):
      print('não existe esse código de evento no sistema.')
      print('1 - tentar novamente \n2 - voltar ao agendamento ')
      resposta = int(input('-> '))
      if resposta == 1:
        self.excluir_evento()
      else:
        pass
        
    else:
      self.eventos.pop(codigo-1)