import sqlite3
conexao = sqlite3.connect('loja.db', check_same_thread=False)  
cursor = conexao.cursor()


