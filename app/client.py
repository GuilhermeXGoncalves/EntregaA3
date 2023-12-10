from flask import request
import database
conexao = database.conexao
cursor = database.conexao.cursor()

#CRIANDO TABELA BANCO 
def criarTabelaClienteBancoDeDados():
    comando = 'CREATE TABLE IF NOT EXISTS clientes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, telefone VARCHAR(11) NOT NULL,cpf VARCHAR(11) NOT NULL)'
    cursor.execute(comando)
    conexao.commit()
    

# CRIAR CLIENTE
def criarClienteBancoDeDados(nome, telefone, cpf):
    comando = f'INSERT INTO clientes (nome , telefone, cpf) VALUES ("{nome}" , "{telefone}" , "{cpf}")'
    cursor.execute(comando)
    conexao.commit()


# LER UM CLIENTE
def lerClienteBancoDeDados(id):

    comando = f'SELECT id , nome , telefone, cpf FROM clientes WHERE id = "{id}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado


def lerTodosClientes():
    comando = f'SELECT * FROM clientes'
    cursor.execute(comando)
    clientes = cursor.fetchall()
    return clientes

    
# EDITAR CLIENTE
def atualizaTelClienteNoDb(id):
    telefone = request.get_json()
    comando = f'UPDATE clientes SET telefone = "{telefone}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    resultado = cursor.fetchall()
    return resultado

def atualizaNomeClienteNoDb(id):
    nome = request.get_json()
    comando = f'UPDATE clientes SET nome = "{nome}" WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    resultado = cursor.fetchall()
    return resultado



# EXLUIR CLIENTE
def deletarClienteDoBancoDeDados(id):
    cursor = database.conexao.cursor()
    comando = f'DELETE FROM clientes WHERE id = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    return ('ok')



