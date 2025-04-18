from tkinter import *
from tkcalendar import Calendar, DateEntry


cor1 = '#B3CBED'
cor2 = '#FEF2E6'
cor3 = '#F5D684'

#criando janela

janela = Tk()
janela.title("Testando")
janela.geometry("1043x453")
janela.configure(background="black")
janela.resizable(width=FALSE, height=FALSE)


#dividindo a janela

frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief="flat")
frame_cima.grid(row=0, column=0)

frame_esq = Frame(janela,width=310, height=403, bg=cor2, relief="flat")
frame_esq.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_dir = Frame(janela, width=730,height=403, bg=cor3, relief='flat')
frame_dir.grid( row=0, column=1, sticky=NSEW, rowspan=2, padx=3, pady=0)


#crando label nome app
app_nome = Label(frame_cima, text='Formulário de consultoria', fg='white', bg=cor1,anchor=NW, font= 'arial 18 bold')
app_nome.place( x=10,y=20)

# label nome
l_nome = Label(frame_esq, text='Nome', fg= cor1, bg=cor2, font='arial 15 bold')
l_nome.place(x=10, y=20)
e_nome = Entry(frame_esq, border=4)
e_nome.place(x=10, y=40)

#Telefone
l_tel = Label(frame_esq, text='Telefone', fg=cor1,bg=cor2, font='arial 15 bold')
l_tel.place(x=10, y=80)
e_tel = Entry(frame_esq, border=4)
e_tel.place(x=10, y=100)


#candario
l_data = Label(frame_esq, text='Data consulta', fg=cor1, bg='#666666', font='arial 15 bold')
l_data.place(x=10, y=200)
e_data = DateEntry(frame_esq, border=4, year=2025)
e_data.place(x=10, y=230)

#estado
l_data = Label(frame_esq, text='Estado', fg='white', bg='#666666', font='arial 15 bold')
l_data.place(x=220, y=200)
e_data = Entry(frame_esq, border=4, width=5)
e_data.place(x=220, y=230)

#botões
b_inserir = Button(frame_esq, text='Inserir', command=janela.destroy,bg='#999999',borderwidth=0,width=5, height=1, relief='flat')
b_inserir.place(relx=0.08, rely=0.7)

b_consultar = Button(frame_esq, text='Consultar', command=janela.destroy, width=5, height=1,borderwidth=0)
b_consultar.place(relx=0.4, rely=0.7)

b_delete = Button(frame_esq, text='Delete', command=janela.destroy,bg='#666666' ,width=5, height=1,borderwidth=0)
b_delete.place(relx=0.7, rely=0.7)



janela.mainloop()