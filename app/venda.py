from flask import Flask, jsonify
import database
from datetime import datetime

app = Flask(__name__)

conexao = database.conexao
cursor = database.conexao.cursor()

def registrar_venda(id_cliente, id_produto, quantidade):
    # Verificar se o cliente existe
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        return jsonify(message="Cliente não encontrado."), 404

    # Verificar se o produto existe
    cursor.execute("SELECT * FROM produtos WHERE id=?", (id_produto,))
    produto = cursor.fetchone()
    if not produto:
        return jsonify(message="Produto não encontrado."), 404
    
    # Realizar a venda
    data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (?, ?, ?, ?)",
    (id_cliente, id_produto, quantidade, data_venda))

    novo_estoque = produto[2] - quantidade 
    cursor.execute("UPDATE produtos SET quantidade=? WHERE id=?", (novo_estoque, id_produto))

    # Confirmar a transação
    conexao.commit()
    return jsonify(message="Venda registrada com sucesso"), 201

def consultar_vendas():
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()
    return jsonify(vendas), 200

def consultar_venda_por_id(id_venda):
    cursor.execute("SELECT * FROM vendas WHERE id=?", (id_venda,))
    venda = cursor.fetchone()
    return jsonify(venda), 200

def povoar_banco_de_dados():
    clientes = ['Sabrina', 
                'Priscila', 
                'Herbert', 
                'Guilherme', 
                'Elaine']
    for cliente in clientes:
        cursor.execute("INSERT INTO clientes (nome) VALUES (?)", (cliente,))

    produtos = [('Iphone X', 10), ('Fone', 20), ('SSD', 30), ('Caixa de som', 40), ('Gabinete', 50),
                ('Teclado', 60), ('Galaxy S22', 70), ('Xiaomi', 80), ('Mouse', 90), ('Monitor', 100)]
    for produto in produtos:
        cursor.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", produto)

    conexao.commit()
    return jsonify(message="Banco de dados atualizado com sucesso"), 201
