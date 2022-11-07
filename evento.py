import os
from calendario import Calendario
import time
from tkinter import *
from banco_eventos import *

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

        janela_evento = Tk()
        janela_evento.title('nome.evento')
        janela_evento.configure(bg=a)
        janela_evento.geometry('400x300+200+200')
        texto_inicio = Label(janela_evento, bg=a, text='- AGENDANDO EVENTO -')
        texto_inicio.place(x='130', y='20')
        menu_nome = Label(janela_evento, bg=a, text='nome: ')
        menu_nome.place(x='50', y='50')
        entrada = Entry(janela_evento)
        entrada.place(x='50', y='80')

        def bt_click():
            evento['nome'] = entrada.get()
            janela_evento.destroy()
            evento['data'] = self.__data_evento.definir_data()
            self.lugar_evento()

        botao = Button(janela_evento, text='próximo', command=bt_click)
        botao.place(x='50', y='110')

    def lugar_evento(self):
        janela_lugar = Tk()
        janela_lugar.title('nome.evento')
        janela_lugar.configure(bg=a)
        janela_lugar.geometry('400x300+200+200')
        texto_inicio = Label(janela_lugar, bg=a, text='- AGENDANDO EVENTO -')
        texto_inicio.place(x='130', y='20')
        menu_lugar = Label(janela_lugar, bg=a, text='local: ')
        menu_lugar.place(x='50', y='50')
        entrada1 = Entry(janela_lugar)
        entrada1.place(x='50', y='80')

        def bt_click1():
            evento['local'] = entrada1.get()
            self.eventos.append((evento['código'], evento['nome'], evento['data'], evento['local']))
            cadastrar(evento['nome'], evento['data'], evento['local'])
            print(showinfo('evento marcado', 'evento marcado com sucesso!'))
            janela_lugar.destroy()
            pass

        botao1 = Button(janela_lugar, text='salvar', command=bt_click1)
        botao1.place(x='50', y='110')


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
                print(showinfo('evento modificado', 'evento modificado com sucesso!'))

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
                print(showinfo('evento removido', 'evento excluído com sucesso!'))

        except(TypeError, ValueError):
            print('\033[0;49;94m\n*que? a não velho* \nvoltando...\033[m')
            time.sleep(4)
            self.excluir_evento()