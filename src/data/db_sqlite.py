# src/data/db_sqlite.py
import os
import sqlite3
from typing import Optional

import pandas as pd

# Caminho padrão do banco
DB_PATH = os.path.join("data", "syphilis.db")
TABLE_NAME = "syphilis_cases"


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """
    Abre (ou cria) uma conexão com o banco SQLite.
    """
    path = db_path or DB_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    return conn


def save_dataframe_to_db(
    df: pd.DataFrame,
    table_name: str = TABLE_NAME,
    db_path: Optional[str] = None,
    if_exists: str = "replace",
) -> None:
    """
    Salva um DataFrame no SQLite, criando a tabela se não existir.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame já pré-processado (features + target).
    table_name : str
        Nome da tabela onde os dados serão gravados.
    db_path : str | None
        Caminho do arquivo .db (se None, usa o default).
    if_exists : str
        Comportamento se a tabela já existir: 'fail', 'replace', 'append'.
    """
    conn = get_connection(db_path)
    try:
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)
    finally:
        conn.close()


def load_dataframe_from_db(
    table_name: str = TABLE_NAME,
    db_path: Optional[str] = None,
) -> pd.DataFrame:
    """
    Lê um DataFrame de uma tabela do SQLite.
    """
    conn = get_connection(db_path)
    try:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)
    finally:
        conn.close()
    return df


def get_table_schema(
    table_name: str = TABLE_NAME,
    db_path: Optional[str] = None,
) -> pd.DataFrame:
    """
    Retorna o schema da tabela (nome das colunas, tipos etc.) para documentar no relatório.
    """
    conn = get_connection(db_path)
    try:
        cursor = conn.execute(f"PRAGMA table_info({table_name})")
        rows = cursor.fetchall()
    finally:
        conn.close()

    return pd.DataFrame(
        rows, columns=["cid", "name", "type", "notnull", "dflt_value", "pk"]
    )
