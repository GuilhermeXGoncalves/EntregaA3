from flask import Flask, redirect, render_template, request, jsonify
import database, client, estoque, venda
conexao = database.conexao
cursor = database.conexao.cursor()

app = Flask(__name__)

#ROTA PRINCIPAL
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


#CLIENTES -------------------------------------------------

#LER TODOS CLIENTES
@app.route('/clientes', methods=['GET'])
def clientes():
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
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()
    return render_template('vendas.html', vendas = vendas)

#LER VENDA POR ID
#EDITAR VENDA
#DELETAR VENDA

#RELATÓRIOS -----------------------------------------------
@app.route('/relatorios')
def relatorio():
    return render_template('relatorio.html')

@app.route('/relatorios/estoquebaixo', methods=['GET'])
def prod_baixo_estoque():
    qtd_minima_produto = 150
    comando = f'SELECT id , nome_produto , preco_produto, qtd_produto FROM produtos WHERE qtd_produto <= "{qtd_minima_produto}"'
    cursor.execute(comando)
    produtos = cursor.fetchall()
    return render_template('estoqueBaixo.html', produtos=produtos)


if __name__ == '__main__':
    app.run(debug=True)

