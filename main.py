from usuario import Usuario
import time
import os
from usuario import usuarios 

usuario = Usuario()       

def comeco():
  try:
    print('\033[0;49;35mPLANNER\033[m')
    print('1 - login \n2 - cadastro \n3 - ver sobre o sistema')
    resposta = int(input('-> '))

  except (TypeError, ValueError):
    print('\033[0;49;93mtivemos um problema :( , digite 1, 2 ou 3\033[m')
    time.sleep(4)
    os.system('clear')
    comeco()

  else:
    if resposta == 1:
      if len(usuarios) == 0:
        print('não será possível realizar login, pois não há nenhum cadastro em nosso sistema')
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
      
    else:
      print('\033[0;49;93mtivemos um problema :( , digite 1 ou 2\033[m')
      time.sleep(4)
      os.system('clear')
      comeco()

comeco()
