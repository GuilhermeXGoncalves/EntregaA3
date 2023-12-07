import sqlite3
from datetime import datetime
conexao = sqlite3.connect('loja.db', check_same_thread=False)  
cursor = conexao.cursor()

#PARTE DO CLIENTE --------------------------------------------------------

def criarTabelaClienteBancoDeDados():
    comando = 'CREATE TABLE IF NOT EXISTS clientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, telefone VARCHAR(11) NOT NULL,cpf VARCHAR(11) NOT NULL)'
    cursor.execute(comando)
    conexao.commit()


def criarClienteBancoDeDados(nome, telefone, cpf):
    comando = f'INSERT INTO clientes (nome , telefone, cpf) VALUES ("{
        nome}" , "{telefone}" , "{cpf}")'
    cursor.execute(comando)
    conexao.commit()

def adicionaCliente():
    criarClienteBancoDeDados('Herbert' , '71986393806' , '78536578855')
    criarClienteBancoDeDados('Guilherme' , '71999287637' , '12365478999')
    criarClienteBancoDeDados('Priscila' , '71996979491' , '32145698777')
    criarClienteBancoDeDados('Elaine' , '71987335906' , '98732165444')
    criarClienteBancoDeDados('Sabrina' , '71992032981' , '45698712333')


#PARTE DOS PRODUTOS --------------------------------------------------------------------------

def criarTabelaProdutoBancoDeDados():
    comando = 'CREATE TABLE IF NOT EXISTS produtos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome_produto TEXT NOT NULL, preco_produto FLOAT NOT NULL,qtd_produto INTEGER NOT NULL)'
    cursor.execute(comando)

def criarProdutoBancoDeDados(nome, preco, qtd):
    comando = f'INSERT INTO produtos (nome_produto , preco_produto, qtd_produto) VALUES ("{
        nome}" , "{preco}" , "{qtd}")'
    cursor.execute(comando)
    conexao.commit()

def adicionaProduto():
    criarProdutoBancoDeDados('TV', 3299.90, 10)
    criarProdutoBancoDeDados('IPHONE 15', 7999.90, 1000)
    criarProdutoBancoDeDados('MACBOOK PRO', 9999.90, 200)
    criarProdutoBancoDeDados('IPHONE 14 PRO MAX', 4599.90, 500)
    criarProdutoBancoDeDados('S23 ULTRA', 5799.90, 150)
    criarProdutoBancoDeDados('GELADEIRA', 6300.00, 30)
    criarProdutoBancoDeDados('FOGÃO', 1589.90, 700)
    criarProdutoBancoDeDados('MICROONDAS', 899.90, 75)
    criarProdutoBancoDeDados('LIQUIFICADOR', 219.90, 2000)
    criarProdutoBancoDeDados('SANDUICHEIRA', 119.90, 1000)
    criarProdutoBancoDeDados('MÁQUINA DE LAVAR', 3899.90, 189)
    criarProdutoBancoDeDados('SOFÁ', 1999.90, 4000)


#PARTE DE VENDAS ----------------------------------------------------------------------------

def criarTabelaVendaBancoDeDados():
    comando = 'CREATE TABLE IF NOT EXISTS vendas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, id_cliente INTEGER NOT NULL, data_venda TEXT NOT NULL, FOREIGN KEY (id_cliente) REFERENCES clientes(id))'
    cursor.execute(comando)
    conexao.commit()


criarTabelaClienteBancoDeDados()
adicionaCliente()
criarTabelaProdutoBancoDeDados()
adicionaProduto()
criarTabelaVendaBancoDeDados()

