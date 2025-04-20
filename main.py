from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk


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
e_nome = Entry(frame_esq, border=4, bg=cor3)
e_nome.place(x=10, y=40)

#Telefone
l_tel = Label(frame_esq, text='Telefone', fg=cor1,bg=cor2, font='arial 15 bold')
l_tel.place(x=10, y=80)
e_tel = Entry(frame_esq, border=4, bg=cor3)
e_tel.place(x=10, y=100)


#candario
l_data = Label(frame_esq, text='Data consulta', fg=cor1, bg=cor2, font='arial 15 bold')
l_data.place(x=10, y=200)
e_data = DateEntry(frame_esq, border=4, bg=cor3, year=2025)
e_data.place(x=10, y=230)

#estado
l_data = Label(frame_esq, text='Estado', fg=cor1, bg=cor2, font='arial 15 bold')
l_data.place(x=220, y=200)
e_data = Entry(frame_esq, border=4, width=5, bg=cor3)
e_data.place(x=220, y=230)

#botões
b_inserir = Button(frame_esq, text='Inserir',background=cor1, borderwidth=0,width=5, height=1, relief='raised', overrelief='ridge')
b_inserir.place(relx=0.08, rely=0.7)
b_inserir.config(bg=cor1)

b_consultar = Button(frame_esq, text='Consultar', command=janela.destroy,bg=cor2, width=5, height=1,borderwidth=0)
b_consultar.place(relx=0.4, rely=0.7)

b_delete = Button(frame_esq, text='Delete', command=janela.destroy,bg='#666666' ,width=5, height=1,borderwidth=0)
b_delete.place(relx=0.7, rely=0.7)

lista=[[1,'ana lucia meira', '123@gmail.com', '123456789', '20/03/2021', 'São paulo'],
       [2,'joana lucia meira', '123@gmail.com', '123456789', '20/03/2021', 'São paulo'],
       [3,'heloisa lucia meira', '123@gmail.com', '123456789', '20/03/2021', 'São paulo'],
       [4,'antonio lucia meira', '123@gmail.com','123456789', '20/03/2021', 'São paulo'],
       [5,'angelina lucia meira', '123@gmail.com','123456789', '20/03/2021', 'São paulo'],
       [6,'ana lucia meira', '123@gmail.com','123456789', '20/03/2021', 'São paulo']]

#lista de cabeçario
list_head = ['Id','nome','email', 'telefone', 'data', 'estado']



tree = ttk.Treeview(frame_dir, selectmode='extended', columns=list_head, show='headings')

#vertical scrollBar
vsb = ttk.Scrollbar(frame_dir, orient='vertical', command= tree.yview)

#horizontal scrollBar
hsb = ttk.Scrollbar(frame_dir, orient='horizontal', command=tree.xview)


tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0,sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame_dir.rowconfigure(0, weight=12)

#local do elementos nas colunas
hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'nw']
#tamanho das larguras das colunas
h = [30, 170,150,150,140,170]
n= 0


for col in list_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])

    n+=1

for item in lista:
    tree.insert('','end', values=item)



janela.mainloop()