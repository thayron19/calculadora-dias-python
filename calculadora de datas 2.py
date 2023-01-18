import datetime
import tkinter
import tkinter.messagebox
import tkcalendar


# ---------------------------------------------------------------------------------------------------------------------
def popup():
    tkinter.messagebox.showinfo('Lógica', 'Dias = diferença dos dias \n'
                                          'Semanas = diferença dos dias / 7 \n'
                                          'Meses = diferença dos dias / 30 \n'
                                          'Anos = diferença dos dias / 365')


# ---------------------------------------------------------------------------------------------------------------------
def hoje(num):
    if num == 1:
        cal_var1.set(f'{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}')
    else:
        cal_var2.set(f'{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}')


# ---------------------------------------------------------------------------------------------------------------------
def teste_datas():
    data1 = datetime.datetime.strptime(calendario1.get_date(), '%d/%m/%Y').date()
    data2 = datetime.datetime.strptime(calendario2.get_date(), '%d/%m/%Y').date()
    # -----------------------------------------------------------------------------------------------------------------
    if data1 > data2:
        comparar = data1 - data2
    else:
        comparar = data2 - data1
    # -----------------------------------------------------------------------------------------------------------------
    if comparar.days == 1:
        diferenca1['text'] = f'{comparar.days} dia'
    elif comparar.days > 1:
        diferenca1['text'] = f'{comparar.days} dias'
    # -----------------------------------------------------------------------------------------------------------------
        if (comparar.days / 7) == 1:
            diferenca2['text'] = f'{comparar.days / 7:.2f} semana'
        elif (comparar.days / 7) > 1:
            diferenca2['text'] = f'{comparar.days / 7:.2f} semanas'
            diferenca3['text'] = ''
            diferenca4['text'] = ''
    # -----------------------------------------------------------------------------------------------------------------
            if (comparar.days / 30) == 1:
                diferenca3['text'] = f'{comparar.days / 30:.2f} mês'
            elif (comparar.days / 30) > 1:
                diferenca3['text'] = f'{comparar.days / 30:.2f} meses'
                diferenca4['text'] = ''
    # -----------------------------------------------------------------------------------------------------------------
                if (comparar.days / 365) == 1:
                    diferenca4['text'] = f'{comparar.days / 365:.2f} ano'
                elif (comparar.days / 365) > 1:
                    diferenca4['text'] = f'{comparar.days / 365:.2f} anos'
    # -----------------------------------------------------------------------------------------------------------------
    else:
        diferenca1['text'] = f'Hoje'
        diferenca2['text'] = ''
        diferenca3['text'] = ''
        diferenca4['text'] = ''


# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Cálculo de datas')

largura_janela = 530
altura_janela = 320

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicaol = float(largura_janela / 2 - largura_tela / 2)
posicaoa = float(altura_janela / 2 - altura_tela / 2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posicaol, posicaoa))
janela.resizable(width=False, height=False)
# ---------------------------------------------------------------------------------------------------------------------
cal_var1 = tkinter.StringVar(janela, '19/05/1988')
calendario1 = tkcalendar.Calendar(janela, selectmode='day', textvariable=cal_var1, locale="pt_BR")
calendario1.place(x=10, y=10)
# ---------------------------------------------------------------------------------------------------------------------
cal_var2 = tkinter.StringVar(janela, f'{datetime.date.today().day}/{datetime.date.today().month}/'
                                     f'{datetime.date.today().year}')

calendario2 = tkcalendar.Calendar(janela, selectmode='day', textvariable=cal_var2, locale="pt_BR")
calendario2.place(x=270, y=10)
# ---------------------------------------------------------------------------------------------------------------------
btn_hoje1 = tkinter.Button(janela, text='Hoje', command=lambda: hoje(1), font=('', 15), bg='#c5c6d1')
btn_hoje1.place(x=10, y=200, width=100)
# ---------------------------------------------------------------------------------------------------------------------
btn = tkinter.Button(janela, text='Calcular', command=lambda: teste_datas(), font=('', 15), bg='#8793ed')
btn.place(x=115, y=200, width=300)
# ---------------------------------------------------------------------------------------------------------------------
btn_hoje2 = tkinter.Button(janela, text='Hoje', command=lambda: hoje(2), font=('', 15), bg='#c5c6d1')
btn_hoje2.place(x=420, y=200, width=100)
# ---------------------------------------------------------------------------------------------------------------------
diferenca1 = tkinter.Label(janela, text='', font=('', 15), justify='center')
diferenca1.place(x=10, y=250, width=255)
diferenca2 = tkinter.Label(janela, text='', font=('', 15), justify='center')
diferenca2.place(x=270, y=250, width=255)
diferenca3 = tkinter.Label(janela, text='', font=('', 15), justify='center')
diferenca3.place(x=10, y=280, width=255)
diferenca4 = tkinter.Label(janela, text='', font=('', 15), justify='center')
diferenca4.place(x=270, y=280, width=255)
# ---------------------------------------------------------------------------------------------------------------------
teste_datas()
# ---------------------------------------------------------------------------------------------------------------------
calculo = tkinter.Button(janela, text='?', command=lambda: popup(), bg='#ed5555')
calculo.place(x=505, y=285)
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()
