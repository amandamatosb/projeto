from calendario import Calendario
from banco_eventos import *

evento = {}

class ErroUsuarioNaoDigitou(Exception):
    pass

class ErroNaoExisteCodigo(Exception):
    pass

class ErroNaoExisteEvento(Exception):
    pass

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
      try:
        if entrada.get() == '':
            raise ErroUsuarioNaoDigitou()

      except ErroUsuarioNaoDigitou:
        print(showerror('Erro', 'Escreva alguma coisa.'))
        entrada.delete(0, END)

      else:
        evento['nome'] = entrada.get().title()
        janela_evento.destroy()
        evento['data'] = self.__data_evento.definir_data()
        self.lugar_evento()

    img_proximo = PhotoImage(file='imagens/proximo.png')
    botao = Button(janela_evento, image=img_proximo, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='85', h='25')

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
      try:
        if entrada.get() == '':
            raise ErroUsuarioNaoDigitou()

      except ErroUsuarioNaoDigitou:
        print(showerror('Erro', 'Escreva alguma coisa.'))
        entrada.delete(0, END)

      else:
        evento['local'] = entrada.get().title()
        self.eventos.append((evento['código'], evento['nome'], evento['data'], evento['local']))
        cadastrar(evento['nome'], evento['data'], evento['local'])
        print(showinfo('Evento Marcado', 'Evento marcado com sucesso!'))
        janela_lugar.destroy()
        pass

    img_salvar = PhotoImage(file='imagens/salvar.png')
    botao = Button(janela_lugar, image=img_salvar, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='72', h='25')

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
      try:
        if int(codigo.get()) > len(self.eventos) or int(codigo.get()) <= 0:
          raise ErroNaoExisteCodigo()

        elif self.eventos[int(codigo.get()) - 1] == ' ':
          raise ErroNaoExisteEvento()

      except ErroNaoExisteCodigo:
        print(showerror('Erro', 'Não existe esse código no sistema.'))
        janela_excluir.destroy()
        self.excluir_evento()

      except ErroNaoExisteEvento:
        print(showerror('Evento Inexistente', 'Não existe esse evento.'))
        janela_excluir.destroy()
        self.excluir_evento()

      else:
        self.eventos.pop(int(codigo.get()) - 1)
        self.eventos.insert(int(codigo.get()) - 1, ' ')
        print(showinfo('Evento Removido', 'Evento excluído com sucesso!'))
        janela_excluir.destroy()
        pass

    def voltar():
      janela_excluir.destroy()

    img_enviar = PhotoImage(file='imagens/botao_enviar1.png')
    botao = Button(janela_excluir, image=img_enviar, command=bt_click, borderwidth=0)
    botao.place(x='309', y='311', w='72', h='25')

    img_voltar = PhotoImage(file='imagens/botao_voltar2.png')
    botao_voltar = Button(janela_excluir, image=img_voltar, command=voltar, borderwidth=0)
    botao_voltar.place(x='570', y='14', w='72', h='25')

    janela_excluir.mainloop()


