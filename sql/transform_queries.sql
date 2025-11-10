
CREATE MATERIALIZED VIEW mv_vendas_detalhadas AS
SELECT
    v.id_venda,
    v.data_venda,
    v.quantidade,
    
    -- Dados do Produto
    p.id_produto,
    p.nome_produto,
    p.categoria,
    p.preco_custo,
    p.preco_venda,
    
    -- Dados do Cliente
    c.id_cliente,
    c.nome AS nome_cliente,
    c.idade,
    c.cidade,
    c.estado,
    c.genero,
    
    -- Métricas Calculadas
    (v.quantidade * p.preco_venda) AS receita_total,
    (v.quantidade * (p.preco_venda - p.preco_custo)) AS lucro_total
FROM vendas v
JOIN produtos p ON v.id_produto = p.id_produto
JOIN clientes c ON v.id_cliente = c.id_cliente;


SELECT
    categoria,
    SUM(receita_total) AS receita_total_categoria,
    SUM(lucro_total) AS lucro_total_categoria
FROM mv_vendas_detalhadas
GROUP BY categoria
ORDER BY lucro_total_categoria DESC;

SELECT
    DATE_TRUNC('month', data_venda) AS mes,
    SUM(receita_total) AS receita_mensal,
    SUM(lucro_total) AS lucro_mensal
FROM mv_vendas_detalhadas
GROUP BY mes
ORDER BY mes;

    id_produto,
    nome_produto,
    categoria,
    SUM(quantidade) AS total_vendido,
    SUM(lucro_total) AS lucro_acumulado
FROM mv_vendas_detalhadas
GROUP BY id_produto, nome_produto, categoria
ORDER BY lucro_acumulado DESC
LIMIT 10;

SELECT
    id_cliente,
    nome_cliente,
    ROUND(SUM(receita_total) / COUNT(DISTINCT id_venda), 2) AS ticket_medio
FROM mv_vendas_detalhadas
GROUP BY id_cliente, nome_cliente
ORDER BY ticket_medio DESC;


SELECT
    CASE
        WHEN idade < 25 THEN '18-24'
        WHEN idade BETWEEN 25 AND 34 THEN '25-34'
        WHEN idade BETWEEN 35 AND 44 THEN '35-44'
        WHEN idade BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS faixa_etaria,
    genero,
    COUNT(DISTINCT id_cliente) AS total_clientes,
    SUM(receita_total) AS receita_por_faixa
FROM mv_vendas_detalhadas
GROUP BY faixa_etaria, genero
ORDER BY faixa_etaria, genero;


SELECT
    estado,
    cidade,
    SUM(receita_total) AS receita_por_local
FROM mv_vendas_detalhadas
GROUP BY estado, cidade
ORDER BY estado, receita_por_local DESC;