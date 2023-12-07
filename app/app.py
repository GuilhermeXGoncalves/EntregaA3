from flask import Flask, redirect, render_template, request, jsonify
import sqlite3
import client
import estoque 
import venda

app = Flask(__name__)

#ROTA PRINCIPAL
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


#CLIENTES -------------------------------------------------

#LER TODOS CLIENTES
@app.route('/clientes', methods=['GET'])
def clientes():
    conexao = sqlite3.connect('loja.db', check_same_thread=False)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)


#ADICIONA CLIENTE
@app.route('/clientes/add', methods=['POST'])
def add_cliente():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    cpf = request.form.get('cpf')
    client.criarClienteBancoDeDados(nome, telefone, cpf)
    return redirect('/clientes')


#LER CLIENTE POR ID
#EDITA CLIENTE POR ID
#DELETA CLIENTE POR ID


#PRODUTOS -------------------------------------------------

#LER TODOS OS PRODUTOS
@app.route('/produtos', methods=['GET'])
def produtos():
    conexao = sqlite3.connect('loja.db', check_same_thread=False)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    return render_template('produtos.html', produtos=produtos)

#ADICIONA PRODUTOS
@app.route('/produtos/add', methods=['POST'])
def add_produto():
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    qtd = request.form.get('qtd')
    estoque.criarProdutoBancoDeDados(nome, preco, qtd)
    return redirect('/produtos')

#LER PRODUTO POR ID
#EDITA PRODUTO POR ID
#DELETA PRODUTO POR ID

#VENDAS -------------------------------------------------

# REGISTRAR VENDA
@app.route('/vendas/add', methods=['POST'])
def registrar_venda():
    data = request.get_json()
    id_cliente = data['id_cliente']
    produtos = data['produtos']
    venda.registrarVenda(id_cliente, produtos)
    return ('OK')

# CONSULTAR TODAS AS VENDAS
@app.route('/vendas', methods=['GET'])
def obter_todas_vendas():
    vendas = venda.obterTodasVendas()
    return jsonify(vendas)

#LER VENDA POR ID
#EDITAR VENDA
#DELETAR VENDA

if __name__ == '__main__':
    app.run(debug=True)

