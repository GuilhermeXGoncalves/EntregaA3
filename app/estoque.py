from flask import request
import database
conexao = database.conexao
cursor = database.conexao.cursor()

# CRIANDO TABELA BANCO
def criarTabelaProdutoBancoDeDados():
    comando = 'CREATE TABLE IF NOT EXISTS produtos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome_produto TEXT NOT NULL, preco_produto FLOAT NOT NULL,qtd_produto INTEGER NOT NULL)'
    cursor.execute(comando)


# CRIAR PRODUTO
def criarProdutoBancoDeDados(nome, preco, qtd):
    comando = f'INSERT INTO produtos (nome_produto , preco_produto, qtd_produto) VALUES ("{nome}" , "{preco}" , "{qtd}")'
    cursor.execute(comando)
    conexao.commit()


# LER UM PRODUTO
def lerProdutoBancoDeDados(nome_produto):
    comando = f'SELECT id , nome_produto , preco_produto, qtd_produto FROM produtos WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado


# LER TODOS PRODUTOS
def lerTodosProdutos():
    comando = f'SELECT * FROM produtos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado


# ATUALIZA DADO DO PRODUTO
def atualizaQtdProdutoNoDb(id):

    qtd_produto = request.get_json()
    comando = f'UPDATE produtos SET qtd_produto = "{qtd_produto}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    resultado = cursor.fetchall()
    return resultado

def atualizaPrecoProdutoNoDb(id):

    preco_produto = request.get_json()
    comando = f'UPDATE produtos SET preco_produto = "{preco_produto}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    resultado = cursor.fetchall()
    return resultado


# EXLUIR PRODUTO
def deletarProdutoDoBancoDeDados(id):
    cursor = database.conexao.cursor()
    comando = f'DELETE FROM produtos WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    return ('ok')


