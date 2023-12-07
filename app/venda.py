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

# REGISTRAR VENDA
def registrarVenda(id_cliente, produtos):
    data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    comando = f'INSERT INTO vendas (id_cliente, data_venda) VALUES ("{id_cliente}", "{data_venda}")'
    cursor.execute(comando)
    conexao.commit()

    id_venda = cursor.lastrowid  # Obtém o ID da venda recém-inserida

    for produto in produtos:
        id_produto, quantidade = produto['id_produto'], produto['quantidade']
        comando = f'INSERT INTO itens_venda (id_venda, id_produto, quantidade) VALUES ("{id_venda}", "{id_produto}", "{quantidade}")'
        cursor.execute(comando)
        conexao.commit()

# CONSULTAR TODAS AS VENDAS
def obterTodasVendas():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    vendas = cursor.fetchall()
    return vendas