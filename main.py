from usuario import Usuario
import time
import os
from usuario import usuarios
from tkinter import *
from tkinter.messagebox import *
from banco_de_dados import *

usuario = Usuario()

a = '#BCD2EE'

def comeco():
    try:
        janela = Tk()
        janela.title('planner')
        janela.configure(bg=a)
        janela.geometry('400x300+200+200')
        texto_inicio = Label(janela, bg=a, text='PLANNER - INÍCIO')
        texto_inicio.place(x='150', y='20')
        texto_login = Label(janela, bg=a, text='1 - login')
        texto_login.place(x='50', y='50')
        texto_cadastro = Label(janela, bg=a, text='2 - cadastro')
        texto_cadastro.place(x='50', y='70')
        texto_sistema = Label(janela, bg=a, text='3 - ver sobre o sistema')
        texto_sistema.place(x='50', y='90')
        texto_bd = Label(janela, bg=a, text='4 - banco de dados')
        texto_bd.place(x='50', y='110')
        entrada = Entry(janela)
        entrada.place(x='50', y='140')

        def bt_click():
            try:
                if int(entrada.get()) == 1:
                    if len(usuarios) == 0:
                        print(showerror("sem cadastros", "não há sequer um cadastro no nosso sistema, faça um!"))

                    else:
                        janela.destroy()
                        usuario.fazer_login()
                        comeco()

                elif int(entrada.get()) == 2:
                    janela.destroy()
                    usuario.realizar_cadastro()
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
                    file.seek(0, 0)
                    file.seek(0, 0)
                    file.close()
                    resposta_botao['text'] = ('(abra o arquivo de texto)')

                elif int(entrada.get()) == 4:
                    janela.destroy()
                    banco()
                    comeco()


                else:
                    raise ValueError()

            except (TypeError, ValueError):
                resposta_botao['text'] = ('*digite correto*')

        botao = Button(janela, text='enviar', command=bt_click)
        botao.place(x='50', y='170')

        resposta_botao = Label(janela, bg=a, text='')
        resposta_botao.place(x='50', y='200')
        janela.mainloop()

    except (TypeError, ValueError):
        print('\033[0;49;94m\n*calma ae mano, tá querendo ir aonde??* \nvoltando...\033[m')
        time.sleep(4)
        os.system('clear')
        comeco()


comeco()