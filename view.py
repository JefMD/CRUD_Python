from tkinter import *
from tkcalendar import DateEntry

janela = Tk()
janela.geometry("400x200")

frame = Frame(janela, width=400, height=200)
frame.pack()

# Campo de data com .place()
e_data = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
e_data.place(x=50, y=50)

janela.mainloop()
