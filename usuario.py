import os
import time
from agendamento import Agendamento
global eventos_usuarios
import re 
import sqlite3
usuarios = []
email = []
eventos_usuarios = {}

class Usuario:
  def __init__(self):
    self.__nome = ''
    self.__email = ''
    self.__senha = ''

  def realizar_cadastro(self):
    os.system('clear')
    print('\033[0;49;96m - CADASTRO\033[m')
    self.__nome = input('\033[0;49;96mnome: \033[m').title()
    while True:
      os.system('clear')
      print('\033[0;49;96m - CADASTRO\033[m')
      print(f'\033[0;49;96mnome:\033[m {self.__nome}')
      try:
        self.__email = input('\033[0;49;96memail: \033[m').lower()
        if self.__email[-10:] != '@gmail.com':
          raise ValueError()
        else:
          break
          
      except(ValueError):
        print('\033[0;49;31m/email inválido!/\033[m')
        input('enter para tentar novamente')
      
    while True: 
      os.system('clear')
      print('\033[0;49;96m - CADASTRO\033[m')
      print(f'\033[0;49;96mnome:\033[m {self.__nome}')
      print(f'\033[0;49;96memail:\033[m {self.__email}')
      try:
        self.__senha = input('\033[0;49;96msenha: \033[m')
        if (len(self.__senha)<8): 
          raise ValueError()
        elif not re.search("[a-z]", self.__senha): 
          raise ValueError()
        elif not re.search("[A-Z]", self.__senha): 
          raise ValueError()
        elif not re.search("[0-9]", self.__senha): 
          raise ValueError()
        elif not re.search("[!#$%&()*+,-./:;<=>?@[\]^_`{|}~']", self.__senha): 
          raise ValueError()
        elif re.search("\s", self.__senha): 
          raise ValueError()
        else: 
          break
          
      except(ValueError):
        print('\033[0;49;31m/senha fraca!/\033[m')
        print('\nAVISO: \n mínimo 8 caracteres \n letras minúsculas [az] \n letras maiúsculas [AZ] \n pelo menos 1 número ou dígito entre [0-9] \n pelo menos 1 caractere especial')
        input('\nenter para tentar novamente')
    
    email.append(self.__email)
    usuarios.extend((self.__nome, self.__email, self.__senha))
    self.bancodedados()

  def fazer_login(self):
    os.system('clear')
    print('\033[0;49;96m - LOGIN\033[m')
    email_digitado = input('\033[0;49;96memail: \033[m')
    if email_digitado in email:
      self.senha_login(email_digitado)

    else:
      print('\033[0;49;31m/email não existente/\033[m')
      input('enter para tentar novamente')
      self.fazer_login()

  def senha_login(self, email_digitado):
    os.system('clear')
    print('\033[0;49;96m - LOGIN \033[m')
    print('\033[0;49;96memail:\033[m', email_digitado)
    senha_digitada = input('\033[0;49;96msenha: \033[m')
    
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
      print('1 - dados do usuário \n2 - agenda \n3 - sair')
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
      print('\033[0;49;94m\n*eita mano, deu erro aq* \nvoltando...\033[m')
      time.sleep(4)
      os.system('clear')
      self.escolher_funcoes(email_digitado, rsenha)
      
  def exibir_dados(self, email_digitado, rsenha):
    os.system('clear')
    rsenha = usuarios.index(email_digitado)
    print('\033[0;49;34m - DADOS DO USUÁRIO\033[m')
    print('\033[0;49;34mnome:\033[m', usuarios[rsenha - 1])
    print('\033[0;49;34memail:\033[m', usuarios[rsenha])
    print('\033[0;49;34msenha:\033[m', usuarios[rsenha + 1], '\n')

    try:
      input('enter para voltar')
      self.escolher_funcoes(email_digitado, rsenha)

    except(ValueError, TypeError):
      print('\033[0;49;94m\n*eita mano, deu erro aq* \nvoltando...\033[m')
      time.sleep(4)
      os.system('clear')
      self.exibir_dados(email_digitado, rsenha)

  def consultar_agendamento(self, email_digitado):
    if email_digitado not in eventos_usuarios.keys():
      eventos_usuarios[email_digitado] = Agendamento()
      self.consultar_agendamento(email_digitado)
    else:
      eventos_usuarios[email_digitado].menu_agendamento()

  def bancodedados(self):
   #conectando
    conexao = sqlite3.connect('usuarios.db')
    
    #definindo um cursor
    cursor = conexao.cursor()
    
    #criando tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
    );
    """)
    
    #inserindo dados
    cursor.execute("""
    INSERT INTO usuarios (nome, email)
    VALUES (?,?)
    """, (self.__nome, self.__email))
    
    conexao.commit()
    
    #desconectando
    conexao.close()
    
  def ler_bd(self):
    #conectando
    conexao = sqlite3.connect('usuarios.db')
    
    #definindo um cursor
    cursor = conexao.cursor()

    print('\ndeu tudo certo *-*\n')
    
    #lendo dados
    cursor.execute("""
    SELECT * FROM usuarios;
    """)
    
    for linha in cursor.fetchall():
        print(linha)
    
    #desconectando
    conexao.close()

    input('\nenter para voltar')
    
  def excluir_dados(self):
    #conectando
    conexao = sqlite3.connect('usuarios.db')
    
    #definindo um cursor
    cursor = conexao.cursor()

    id_usuario = int(input('\nid do usuário: '))
    
    cursor.execute("""
    DELETE FROM usuarios
    WHERE id = ?
    """, (id_usuario,))

    conexao.commit()
    
    print('\nexcluido com sucesso *-*')
    
    #desconectando
    conexao.close()

    input('\nenter para voltar')
      