from flask import Flask, redirect, render_template, request, jsonify
import database
import client
import estoque
import venda
conexao = database.conexao
cursor = database.conexao.cursor()

app = Flask(__name__)

# ROTA PRINCIPAL


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


# CLIENTES -------------------------------------------------

# LER TODOS CLIENTES
@app.route('/clientes', methods=['GET'])
def clientes():
    comando = f'SELECT id, nome, telefone, cpf FROM clientes'
    cursor.execute(comando)
    clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)


# ADICIONA CLIENTE
@app.route('/clientes/add', methods=['POST'])
def add_cliente():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    cpf = request.form.get('cpf')
    client.criarClienteBancoDeDados(nome, telefone, cpf)
    return redirect('/clientes')


# LER CLIENTE POR ID
@app.route('/clientes/<id>', methods=['GET'])
def obter_cliente(id):
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    cliente = cursor.fetchone()
    return render_template('clientes.html', cliente=cliente)

# EDITA CLIENTE POR ID


@app.route('/clientes/edit/<id>', methods=['POST'])
def editar_cliente(id):
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    cpf = request.form.get('cpf')
    cursor.execute(
        "UPDATE clientes SET nome = %s, telefone = %s, cpf = %s WHERE id = %s", (nome, telefone, cpf, id))
    return redirect('/clientes')

# DELETA CLIENTE POR ID


@app.route('/clientes/delete/<id>', methods=['DELETE'])
def deletar_cliente(id):
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    return ('OK')


# PRODUTOS -------------------------------------------------

# LER TODOS OS PRODUTOS
@app.route('/produtos', methods=['GET'])
def produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    return render_template('produtos.html', produtos=produtos)

# ADICIONA PRODUTOS


@app.route('/produtos/add', methods=['POST'])
def add_produto():
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    qtd = request.form.get('qtd')
    estoque.criarProdutoBancoDeDados(nome, preco, qtd)
    return redirect('/produtos')

# LER PRODUTO POR ID


@app.route('/produtos/<id>', methods=['GET'])
def get_produto(id):
    produto = estoque.lerProdutoBancoDeDados(id)
    return render_template('produto.html', produto=produto)

# EDITA PRODUTO POR ID


@app.route('/produtos/edit/<id>', methods=['POST'])
def edit_produto(id):
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    qtd = request.form.get('qtd')
    estoque.editarProdutoBancoDeDados(id, nome, preco, qtd)
    return redirect('/produtos')

# DELETA PRODUTO POR ID


@app.route('/produtos/delete/<id>', methods=['POST'])
def delete_produto(id):
    estoque.deletarProdutoBancoDeDados(id)
    return redirect('/produtos')

# VENDAS -------------------------------------------------

# REGISTRAR VENDA


@app.route('/vendas/add', methods=['POST'])
def registrar_venda():
    data = request.get_json()
    id_cliente = data['nome_cliente']
    produtos = data['produtos']
    venda.registrarVenda(id_cliente, produtos)
    return ('OK')

# CONSULTAR TODAS AS VENDAS


@app.route('/vendas', methods=['GET'])
def obter_todas_vendas():
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()
    return render_template('vendas.html', vendas=vendas)

# LER VENDA POR ID


@app.route('/vendas/<id>', methods=['GET'])
def obter_venda(id):
    cursor.execute("SELECT * FROM vendas WHERE id = %s", (id,))
    venda = cursor.fetchone()
    return render_template('venda.html', venda=venda)

# RELATÓRIOS -----------------------------------------------
@app.route('/relatorios', methods=['GET'])
def index_relatorio():
    print('Rota Relatório')
    return render_template('relatorio.html')

@app.route('/relatorio_produtos_mais_vendidos', methods=['GET'])
def relatorio_produtos_mais_vendidos():
    cursor.execute("SELECT produtos FROM vendas")
    vendas = cursor.fetchall()
    total_vendas_por_produto = defaultdict(int)

    # CARLCULAR A QUANTIDADE DE ITENS MAIS VENDIDOS
    for venda in vendas:
        produtos = venda['produtos']
        for produto, quantidade in produtos.items():
            total_vendas_por_produto[produto] += quantidade

    # ORDENAR OS PRODUTOS COM BASE NA QUANTIDADE DE VENDAS
    produtos_mais_vendidos = sorted(
        total_vendas_por_produto.items(), key=lambda x: x[1], reverse=True)

    # GERAR O RELATÓRIO
    relatorio = "Relatório de Produtos Mais Vendidos:\n"
    for produto, quantidade_total in produtos_mais_vendidos:
        relatorio += f"{produto}: {quantidade_total} unidades\n"

    return render_template('relatorio_produtos_mais_vendidos.html', relatorio=relatorio)


@app.route('/relatorio/produtos_por_cliente', methods=['GET'])
def relatorio_produtos_por_cliente():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    # VERIFICAR AS VENDAS
    cursor.execute("SELECT * FROM vendas")
    vendas = cursor.fetchall()

    # ARMAZENAR RELATÓRIO
    relatorio = {}

    # RECUPERAR AS VENDAS E ASSOCIAR EM UM CLIENTE
    for cliente in clientes:
        cliente_id = cliente['id']
        relatorio[cliente_id] = {'cliente': cliente, 'produtos_vendidos': []}

        # VERIFICAR SE A VENDA ESTÁ ASSOCIADA NO CLIENTE
        for venda in vendas:
            if venda['id_cliente'] == cliente_id:
                produtos_vendidos = venda['produtos']
                relatorio[cliente_id]['produtos_vendidos'].extend(
                    produtos_vendidos)

    return render_template('relatorio_produtos_por_cliente.html', relatorio=relatorio)


@app.route('/relatorio/media_consumo/<id_cliente>', methods=['GET'])
def relatorio_media_consumo(id_cliente):
    # CONSULTAR DADOS
    cursor.execute(
        "SELECT produtos FROM vendas WHERE id_cliente = %s", (id_cliente,))
    vendas_cliente = cursor.fetchall()

    if not vendas_cliente:
        return render_template('sem_vendas.html', id_cliente=id_cliente)

    # CALCULAR MÉDIA CONSUMO
    total_produtos = 0
    total_vendas = len(vendas_cliente)

    for venda in vendas_cliente:
        produtos_venda = venda['produtos']
        total_produtos += len(produtos_venda)

    media_consumo = total_produtos / total_vendas

    return render_template('relatorio_media_consumo.html', id_cliente=id_cliente, media_consumo=media_consumo)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
