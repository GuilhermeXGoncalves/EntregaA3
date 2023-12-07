from flask import Flask, redirect, render_template, request, jsonify
import sqlite3
import client
import estoque 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/clientes', methods=['GET'])
def clientes():
    conexao = sqlite3.connect('loja.db', check_same_thread=False)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)

@app.route('/produtos', methods=['GET'])
def produtos():
    conexao = sqlite3.connect('loja.db', check_same_thread=False)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    return render_template('produtos.html', produtos=produtos)

@app.route('/clientes', methods=['POST'])
def add_cliente():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    cpf = request.form.get('cpf')
    client.criarClienteBancoDeDados(nome, telefone, cpf)
    return redirect('/clientes')

@app.route('/produtos', methods=['POST'])
def add_produto():
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    qtd = request.form.get('qtd')
    estoque.criarProdutoBancoDeDados(nome, preco, qtd)
    return redirect('/produtos')

@app.route('/produtos/add', methods=['POST'])
def adiciona_produto():
    data = request.get_json()
    nome = data['nome']
    preco = data['preco']
    qtd = data['qtd']
    estoque.criarProdutoBancoDeDados(nome, preco, qtd)
    return jsonify({'status': 'Produto adicionado com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)

