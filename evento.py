import os
from calendario import Calendario
import time
from tkinter import *

evento = {}

b = '#FFFFFF'
a = '#BCD2EE'
v = '#B22222'


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
    
        evento = Tk()
        evento.title('Nome do Evento')
        evento.configure(bg = a)
        evento.geometry('300x300+200+200')
    
        menu_nome = Label(text = 'Nome: ', bg = a, fg = v)
        menu_nome.place(x = 100, y = 70)
        entrada1 = Entry(evento)
        entrada1.place(x = 100, y = 100)
    
    def bit_click():
      evento.destroy()
      self.lugar_evento()
    
      botao = Button(evento, text = 'Próximo', command = bit_click)
      botao.place(x = 100, y = 130)
      
      evento['data'] = self.__data_evento.definir_data()
      os.system('clear')

     def lugar_evento(self):
       evento1 = Tk()
      evento1.title('Local do Evento')
      evento1.configure(bg = azul)
      evento1.geometry('300x300+200+200')
    
      menu_local = Label(evento1, text = 'Local: ', bg = azul, fg = vermelho)
      menu_local.place(x = 100, y = 70)
      entrada2 = Entry(evento1)
      entrada2.place(x = 100, y = 100)


    def bit_click1():  
      self.eventos.append(evento.copy())
    
    botao1 = Button(evento1, text = 'Salvar',command = bit_click1)
    botao1.place(x = 100, y = 130)


      self.eventos.append((evento['código'], evento['nome'],         evento['data'], evento['local']))

    def modificar_evento(self):
        try:
            os.system('clear')
            print('*caso esqueça do código do seu evento, digite 0 para a pergunta.')
            codigo = int(input('digite o código do evento que deseja modificar: '))

            if codigo == 0:
                for e in self.eventos:
                    print('-=' * 20)
                    for chave, valor in e.items():
                        print(f'{chave} = {valor} ', end='')
                        print()

                print('-=' * 20)
                input('\nenter para voltar')
                self.modificar_evento()

            elif codigo > len(self.eventos) or codigo < 0:
                print('\nnão existe esse código de evento no sistema.')
                print('1 - tentar novamente \n2 - voltar ao agendamento ')
                resposta = int(input('-> '))
                if resposta == 1:
                    self.modificar_evento()
                elif resposta == 2:
                    pass
                else:
                    raise ValueError()

            elif self.eventos[codigo - 1] == ' ':
                print('\nnão existe esse evento')
                input('\nenter para voltar')
                self.excluir_evento()

            else:
                self.__data_evento.datas.pop(codigo - 1)
                self.eventos.pop(codigo - 1)
                evento['código'] = codigo
                os.system('clear')
                print('EVENTO')
                evento['nome'] = self.__nome_evento = input('nome: ')
                os.system('clear')
                evento['data'] = self.__data_evento.definir_data()
                os.system('clear')
                evento['local'] = self.__local_evento = input('local: ')

                self.eventos.insert(codigo - 1, evento.copy())

        except:
            print('\033[0;49;94m\n*que? a não velho* \nvoltando...\033[m')
            time.sleep(4)
            self.modificar_evento()

    def excluir_evento(self):
        try:
            os.system('clear')
            print('*caso esqueça do código do seu evento, digite 0 para a pergunta.')
            codigo = int(input('digite o código do evento que deseja excluir: '))
            if codigo == 0:
                for e in self.eventos:
                    print('-=' * 20)
                    for chave, valor in e.items():
                        print(f'{chave} = {valor} ', end='')
                        print()

                print('-=' * 20)
                input('\nenter para voltar')
                self.excluir_evento()

            elif codigo > len(self.eventos) or codigo < 0:
                print('\nnão existe esse código de evento no sistema.')
                print('1 - tentar novamente \n2 - voltar ao agendamento ')
                resposta = int(input('-> '))
                if resposta == 1:
                    self.excluir_evento()
                elif resposta == 2:
                    pass
                else:
                    raise ValueError()

            elif self.eventos[codigo - 1] == ' ':
                print('\nnão existe esse evento')
                input('\nenter para voltar')
                self.excluir_evento()

            else:
                self.eventos.pop(codigo - 1)
                self.eventos.insert(codigo - 1, ' ')

        except(TypeError, ValueError):
            print('\033[0;49;94m\n*que? a não velho* \nvoltando...\033[m')
            time.sleep(4)
            self.excluir_evento()


agendar_evento = Evento()
evento.nome_evento()