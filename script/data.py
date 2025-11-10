#type:ignore


import pandas as pd
import random
from datetime import datetime, timedelta
import os

os.makedirs("../data", exist_ok=True)


#CLIENTE
clientes = []
nomes = ["Ana", "Bruno", "Carla", "Diego", "Eduarda", "Felipe", "Gabriela", "Heitor", "Isabela", "João"]
cidades = ["São Paulo", "Rio de Janeiro","Belo Horizonte","Curitiba", "Recife", "Fortaleza"]
estados = ["SP", "RJ", "MG", "PR", "PE", "CE"]

for i in range(1,51):
    clientes.append({
        "id_cliente": i,
        "nome": random.choice(nomes) + f"{random.randint(100,999)}",
        "idade": random.randint(18,60),
        "cidade": random.choice(cidades),
        "estado": random.choice(estados),
        "genero": random.choice(["Masculino","Feminino"])   
    })

df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv("../data/clientes.csv", index=False)

#PRODUTOS

produtos = []
categorias = ["Eletrônicos","Roupas","Livros", "Alimentos","Acessório"]
for i in range(1,21):
    categoria = random.choice(categorias)
    preco_custo = random.uniform(20, 200)
    preco_venda = preco_custo * random.uniform(1.2, 1.8)
    produtos.append({
        "id_produto": i,
        "nome_produto": f"Produto_{i}",
        "categoria": categoria,
        "preco_custo": round(preco_custo, 2),
        "preco_venda": round(preco_venda, 2)
    })

df_produtos = pd.DataFrame(produtos)
df_produtos.to_csv("../data/produtos.csv",index=False)

#VENDAS
vendas = []
data_inicial = datetime(2023, 1, 1)
for i in range(1, 1001):
    id_cliente = random.randint(1, 50)
    id_produto = random.randint(1, 20)
    quantidade = random.randint(1, 5)
    data_venda = data_inicial + timedelta(days=random.randint(0, 600))
    vendas.append({
        "id_venda": i,
        "id_cliente": id_cliente,
        "id_produto": id_produto,
        "quantidade": quantidade,
        "data_venda": data_venda.date()
    })

df_vendas = pd.DataFrame(vendas)
df_vendas.to_csv("../data/vendas.csv", index=False)

print("Dados gerados com sucesso na pasta /data")