import os
import time
from agendamento import Agendamento
from tkinter.messagebox import *
global eventos_usuarios
import re
from tkinter import *
from banco_usuarios import *
import sqlite3
import tkinter.messagebox as tkMessageBox
import tkinter.messagebox

usuarios = []
email = []
eventos_usuarios = {}

a = '#BCD2EE'


class Usuario:
  def __init__(self):
    self.__nome = ''
    self.__email = ''
    self.__senha = ''

  def realizar_cadastro(self):
    janela_cadastro = Tk()
    janela_cadastro.title('planner.cadastro')
    janela_cadastro.geometry('700x394')
    img = PhotoImage(file='imagens/cadastro.png')
    labelimage_cadastro = Label(image=img)
    labelimage_cadastro.pack(side=LEFT)
    entrada = Entry(janela_cadastro)
    entrada.place(x='270', y='130', w = '159', h = '21')
    entrada1 = Entry(janela_cadastro)
    entrada1.place(x='270', y='189', w = '159', h = '21')
    entrada2 = Entry(janela_cadastro, show = '*')
    entrada2.place(x='270', y='250', w = '159', h = '21')

    def bt_click():
      self.__nome = entrada.get().title()
      while True:
        self.__email = entrada1.get().lower()
        if self.__email[-10:] != '@gmail.com':
          print(showinfo("email inválido", "use @gmail.com para validar o email"))
          janela_cadastro.destroy()
          self.realizar_cadastro()

        elif self.__email in email:
          print(showinfo("email existente", "já existe esse email no sistema"))
          janela_cadastro.destroy()
          self.realizar_cadastro()

        else:
          break

      while True:
        self.__senha = entrada2.get()
        if (len(self.__senha) < 8) or not re.search("[a-z]", self.__senha) or not re.search("[A-Z]", self.__senha)   or not re.search( "[0-9]", self.__senha) or not re.search("[!#$%&()*+,-./:;<=>?@[\]^_`{|}~']", self.__senha) or re.search("\s", self.__senha):
          print(showinfo("senha fraca", "SENHA FRACA!\n\nAVISO: \n mínimo 8 caracteres \n letras minúsculas [az] \n letras maiúsculas [AZ] \n pelo menos 1 número ou dígito entre [0-9] \n pelo menos 1 caractere especial"))
          janela_cadastro.destroy()
          self.realizar_cadastro()

        else:
          break

      email.append(self.__email)
      usuarios.extend((self.__nome, self.__email, self.__senha))
      cadastrar(self.__nome, self.__email)

      print(showinfo('cadastro realizado', 'cadastro realizado com sucesso'))
      janela_cadastro.destroy()

    img_enviar = PhotoImage(file='imagens/botao_enviar1.png')
    botao = Button(janela_cadastro, image=img_enviar, command=bt_click, borderwidth=0)
    botao.place(x='312', y='321', w='72', h='33')
    janela_cadastro.mainloop()

  def fazer_login(self):
    janela_login = Tk()
    janela_login.title('planner.login')
    janela_login.geometry('700x394')
    img = PhotoImage(file='imagens/login.png')
    labelimage_login = Label(image=img)
    labelimage_login.pack(side=LEFT)
    entrada = Entry(janela_login)
    entrada.place(x='270', y='175', w = '159', h = '21')

    def bt_click():
      email_digitado = entrada.get()
      if email_digitado in email:
        janela_login.destroy()
        self.senha_login(email_digitado)

      else:
        resultado = tkinter.messagebox.askquestion("email não existe", "você não tem cadastro, deseja se cadastrar? ", icon="warning")
        if resultado == 'yes':
          janela_login.destroy()
        else:
          janela_login.destroy()
          self.fazer_login()

    img_enviar = PhotoImage(file='imagens/botao_enviar1.png')
    botao = Button(janela_login, image=img_enviar, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='72', h='33')

    janela_login.mainloop()

  def senha_login(self, email_digitado):
    janela_loginsenha = Tk()
    janela_loginsenha.title('planner.login')
    janela_loginsenha.geometry('700x394')
    img = PhotoImage(file='imagens/login_senha.png')
    labelimage_login = Label(image=img)
    labelimage_login.pack(side=LEFT)
    entrada = Entry(janela_loginsenha, show= '*')
    entrada.place(x='270', y='175', w='159', h='21')

    def bt_click():
      senha_digitada = entrada.get()
      if senha_digitada != usuarios[rsenha + 1]:
        resultado = tkinter.messagebox.askquestion("senha errada", "você deseja tentar novamente? ",
                                                   icon="warning")
        if resultado == 'yes':
          janela_loginsenha.destroy()
          self.senha_login(email_digitado)
        else:
          janela_loginsenha.destroy()

      else:
        print(showinfo("login feito", "BEM VINDO AO PLANNER"))
        janela_loginsenha.destroy()
        self.escolher_funcoes(email_digitado, rsenha)

    img_enviar = PhotoImage(file='imagens/botao_enviar1.png')
    botao = Button(janela_loginsenha, image=img_enviar, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='72', h='33')

    rsenha = usuarios.index(email_digitado)

    janela_loginsenha.mainloop()

  def escolher_funcoes(self, email_digitado, rsenha):
    janela_escolher_funcoes = Tk()
    janela_escolher_funcoes.title('planner.escolha')
    janela_escolher_funcoes.geometry('700x394')
    img = PhotoImage(file='imagens/planner.png')
    labelimage_inicio = Label(image=img)
    labelimage_inicio.pack(side=LEFT)
    entrada = Entry(janela_escolher_funcoes)
    entrada.place(x='58', y='197')

    def enviar():
      if int(entrada.get()) == 1:
        janela_escolher_funcoes.destroy()
        self.exibir_dados(email_digitado, rsenha)
        self.escolher_funcoes(email_digitado, rsenha)
      elif int(entrada.get()) == 2:
        janela_escolher_funcoes.destroy()
        self.consultar_agendamento(email_digitado)
        self.escolher_funcoes(email_digitado, rsenha)
      else:
        print(showerror("erro", 'eita mano deu erro aqui'))
        janela_escolher_funcoes.destroy()
        self.escolher_funcoes(email_digitado, rsenha)

    img_enviar = PhotoImage(file='imagens/botao_enviar.png')
    botao = Button(janela_escolher_funcoes, image=img_enviar, command=enviar, borderwidth=0)
    botao.place(x='58', y='257', w='72', h='33')

    def voltar():
      janela_escolher_funcoes.destroy()

    img_voltar = PhotoImage(file='imagens/botao_voltar.png')
    botao_voltar = Button(janela_escolher_funcoes, image=img_voltar, command = voltar, borderwidth=0)
    botao_voltar.place(x='592', y='334', w='72', h='33')

    janela_escolher_funcoes.mainloop()

  def exibir_dados(self, email_digitado, rsenha):
    janela_exibir_dados = Tk()
    janela_exibir_dados.title('dados.do.usuario')
    janela_exibir_dados.geometry('700x394')
    img = PhotoImage(file='imagens/dados_usuario.png')
    labelimage_dados = Label(image=img)
    labelimage_dados.pack(side=LEFT)
    texto_nome = Label(janela_exibir_dados, bg ='#FBF8F0', text=(usuarios[rsenha - 1]))
    texto_nome.place(x='255', y='146')
    texto_email = Label(janela_exibir_dados, bg ='#FBF8F0',text=(usuarios[rsenha]))
    texto_email.place(x = '255', y = '186')
    texto_senha = Label(janela_exibir_dados, bg ='#FBF8F0', text=(usuarios[rsenha + 1]))
    texto_senha.place(x='255', y='226')

    def bt_click():
      janela_exibir_dados.destroy()

    img_voltar = PhotoImage(file='imagens/botao_voltar2.png')
    botao = Button(janela_exibir_dados, image=img_voltar, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='72', h='33')

    janela_exibir_dados.mainloop()

  def consultar_agendamento(self, email_digitado):
    if email_digitado not in eventos_usuarios.keys():
      eventos_usuarios[email_digitado] = Agendamento()
      self.consultar_agendamento(email_digitado)
    else:
      eventos_usuarios[email_digitado].menu_agendamento()