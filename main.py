from usuario import Usuario
import time
import os
from usuario import usuarios 

usuario = Usuario()       

def comeco():
  try:
    print('\033[0;49;35mPLANNER - INÍCIO\033[m')
    print('1 - login \n2 - cadastro \n3 - ver sobre o sistema\n4 - banco de dados')
    resposta = int(input('-> '))
    if resposta == 1:
      if len(usuarios) == 0:
        print('\033[0;49;94m\n*vish! não tem sequer um cadastro no nosso sistema* \nvoltando...\033[m')
        time.sleep(5)
        os.system('clear')
        comeco()
      else:
        usuario.fazer_login()
        os.system('clear')
        comeco()
      
    elif resposta == 2:
      usuario.realizar_cadastro()
      os.system('clear')
      comeco()

    elif resposta == 3:
      file = open('planner.txt', 'w+')
      file.write('INTEGRANTES DO PROJETO: ')
      file.write('\nAmanda Barros Matos')
      file.write('\nLivia Gabriele Campos Lima')
      file.write('\nLarissa Cristina Nunes Guarates')
      file.write('\n\nNós somos do grupo Áries+Libra ')
      file.write('e estamos desenvolvendo esse sistema de Planner')
      file.write('\n\nMatérias:')
      file.write('\nProgramação Orientada a Objetos')
      file.write('\nLinguagem de Programação')
      file.write('\nFundamentos e Análises de Sistema')
      file.write('\nBanco de Dados')
      file.seek(0,0)
      print(file.read())
      file.seek(0,0)
      file.close()
      print('\n(arquivo de texto)')
      input('\nenter para voltar;)')
      os.system('clear')
      comeco()

    elif resposta == 4:
      if len(usuarios) == 0:
        print('\033[0;49;94m\n*vish! não tem sequer um cadastro no nosso sistema* \nvoltando...\033[m')
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
    print('\033[0;49;94m\n*calma ae mano, tá querendo ir aonde??* \nvoltando...\033[m')
    time.sleep(4)
    os.system('clear')
    comeco()

comeco()
