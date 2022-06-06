import sqlite3

#conexão com o bd
banco = sqlite3.connect('dispvag.db')

cursor = banco.cursor()

cursor.execute("DROP TABLE vagas")
banco.commit() 