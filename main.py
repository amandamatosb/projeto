from usuario import Usuario
import time
import os
from usuario import usuarios 

usuario = Usuario()       

def comeco():
  try:
    print('\033[0;49;35mPLANNER - INÍCIO\033[m')
    print('1 - login \n2 - cadastro \n3 - ver sobre o sistema')
    resposta = int(input('-> '))
    if resposta == 1:
      if len(usuarios) == 0:
        print('\033[0;49;94m\n*vish! não tem sequer um cadastro no nosso sistema* \n voltando...\033[m')
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
      file.write('\nINTEGRANTES DO PROJETO: ')
      file.write('\n Amanda Barros Matos')
      file.write('\n Ana Beatriz Pimenta Coelho')
      file.write('\n Livia Gabriele Campos Lima')
      file.write('\n Larissa Cristina Nunes Guarates')
      file.write('\n\nNós somos do grupo Áries+Libra+Sagitário ')
      file.write('\n\nMATÉRIAS:')
      file.write('\n Programação Orientada a Objetos')
      file.write('\n Linguagem de Programação')
      file.write('\n Fundamentos e Análises de Sistema')
      file.write('\n Banco de Dados')
      file.seek(0,0)
      print(file.read())
      file.seek(0,0)
      file.close()
      print('\n(arquivo de texto)')
      input('\nenter para voltar;)')
      os.system('clear')
      comeco()
      
    else:
      raise ValueError()

  except (TypeError, ValueError):
    print('\033[0;49;94m\n*digite uma das opções* \n voltando...\033[m')
    time.sleep(4)
    os.system('clear')
    comeco()

comeco()
