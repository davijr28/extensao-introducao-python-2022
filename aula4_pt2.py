#Importar biblioteca sqlite3
import sqlite3

#Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#Criar objeto tipo cursor
cursor = conexao.cursor()

#inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#executar o comando SQL
print(cursor.execute(sql))

#confirmar o INSERT com commit() e fechar o banco
conexao.commit()
conexao.close()