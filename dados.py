import sqlite3 as lite


#criando conexao
con = lite.connect('dados.db')



#criando tabela


with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, telefone TEXT, email TEXT, data DATE, estado TEXT)")
