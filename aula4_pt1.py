#Importar biblioteca sqlite3
import sqlite3

#Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#Criar objeto tipo cursor
cursor = conexao.cursor()

#Comnado SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#Executar o comando SQL no SQLite (cursor)
cursor.execute(sql)

#exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")