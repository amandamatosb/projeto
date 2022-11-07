from datetime import date
from tkinter import *
from tkcalendar import DateEntry
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import tkinter.messagebox
from tkinter.messagebox import *

a = '#BCD2EE'


class Calendario:
    def __init__(self):
        self.datas = []

    def definir_data(self):
        janela_calendario = Tk()
        janela_calendario.title('data')
        janela_calendario.configure(bg=a)
        janela_calendario.geometry('500x300+200+200')

        class MyDateEntry(DateEntry):
            def __init__(self, master=None, **kw):
                DateEntry.__init__(self, master=None, **kw)
                self._top_cal.configure(bg='black', bd=1)
                tk.Label(self._top_cal, bg='gray90', anchor='w',
                         text='hoje: %s' % date.today().strftime('%d/%m/%Y')).pack(fill='x')

                texto = Label(janela_calendario, bg=a, text='- escolha a data -')
                texto.place(x='50', y='170')

        def bt_click():
            resultado = tkinter.messagebox.askquestion("confirmação", "confirma essa data?", icon="warning")
            if resultado == 'yes':
                global data
                data = ajustes.get_date().strftime('%d/%m/%Y')
                janela_calendario.destroy()
                self.definir_horario()

            else:
                janela_calendario.destroy()
                self.definir_data()

        botao = Button(janela_calendario, text='enviar', command=bt_click)
        botao.place(x='50', y='200')

        # criando a entrada e mudando os ajustes de cor do calendario
        ajustes = MyDateEntry(janela_calendario, year=2022, month=11, day=9,
                              selectbackground='gray80',
                              selectforeground='black',
                              normalbackground='white',
                              normalforeground='black',
                              background='gray90',
                              foreground='black',
                              bordercolor='gray90',
                              othermonthforeground='gray50',
                              othermonthbackground='white',
                              othermonthweforeground='gray50',
                              othermonthwebackground='white',
                              weekendbackground='white',
                              weekendforeground='black',
                              headersbackground='white',
                              headersforeground='gray70', locale='pt_br')
        ajustes.pack()
        janela_calendario.mainloop()
        return self.datas[len(self.datas) - 1]

    def definir_horario(self):
        janela_horario = Tk()
        janela_horario.title('data')
        janela_horario.configure(bg=a)
        janela_horario.geometry('400x300+200+200')

        lb_horario = Listbox()
        lb_horario.pack(side=LEFT, fill="both")
        sb = Scrollbar()
        sb.pack(side=LEFT, fill="y")
        sb.configure(command=lb_horario.yview)
        lb_horario.configure(yscrollcommand=sb.set)

        for h in range(0, 24):
            for m in range(0, 60, 5):
                lb_horario.insert(END, f'{h}:{m}')

        def bt_click():
            resultado = tkinter.messagebox.askquestion("confirmação", "confirma este horário?", icon="warning")
            if resultado == 'yes':
                horario = str(lb_horario.get(ACTIVE))
                data_do_evento = f"{data} às {horario}"
                self.data_ocupada(data_do_evento)
                janela_horario.destroy()

            else:
                janela_horario.destroy()
                self.definir_horario()

        botao = Button(janela_horario, text='enviar', command=bt_click)

        texto = Label(janela_horario, bg=a, text=' - selecione o horário -')
        texto.place(x='180', y='20')
        botao.place(x='185', y='50')

        janela_horario.mainloop()

    def data_ocupada(self, data_do_evento):
        if data_do_evento not in self.datas:
            self.datas.append(data_do_evento)

        else:
            print(showerror("erro", 'já tem evento marcado para essa data'))
            self.definir_data()