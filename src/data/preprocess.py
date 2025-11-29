"""
preprocess.py
-------------
Funções para pré-processamento do dataset.

Inclui:
- basic_cleaning: tratamento de idades negativas e preenchimento de valores faltantes
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpeza básica no dataset.

    Etapas:
    - Corrige idades negativas
    - Preenche valores faltantes com mediana (numérico) ou moda (categórico)

    Parameters
    ----------
    df : pd.DataFrame
        Dataset original

    Returns
    -------
    pd.DataFrame
        Dataset limpo
    """
    df = df.copy()

    # Corrigir idades negativas
    df.loc[df["AGE"] < 0, "AGE"] = np.nan
    df["AGE"] = df["AGE"].fillna(df["AGE"].median())

    # Outras colunas numéricas podem ser preenchidas depois no pipeline
    return df


def get_preprocessing_pipeline(num_cols: list, cat_cols: list) -> ColumnTransformer:
    """
    Retorna um ColumnTransformer pronto para pré-processamento.

    Parameters
    ----------
    num_cols : list
        Lista de colunas numéricas
    cat_cols : list
        Lista de colunas categóricas

    Returns
    -------
    ColumnTransformer
        Pré-processador completo
    """
    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocess = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, num_cols),
            ("cat", categorical_transformer, cat_cols)
        ]
    )

    return preprocess
