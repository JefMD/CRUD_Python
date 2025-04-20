import sqlite3 as lite

conn = lite.connect('dados.db')


#Crud - create

lista = ['ana lucia meira', '123@gmail.com', '123456789', '20/03/2021', 'São paulo']


with conn:
    cur = conn.cursor()
    query = ("INSERT INTO formulario(nome, email, telefone, data, estado)VALUES(?,?,?,?,?)")
    cur.execute(query,lista)



#cRud - read
with conn:
    cur = conn.cursor()
    query = ( "SELECT * FROM formulario" )
    cur.execute(query)
    info = cur.fetchall()
    print(info)




#crUd - update
    lista= ['ana lucia', 1]
with conn:
    cur = conn.cursor()
    query = ( "UPDATE formulario SET nome=? WHERE id=?" )
    cur.execute(query,lista)


#cruD - delete
lista = [1]
with conn:
    cur = conn.cursor()
    query = ("DELETE FROM formulario WHERE id=?")   
    cur.execute(query, lista)
