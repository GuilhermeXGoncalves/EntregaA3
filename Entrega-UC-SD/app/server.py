import estoque, client
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

# INDEX
@app.route('/')
def index():
    return render_template("index.html")


##----------PRODUTOS

# CONSULTAR TODOS OS PRODUTOS
@app.route('/produtos', methods=['GET'])
def produto():
    produto = estoque.lerTodosProdutos()
    return jsonify(produto)


# CONSULTAR  PRODUTO POR NOME
@app.route('/produtos/<string:nome_produto>', methods=['GET'])
def obter_produto_por_nome(nome_produto):
    produto = estoque.lerProdutoBancoDeDados(nome_produto)
    return jsonify(produto)


# EDITAR PRODUTO = QTD
@app.route('/produtos/qtd/<string:nome_produto>', methods=['PUT'])
def edita_qtd_produto(nome_produto):
    produto = estoque.atualizaQtdProdutoNoDb(nome_produto)
    return jsonify(produto)

# EDITAR PRODUTO = PREÇO
@app.route('/produtos/pr/<string:nome_produto>', methods=['PUT'])
def edita_preco_produto(nome_produto):
    produto = estoque.atualizaPrecoProdutoNoDb(nome_produto)
    return jsonify(produto)


# DELETAR PRODUTO
@app.route('/produtos/del/<string:nome_produto>', methods=['DELETE'])
def deleta_prod_db(nome_produto):
    produto = estoque.deletarProdutoDoBancoDeDados(nome_produto)
    return jsonify(produto)


# CADASTRAR PRODUTO
@app.route('/produtos/add', methods=['POST'])
def cria_prod_db():
    estoque.criarProdutoBancoDeDados(nome = request.get_json() , preco = request.get_json() , qtd = request.get_json())
    return ('OK')


##----------CLIENTES

# CONSULTAR TODOS OS CLIENTES
@app.route('/clientes', methods=['GET'])
def get_clientes():
    cliente = client.lerTodosClientes()
    return jsonify(cliente)

# CONSULTAR CLIENTE POR ID
@app.route('/clientes/<int:id>' , methods=['GET'])
def get_cliente_por_id(id):
    cliente = client.lerClienteBancoDeDados(id)
    return jsonify(cliente)

# EDITAR CLIENTE = TELEFONE
@app.route('/clientes/tel/<int:id>', methods=['PUT'])
def edita_telefone_cliente(id):
    cliente = client.atualizaTelClienteNoDb(id)
    return jsonify(cliente)

# EDITAR CLIENTE = NOME
@app.route('/clientes/nome/<int:id>', methods=['PUT'])
def edita_nome_cliente(id):
    cliente = client.atualizaNomeClienteNoDb(id)
    return jsonify(cliente)

# DELETAR CLIENTE
@app.route('/clientes/del/<int:id>', methods=['DELETE'])
def deleta_client_db(id):
    cliente = client.deletarClienteDoBancoDeDados(id)
    return jsonify(cliente)

# CADASTRAR CLIENTE


if __name__ == "__main__":
    app.run(debug=True, port=5500)
