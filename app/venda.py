from flask import request
from datetime import datetime
import database

conexao = database.conexao
cursor = database.conexao.cursor()

# CRIANDO TABELA DE VENDAS
def criarTabelaVendaBancoDeDados():
    comando = 'CREATE TABLE IF NOT EXISTS vendas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, id_cliente INTEGER NOT NULL, data_venda TEXT NOT NULL, FOREIGN KEY (id_cliente) REFERENCES clientes(id))'
    cursor.execute(comando)
    conexao.commit()

# REGISTRAR VENDA - 

def registrarVenda(nome_cliente, produto, qtd_produto):
    """ SELECT nome FROM clientes WHERE nome_cliente = {nome_cliente}
"""



# CONSULTAR TODAS AS VENDAS
def obterTodasVendas():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    vendas = cursor.fetchall()
    return vendas