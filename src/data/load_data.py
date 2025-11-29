"""
load_data.py
------------
Funções para carregar datasets de Sífilis Congênita.

Inclui:
- load_csv: carregamento de CSV com verificação de existência
"""

import os
import pandas as pd


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV e retorna como DataFrame.

    Parameters
    ----------
    filepath : str
        Caminho do arquivo CSV.

    Returns
    -------
    pd.DataFrame
        Dataset carregado.
    
    Raises
    ------
    FileNotFoundError
        Se o arquivo não existir.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    try:
        df = pd.read_csv(filepath)
        print(f"[OK] Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
        return df
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar o arquivo {filepath}: {e}")
