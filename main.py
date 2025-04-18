from tkinter import *

from tkcalendar import Calendar, DateEntry



#criando janela

janela = Tk()
janela.title("Testando")
janela.geometry("1043x453")
janela.configure(background="black")
janela.resizable(width=FALSE, height=FALSE)


#dividindo a janela

frame_cima = Frame(janela, width=310, height=50, bg='#999999', relief="flat")
frame_cima.grid(row=0, column=0)

frame_esq = Frame(janela,width=310, height=403, bg='#666666', relief="flat")
frame_esq.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_dir = Frame(janela, width=700,height=403, bg='gray', relief='flat')
frame_dir.grid( row=0, column=1, sticky=NSEW, rowspan=2, padx=3, pady=0)


#crando label nome app
app_nome = Label(frame_cima, text='Formulário de consultoria', fg='white', bg='#999999',anchor=NW, font= 'arial 18 bold')
app_nome.place( x=10,y=20)

# label nome
l_nome = Label(frame_esq, text='Nome', fg='white', bg='#666666', font='arial 15 bold')
l_nome.place(x=10, y=20)
e_nome = Entry(frame_esq, border=4)
e_nome.place(x=10, y=40)

#Telefone
l_tel = Label(frame_esq, text='Telefone', fg='white', bg='#666666', font='arial 15 bold')
l_tel.place(x=10, y=80)
e_tel = Entry(frame_esq, border=4)
e_tel.place(x=10, y=100)


#candario
l_data = Label(frame_esq, text='Data consulta', fg='white', bg='#666666', font='arial 15 bold')
l_data.place(x=10, y=200)
e_data = DateEntry(frame_esq, border=4, year=2025)
e_data.place(x=10, y=230)

#estado
l_data = Label(frame_esq, text='Estado', fg='white', bg='#666666', font='arial 15 bold')
l_data.place(x=220, y=200)
e_data = Entry(frame_esq, border=4, width=5)
e_data.place(x=220, y=230)

#botões
b_inserir = Button(frame_esq, text='inserir', command=exit, width=5, height=1)
b_inserir.place(relx=0.1, rely=0.7)


janela.mainloop()