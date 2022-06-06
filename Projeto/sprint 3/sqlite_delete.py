import sqlite3

try:
    #conexão com o bd
    banco = sqlite3.connect('dispvag.db')

    cursor = banco.cursor()

    #deleta dados a tabela vagas com condições especificas
    cursor.execute("DELETE from vagas WHERE salario = 'R$ 1.560,00 a R$ 2.500,00 (Bruto mensal)'")
    banco.commit() 

    banco.close()
    print("Os dados foram apagados")
except sqlite3.Error as erro:
    print("Erro ao excluir:",erro)

cursor.execute("DROP TABLE vagas")
banco.commit() 

