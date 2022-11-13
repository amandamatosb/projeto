from calendario import Calendario
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
        janela_evento.geometry('700x394')
        img = PhotoImage(file='imagens/add_nome.png')
        labelimage_inicio = Label(image=img)
        labelimage_inicio.pack(side=LEFT)
        entrada = Entry(janela_evento)
        entrada.place(x='270', y='175', w = '159', h = '21')

        def bt_click():
            evento['nome'] = entrada.get().title()
            janela_evento.destroy()
            evento['data'] = self.__data_evento.definir_data()
            self.lugar_evento()

        img_proximo = PhotoImage(file='imagens/proximo.png')
        botao = Button(janela_evento, image=img_proximo, command=bt_click, borderwidth=0)
        botao.place(x='309', y='311', w='85', h='33')

        janela_evento.mainloop()

    def lugar_evento(self):
        janela_lugar = Tk()
        janela_lugar.title('lugar.evento')
        janela_lugar.geometry('700x394')
        img = PhotoImage(file='imagens/add_local.png')
        labelimage_inicio = Label(image=img)
        labelimage_inicio.pack(side=LEFT)
        entrada = Entry(janela_lugar)
        entrada.place(x='270', y='175', w='159', h='21')

        def bt_click():
            evento['local'] = entrada.get().title()
            self.eventos.append((evento['código'], evento['nome'], evento['data'], evento['local']))
            cadastrar(evento['nome'], evento['data'], evento['local'])
            print(showinfo('evento marcado', 'evento marcado com sucesso!'))
            janela_lugar.destroy()
            pass

        img_salvar = PhotoImage(file='imagens/salvar.png')
        botao = Button(janela_lugar, image=img_salvar, command=bt_click, borderwidth=0)
        botao.place(x='309', y='311', w='72', h='33')

        janela_lugar.mainloop()

    def excluir_evento(self):
        janela_excluir = Tk()
        janela_excluir.title('excluir.evento')
        janela_excluir.geometry('700x394')
        img = PhotoImage(file='imagens/excluir_evento.png')
        labelimage_inicio = Label(image=img)
        labelimage_inicio.pack(side=LEFT)
        codigo = Entry(janela_excluir)
        codigo.place(x='270', y='175', w='159', h='21')

        def bt_click():
            if int(codigo.get()) > len(self.eventos) or int(codigo.get()) <= 0:
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

        def voltar():
            janela_excluir.destroy()

        img_enviar = PhotoImage(file='imagens/botao_enviar1.png')
        botao = Button(janela_excluir, image=img_enviar, command=bt_click, borderwidth=0)
        botao.place(x='309', y='311', w='72', h='33')

        img_voltar = PhotoImage(file='imagens/botao_voltar2.png')
        botao_voltar = Button(janela_excluir, image=img_voltar, command=voltar, borderwidth=0)
        botao_voltar.place(x='570', y='14', w='72', h='33')

        janela_excluir.mainloop()

