# 🛒 Projeto Loja Online

## 🎯 Visão Geral  
O **Loja Online** é um projeto completo de **Análise de Dados**, simulando uma loja virtual e passando por todas as etapas do processo **ELT → Power BI**.  
O objetivo é demonstrar o fluxo de **coleta, tratamento, carga e visualização de dados**, ideal para portfólio de quem atua ou quer iniciar na área de dados.

---

## 📁 Estrutura do Projeto  
```bash
projeto_loja_online/
│
├── data/          # Dados simulados em CSV
├── scripts/       # Scripts Python para gerar e carregar dados
├── sql/           # Scripts SQL (criação e consultas)
├── powerbi/       # Dashboard (.pbix)
└── README.md      # Documentação do projeto
```

---

## ⚙️ Tecnologias Utilizadas  
- 🐍 **Python (Pandas, Random, Datetime)** – Geração e manipulação dos dados  
- 🗃️ **MySQL** – Criação de banco e modelagem relacional  
- 💾 **SQL** – Consultas, joins, views e métricas calculadas  
- 📊 **Power BI** – Visualização e análise interativa dos indicadores  

---

## 🚀 Etapas do Projeto  
1. **Extração (E)** – Geração de dados simulados com Python.  
2. **Carga (L)** – Inserção dos CSVs no banco MySQL.  
3. **Transformação (T)** – Criação de tabelas, joins e métricas em SQL.  
4. **Visualização (BI)** – Criação de dashboard no Power BI.  

---

## 📊 Principais Indicadores no Dashboard  
- Receita total 💰  
- Lucro total 📈  
- Quantidade de vendas 🧾  
- Vendas por categoria de produto 🛍️  
- Perfil dos clientes (idade, cidade, gênero) 👥  
- Evolução mensal de vendas 📆  

---

## 🧩 Como Executar Localmente  

1. Clone o repositório:
   ```bash
   git clone https://github.com/Cezanne369/Loja_online.git
   cd Loja_online
   ```

2. Crie o banco e as tabelas (rodando o script SQL):
   ```sql
   SOURCE sql/criar_tabelas.sql;
   ```

3. Gere os dados simulados:
   ```bash
   python scripts/gerar_dados.py
   ```

4. Carregue os CSVs no banco (ou via Workbench):
   ```bash
   python scripts/carregar_dados.py
   ```

5. Abra o Power BI → Conecte ao banco → Importe o dashboard (`powerbi/dashboard.pbix`).

---

## 💡 Possíveis Melhorias  
- Automatizar o pipeline com Airflow ou Python ETL  
- Criar views otimizadas no MySQL  
- Adicionar novas fontes de dados (ex: API de frete ou marketing)  
- Publicar o dashboard no Power BI Service  

---

## 🧠 Autor  
**Jean Paul Cézanne Silva Borja**  
📚 Estudante de Sistemas de Informação e apaixonado por dados.  
🔗 [LinkedIn](https://www.linkedin.com/in/jean-paul-c%C3%A9zanne-silva-borja) | [GitHub](https://github.com/Cezanne369)

---

## 🪪 Licença  
Este projeto está sob a licença **MIT**.  
Sinta-se à vontade para estudar, modificar e compartilhar. 🚀
