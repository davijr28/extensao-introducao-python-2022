#Importar biblioteca sqlite3
import sqlite3

#criar função conectar
def conectar():
  #Estabelecer conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #Criar objeto tipo cursor
  cursor = conexao.cursor()
  
  return conexao, cursor
