import pandas as pd
import os
import re
from unidecode import unidecode

# 📁 Caminho da pasta onde estão os arquivos CSV
CSV_FOLDER = r"C:\Users\Jean\Desktop\cursos_alura\projeto_loja_online\data"

# 📄 Nome do arquivo SQL de saída
OUTPUT_SQL_FILE = "insert_data.sql"

# 💾 Nome do banco de dados MySQL
DATABASE_NAME = "loja_online"

# 🗃️ Arquivos CSV a processar (nome_tabela: nome_arquivo)
FILES_TO_PROCESS = {
    "clientes": "clientes.csv",
    "produtos": "produtos.csv",
    "vendas": "vendas.csv"
}


def sanitize_column_names(df):
    """Padroniza nomes de colunas para formato SQL-friendly."""
    df.columns = [unidecode(col.strip().lower().replace(" ", "_")) for col in df.columns]
    return df


def clean_string_columns(df):
    """Remove acentos e caracteres não ASCII das colunas de texto."""
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = (
            df[col]
            .astype(str)
            .apply(lambda x: unidecode(x.strip()) if pd.notna(x) else None)
        )

        # Remove quebras de linha, tabulações e múltiplos espaços
        df[col] = df[col].apply(lambda x: re.sub(r"\s+", " ", x) if x else x)
    return df


def format_value(val):
    """Formata valores para sintaxe SQL (NULL, números e strings com aspas escapadas)."""
    if pd.isna(val):
        return "NULL"
    if isinstance(val, (int, float)):
        return str(val)
    escaped = str(val).replace("'", "''")  # escapa aspas simples
    return f"'{escaped}'"


def generate_insert_sql(table_name, df):
    """Gera comandos INSERT INTO ... VALUES (...)"""
    sql_statements = []

    # Ajusta data_venda, se existir
    if "data_venda" in df.columns:
        df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce").dt.strftime("%Y-%m-%d")

    # Gera os INSERTs linha a linha
    for _, row in df.iterrows():
        columns = ", ".join(df.columns)
        values = ", ".join(format_value(val) for val in row)
        sql_statements.append(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")

    return sql_statements


def main():
    all_sql = [f"USE {DATABASE_NAME};", "\n-- Comandos INSERT gerados automaticamente\n"]

    for table, filename in FILES_TO_PROCESS.items():
        path = os.path.join(CSV_FOLDER, filename)

        if not os.path.exists(path):
            all_sql.append(f"-- ⚠️ ERRO: Arquivo não encontrado → {path}")
            continue

        try:
            print(f"🔹 Processando {filename} ...")

            # Lê CSV com encoding seguro
            df = pd.read_csv(path, encoding="latin1")

            # Limpa e padroniza colunas e textos
            df = sanitize_column_names(df)
            df = clean_string_columns(df)

            # Gera comandos SQL
            insert_statements = generate_insert_sql(table, df)
            all_sql.append(f"\n-- Tabela: {table} ({len(insert_statements)} linhas)")
            all_sql.extend(insert_statements)

            print(f"✅ {len(insert_statements)} linhas geradas para {table}")
        except Exception as e:
            all_sql.append(f"-- ❌ ERRO ao processar {filename}: {e}")
            print(f"❌ Erro ao processar {filename}: {e}")

    # Salva o arquivo SQL final
    with open(OUTPUT_SQL_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(all_sql))

    print(f"\n🎉 Comandos SQL gerados com sucesso em: {os.path.abspath(OUTPUT_SQL_FILE)}")
    print("💡 Execute o arquivo 'insert_data.sql' no seu MySQL Workbench.")


if __name__ == "__main__":
    main()
