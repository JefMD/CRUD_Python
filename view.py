import sqlite3 as lite

conn = lite.connect('dados.db')


#Crud - create


def inserir_info (i):
    with conn:
        cur = conn.cursor()
        query = ("INSERT INTO formulario(nome, telefone, email, data, estado)VALUES(?,?,?,?,?)")
        cur.execute(query,i)
        



#cRud - read
def mostrar_info():
    lista = []
    with conn:
        cur = conn.cursor()
        query = ( "SELECT * FROM formulario" )
        cur.execute(query)
        info = cur.fetchall()
        for item in info:
            lista.append(item)
    return lista
        




#crUd - update
def atualizar_info(i):
    with conn:
        cur = conn.cursor()
        query = ( "UPDATE formulario SET nome=?, telefone=?, email=?, data=?, estado=? WHERE id=?" )
        cur.execute(query,i)


#cruD - delete
def delete_info(i):
    with conn:
        cur = conn.cursor()
        query = ("DELETE FROM formulario WHERE id=?")   
        cur.execute(query, i)
