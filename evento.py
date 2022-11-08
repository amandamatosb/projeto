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

        janela_evento.mainloop()

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

        janela_lugar.mainloop()

    def excluir_evento(self):
        janela_excluir = Tk()
        janela_excluir.title('nome.evento')
        janela_excluir.configure(bg=a)
        janela_excluir.geometry('400x300+200+200')
        texto_inicio = Label(janela_excluir, bg=a, text='- EXCLUINDO EVENTO -')
        texto_inicio.place(x='130', y='20')
        menu_nome = Label(janela_excluir, bg=a, text='*caso esqueça do código, digite 0 para voltar*')
        menu_nome.place(x='50', y='50')
        menu_nome = Label(janela_excluir, bg=a, text='código do evento: ')
        menu_nome.place(x='50', y='70')
        codigo = Entry(janela_excluir)
        codigo.place(x='50', y='100')

        def bt_click():
            if int(codigo.get()) == 0:
                janela_excluir.destroy()
                pass

            elif int(codigo.get()) > len(self.eventos) or int(codigo.get()) < 0:
                print(showerror('erro', 'não existe esse cógigo no sistema'))
                janela_excluir.destroy()
                self.excluir_evento()

            elif self.eventos[int(codigo.get()) - 1] == ' ':
                print(showerror('inexistente', 'não existe esse evento'))
                janela_excluir.destroy()
                self.excluir_evento()

            else:
                self.eventos.pop(int(codigo.get()) - 1)
                self.eventos.insert(int(codigo.get()) - 1, ' ')
                print(showinfo('evento removido', 'evento excluído com sucesso!'))
                janela_excluir.destroy()
                pass

        botao = Button(janela_excluir, text = 'enviar', command = bt_click)
        botao.place(x = '50', y = '130')
        janela_excluir.mainloop()