import os
import time
from agendamento import Agendamento
global eventos_usuarios
usuarios = []
email = []
eventos_usuarios = {}

class Usuario:
  def __init__(self):
    self.__nome = ''
    self.__email = ''
    self.__senha = ''
    self.__cidade = ''
    self.__estado = ''
    self.__logradouro = ''
    self.__bairro =  ''
    self.__numero = '' 

  def realizar_cadastro(self):
    os.system('clear')
    print('- CADASTRO')
    self.__nome = input('nome: ').title()
    self.__email = input('email: ') 
    self.__senha = input('senha: ')
    print()
    print('- ENDEREÇO')
    self.__cidade = input('cidade: ').title()
    self.__estado = input('sigla do estado: ').upper()
    self.__logradouro = input('logradouro: ').title()
    self.__bairro = input('bairro: ').title()
    self.__numero = input('número residencial: ')
    print('\033[0;49;92m/cadastro finalizado/\033[m')
    time.sleep(5)

    email.append(self.__email)
    usuarios.extend((self.__nome, self.__email, self.__senha, self.__cidade, self.__estado, self.__logradouro, self.__bairro, self.__numero))

  def fazer_login(self):
    os.system('clear')
    print(' - LOGIN ')
    email_digitado = input('email: ')
    if email_digitado in email:
      self.senha_login(email_digitado)

    else:
      print('\033[0;49;31m/email não existente/\033[m')
      input('enter para tentar novamente')
      self.fazer_login()

  def senha_login(self, email_digitado):
    os.system('clear')
    print(' - LOGIN ')
    print('email:', email_digitado)
    senha_digitada = input('senha: ')
    
    rsenha = usuarios.index(email_digitado)
    
    if senha_digitada != usuarios[rsenha + 1]:
      print("\033[0;49;31m/senha incorreta/\033[m")
      input('enter para tentar novamente')
      self.senha_login(email_digitado)

    else:
      print("\033[0;49;32m/senha correta/\033[m")
      time.sleep(5)
      self.escolher_funcoes(email_digitado, rsenha)

  def escolher_funcoes(self, email_digitado, rsenha):
    try:
      os.system('clear')
      print('\033[0;49;35mPLANNER - BEM VINDO\033[m')
      print('1 - exibir dados do usuário \n2 - agenda \n3 - voltar')
      resposta = int(input('-> '))
      if resposta == 1:
        self.exibir_dados(email_digitado, rsenha)
      elif resposta == 2:
        os.system('clear')
        self.consultar_agendamento(email_digitado)
        self.escolher_funcoes(email_digitado, rsenha)
      elif resposta == 3:
        pass
      else:
        raise ValueError()
        
    except(TypeError, ValueError):
      print('\033[0;49;93mtivemos um problema :( , digite 1, 2 ou 3\033[m')
      time.sleep(4)
      os.system('clear')
      self.escolher_funcoes(email_digitado, rsenha)
      
  def exibir_dados(self, email_digitado, rsenha):
    os.system('clear')
    rsenha = usuarios.index(email_digitado)
    print('    - DADOS DO USUÁRIO -  ')
    print('\033[0;49;34mnome:\033[m', usuarios[rsenha - 1])
    print('\033[0;49;34memail:\033[m', usuarios[rsenha])
    print('\033[0;49;34msenha:\033[m', usuarios[rsenha + 1], '\n')
    print('       - ENDEREÇO -  ')
    print('\033[0;49;34mcidade:\033[m', usuarios[rsenha + 2])
    print('\033[0;49;34mestado:\033[m', usuarios[rsenha + 3])
    print('\033[0;49;34mlogradouro:\033[m', usuarios[rsenha + 4])
    print('\033[0;49;34mbairro:\033[m', usuarios[rsenha + 5])
    print('\033[0;49;34mnúmero residencial:\033[m', usuarios[rsenha + 6])

    try:
      print('\033[0;49;35m\nPLANNER\033[m')
      print('1 - agenda \n2 - voltar')
      resposta = int(input('-> '))
      if resposta == 1:
        self.consultar_agendamento(email_digitado)
        self.escolher_funcoes(email_digitado, rsenha)
      elif resposta == 2:
        self.escolher_funcoes(email_digitado, rsenha)
      else:
        raise ValueError()

    except(ValueError, TypeError):
      print('\033[0;49;93mtivemos um problema :( , digite 1 ou 2\033[m')
      time.sleep(4)
      os.system('clear')
      self.exibir_dados(email_digitado, rsenha)

  def consultar_agendamento(self, email_digitado):
    if email_digitado not in eventos_usuarios.keys():
      eventos_usuarios[email_digitado] = Agendamento()
      self.consultar_agendamento(email_digitado)
    else:
      eventos_usuarios[email_digitado].menu_agendamento()
      