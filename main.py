from usuario import Usuario
import time
import os
from usuario import usuarios 
from tkinter import *

usuario = Usuario()       
b = '#FFFFFF'
a = '#BCD2EE'
v = '#B22222'

def comeco():
  try:
    janela = Tk()
    janela.title('Planner')
    janela.configure(bg = a)
    janela.geometry('400x300+200+200')
    texto_inicio = Label(janela, bg = a, fg = v, text = 'PLANNER - INÍCIO')
    texto_inicio.place(x = '150', y = '20')
    texto_login = Label(janela, bg = a, fg = v, text = '1 - Login')
    texto_login.place(x = '50', y = '50')
    texto_cadastro = Label(janela, bg = a, fg = v, text = '2 - Cadastro')
    texto_cadastro.place(x = '50', y = '70')
    texto_sistema = Label(janela, bg = a, fg = v, text = '3 - Ver sobre o sistema')
    texto_sistema.place(x = '50', y = '90')
    texto_bd = Label(janela, bg = a, fg = v, text = '4 - Banco de dados')
    texto_bd.place(x = '50', y = '110')
    entrada = Entry(janela)
    entrada.place(x = '50', y = '140')

    def bt_click():
      try:
        if int(entrada.get()) == 1:
          if len(usuarios) == 0:
            texto_aviso = Label(janela, text = '*vish! não tem sequer um cadastro no nosso sistema* \nfaça um!')
            texto_aviso.place(x = '50', y = '210')
            time.sleep(4)
          else:
            usuario.fazer_login()
            os.system('clear')
            comeco()
            
        elif int(entrada.get()) == 2:
          usuario.realizar_cadastro()
          os.system('clear')
          comeco()
  
        elif int(entrada.get()) == 3:
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
          file.seek(0,0)
          file.seek(0,0)
          file.close()
          resposta_botao['text'] = ('\n(abra o arquivo de texto)')
  
        elif int(entrada.get()) == 4:
          if len(usuarios) == 0:
            print('\033[0;49;94m*vish! não tem sequer um cadastro no nosso sistema* \nfaça um!...\033[m')
            time.sleep(5)
            os.system('clear')
            comeco()
          else:
            os.system('clear')
            print('- BANCO DE DADOS DOS CADASTROS')
            print('1 - ver banco de dados \n2 - excluir algum usuário\n3 - voltar')
            resposta = int(input('-> '))
            if resposta == 1:
              usuario.ler_bd()
              os.system('clear')
              comeco()
              
            elif resposta == 2:
              usuario.excluir_dados()
              os.system('clear')
              comeco()
    
            elif resposta == 3:
              os.system('clear')
              comeco()
    
            else:
              raise ValueError()
  
        else:
          raise ValueError()

      except (TypeError, ValueError):
        resposta_botao['text'] = ('\n*digite correto*')
        time.sleep(4)
        os.system('clear')
        comeco()
        
    botao = Button(janela, text = 'enviar', foreground = v, command = bt_click)
    botao.place(x = '50', y = '170')

    resposta_botao = Label(janela, background = a, foreground = v, text = '')
    resposta_botao.place(x = '50', y = '200')
    janela.mainloop()

  except (TypeError, ValueError):
    print('\033[0;49;94m\n*calma ae mano, tá querendo ir aonde??* \nvoltando...\033[m')
    time.sleep(4)
    os.system('clear')
    comeco()

comeco()