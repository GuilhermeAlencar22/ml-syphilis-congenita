"""
train.py
--------
Pipeline completo de treinamento para o modelo de Sífilis Congênita.

Inclui:
- tratamento de AGE
- divisão treino/teste
- preprocessamento (imputação + one hot + scaling)
- RandomForest dentro do Pipeline
- salvamento do modelo final

Uso:
    from src.models.train import train_model
    model, X_test, y_test = train_model(df)
"""

import os
import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier


def train_model(df: pd.DataFrame, target_col="VDRL_RESULT",
                save_path="models/best_model_rf.pkl"):
    """
    Treina o modelo completo (preprocessamento + RandomForest).

    Parameters
    ----------
    df : pd.DataFrame
        Dataset completo, contendo features + target.
    target_col : str
        Nome da coluna target.
    save_path : str
        Caminho do arquivo para salvar o modelo.

    Returns
    -------
    model : Pipeline
        Pipeline completo (preprocessamento + modelo).
    X_test : pd.DataFrame
    y_test : pd.Series
    """

    # ======== Tratamento especial de AGE (compatível com notebook) ========
    df = df.copy()
    df.loc[df["AGE"] < 0, "AGE"] = np.nan
    df["AGE"] = df["AGE"].fillna(df["AGE"].median())

    # ======== Separar X e y ========
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Colunas numéricas e categóricas (compatível com notebook)
    numeric_cols = ["AGE", "NUM_RES_HOUSEHOLD", "NUM_LIV_CHILDREN",
                    "NUM_ABORTIONS", "NUM_PREGNANCIES"]

    categorical_cols = [c for c in X.columns if c not in numeric_cols]

    print("\n[INFO] Colunas numéricas:", numeric_cols)
    print("[INFO] Colunas categóricas:", len(categorical_cols))

    # ======== Pré-processamento ========
    preprocess = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ]), numeric_cols),

            ("cat", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ]), categorical_cols)
        ]
    )

    # ======== Divisão treino/teste ========
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # ======== Modelo ========
    rf_clf = RandomForestClassifier(
        n_estimators=500,
        random_state=42,
        class_weight="balanced",
    )

    # ======== Pipeline final ========
    model = Pipeline([
        ("preprocess", preprocess),
        ("model", rf_clf)
    ])

    # ======== Treinar ========
    model.fit(X_train, y_train)

    print("\n[OK] Modelo treinado!")
    print(f"Acurácia treino: {model.score(X_train, y_train):.4f}")

    # ======== Salvar ========
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)

    print(f"[OK] Modelo salvo em {save_path}")

    return model, X_test, y_test
