import database
conexao = database.conexao
cursor = database.conexao.cursor()

#Rel produtos mais vendidos

#Rel produtos por cliente

#Rel consumo médio por cliente

#Rel produtos baixo estoque
def prodBaixoEstoque():
    qtd_minima_produto = 150
    comando = f'SELECT id , nome_produto , preco_produto, qtd_produto FROM produtos WHERE qtd_produto <= "{qtd_minima_produto}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado