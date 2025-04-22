from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import messagebox
from view import *  

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


def mostrar():

    
    global tree

    lista= mostrar_info()
    #lista de cabeçario
    list_head = ['Id','nome', 'telefone', 'email', 'data', 'estado']
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

def inserir():

    nome = e_nome.get()
    telefone = e_tel.get()
    email = e_email.get()
    data = e_data.get()
    estado = e_estado.get()

    lista =[nome, telefone, email, data, estado]
    if nome == '':
        messagebox.showerror('ERRO', 'O campo nome nao pode estar vazio.')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso','Os dados foram cadastrados com sucesso.')

    e_nome.delete(0,'end')
    e_tel.delete(0, 'end')
    e_email.delete(0, 'end')
    e_data.delete(0, 'end')
    e_estado.delete(0, 'end')


    for widget in frame_dir.winfo_children():
        widget.destroy()

    mostrar()

global tree  
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0,'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')
        e_data.delete(0, 'end')
        e_estado.delete(0, 'end')

        e_nome.insert(0,tree_lista[1])
        e_tel.insert(0, tree_lista[2])
        e_email.insert(0,tree_lista[3] )
        e_data.insert(0,tree_lista [4] )
        e_estado.insert(0,tree_lista[5])

        def update():

            nome = e_nome.get()
            telefone = e_tel.get()
            email = e_email.get()
            data = e_data.get()
            estado = e_estado.get()

            lista =[nome, telefone, email, data, estado, valor_id]
            if nome == '':
                messagebox.showerror('ERRO', 'O campo nome nao pode estar vazio.')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso','Os dados foram atualizados com sucesso.')

            e_nome.delete(0,'end')
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')
            e_data.delete(0, 'end')
            e_estado.delete(0, 'end')


            for widget in frame_dir.winfo_children():
                widget.destroy()
            mostrar()
    #botao atualizar        
        b_update = Button(frame_esq, command=update,text='Confirmar',bg=cor2, width=5, height=1,borderwidth=0)
        b_update.place(relx=0.4, rely=0.9)

    except IndexError:
        messagebox.showerror('ERRO', 'selecione os dados na tabela')  


def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]
        delete_info(valor_id)
        messagebox.showinfo('SUCESSO', 'Os dados foram deletados com sucesso')

        for widget in frame_dir.winfo_children():
            widget.destroy()
        mostrar()
    except:
        messagebox.showerror('ERRO', 'Os dados não foram deletados corretamente')    



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

#email
l_email = Label(frame_esq, text='Email', fg=cor1,bg=cor2, font='arial 15 bold')
l_email.place(x=10, y=135)
e_email = Entry(frame_esq, border=4, bg=cor3)
e_email.place(x=10, y=160)


#candario
l_data = Label(frame_esq, text='Data consulta', fg=cor1, bg=cor2, font='arial 15 bold')
l_data.place(x=10, y=200)
e_data = DateEntry(frame_esq, border=4, bg=cor3, year=2025)
e_data.place(x=10, y=230)

#estado
l_estado = Label(frame_esq, text='Estado', fg=cor1, bg=cor2, font='arial 15 bold')
l_estado.place(x=220, y=200)
e_estado = Entry(frame_esq, border=4, width=5, bg=cor3)
e_estado.place(x=220, y=230)

#botões
b_inserir = Button(frame_esq,command=inserir, text='Inserir',background=cor1, borderwidth=0,width=5, height=1, relief='raised', overrelief='ridge')
b_inserir.place(relx=0.08, rely=0.7)
b_inserir.config(bg=cor1)

b_consultar = Button(frame_esq,command=atualizar, text='Consultar',bg=cor2, width=5, height=1,borderwidth=0)
b_consultar.place(relx=0.4, rely=0.7)

b_delete = Button(frame_esq, text='Delete', command=deletar,bg='#666666' ,width=5, height=1,borderwidth=0)
b_delete.place(relx=0.7, rely=0.7)



mostrar()
janela.mainloop()