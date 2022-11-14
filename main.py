from usuario import Usuario
import time
import os
from usuario import usuarios
from tkinter import *
from tkinter.messagebox import *
from banco_usuarios import *
from banco_eventos import *

usuario = Usuario()


def comeco():
  janela = Tk()
  janela.title('planner')
  janela.geometry('700x394')
  img = PhotoImage(file='imagens/menuinicial.png')
  labelimage_inicio = Label(image=img)
  labelimage_inicio.pack(side= LEFT)
  entrada = Entry(janela)
  entrada.place(x='58', y='197')

  def ver_sistema():
    janela.destroy()
    janela_sistema = Tk()
    janela_sistema.title('banco.de.dados')
    janela_sistema.geometry('700x394')
    img_sistema = PhotoImage(file='imagens/sistema.png')
    labelimage_bd = Label(image=img_sistema)
    labelimage_bd.pack(side=LEFT)
    file = open('planner.txt', 'w+')
    file.write('INTEGRANTES DO PROJETO: ')
    file.write('\nAmanda Barros Matos')
    file.write('\nAna Beatriz Pimenta Coelho')
    file.write('\nLivia Gabriele Campos Lima')
    file.write('\nLarissa Cristina Nunes Guarates')
    file.write('\n\nNós somos do grupo Áries+Libra+Sagitário ')
    file.write('\n\nMatérias:')
    file.write('\nProgramação Orientada a Objetos')
    file.write('\nLinguagem de Programação')
    file.write('\nFundamentos e Análises de Sistema')
    file.write('\nBanco de Dados')
    file.seek(0, 0)
    file.seek(0, 0)
    file.close()

    def voltar():
      janela_sistema.destroy()
      comeco()

    img_voltar = PhotoImage(file='imagens/botao_voltar.png')
    botao_voltar = Button(janela_sistema, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='592', y='334', w='72', h='25')

    janela_sistema.mainloop()

  img_sis = PhotoImage(file='imagens/botao_sistema.png')
  botao_sistema = Button(janela, image=img_sis, command=ver_sistema, borderwidth=0)
  botao_sistema.place(x='476', y='40', w='189', h='25')

  def banco_de_dados():
    janela.destroy()
    banco()

  def banco():
    janela_banco = Tk()
    janela_banco.title('banco.de.dados')
    janela_banco.geometry('700x394')
    img_bd = PhotoImage(file='imagens/bancodedados.png')
    labelimage_bd = Label(image=img_bd)
    labelimage_bd.pack(side=LEFT)
    entrada = Entry(janela_banco)
    entrada.place(x='58', y='197')

    def enviar():
      try:
        if int(entrada.get()) == 1:
          janela_banco.destroy()
          banco_usuarios()
          banco()

        elif int(entrada.get()) == 2:
          janela_banco.destroy()
          banco_eventos()
          banco()

        else:
          raise ValueError()

      except(TypeError, ValueError):
        print(showerror('erro', 'digite correto'))
        entrada.delete(0, END)

    img_enviar = PhotoImage(file='imagens/botao_enviar.png')
    botao = Button(janela_banco, image=img_enviar, command=enviar, borderwidth=0)
    botao.place(x='58', y='257', w='72', h='25')

    def voltar():
      janela_banco.destroy()
      comeco()

    img_voltar = PhotoImage(file='imagens/botao_voltar.png')
    botao_voltar = Button(janela_banco, image=img_voltar, command = voltar, borderwidth=0)
    botao_voltar.place(x='592', y='334', w='72', h='25')

    janela_banco.mainloop()

  img_bd = PhotoImage(file='imagens/botao_bd.png')
  botao_bd = Button(janela, image=img_bd, command=banco_de_dados, borderwidth=0)
  botao_bd.place(x='480', y='334', w='178', h='25')

  def bt_click():
    try:
      if int(entrada.get()) == 1:
        janela.destroy()
        usuario.fazer_login()
        comeco()

      elif int(entrada.get()) == 2:
        janela.destroy()
        usuario.realizar_cadastro()
        comeco()

      else:
        raise ValueError()


    except (TypeError, ValueError):
      print(showerror('erro', 'digite correto'))
      entrada.delete(0, END)

  img_enviar = PhotoImage(file='imagens/botao_enviar.png')
  botao = Button(janela, image = img_enviar, command=bt_click, borderwidth=0)
  botao.place(x='58', y='257', w='72', h='25')

  janela.mainloop()

comeco()