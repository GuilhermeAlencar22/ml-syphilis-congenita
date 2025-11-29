"""
evaluate.py
-----------
Funções para avaliação do modelo treinado.

Inclui:
- carregamento do modelo completo (pipeline)
- métricas de classificação (accuracy, precision, recall, f1)
- matriz de confusão
- AUC ROC
- Precision–Recall

Uso:
    from src.models.evaluate import evaluate_model
    results = evaluate_model("models/best_model_rf.pkl", X_test, y_test)
"""

import joblib
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
    precision_recall_curve
)


def load_trained_model(model_path="models/best_model_rf.pkl"):
    """Carrega o pipeline completo treinado."""
    return joblib.load(model_path)


def evaluate_model(model_path, X_test, y_test):
    """
    Avalia o modelo treinado com métricas completas.

    Parameters
    ----------
    model_path : str
        Caminho do modelo salvo (.pkl)
    X_test : pd.DataFrame
        Conjunto de teste (não preprocessado)
    y_test : pd.Series

    Returns
    -------
    dict
        Métricas + arrays de curvas
    """

    model = load_trained_model(model_path)

    # Predições
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Métricas
    results = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "auc": roc_auc_score(y_test, y_prob),
        "roc_curve": roc_curve(y_test, y_prob),
        "pr_curve": precision_recall_curve(y_test, y_prob),
    }

    print("\n[RESULTADOS DO MODELO]")
    print(f"Accuracy:  {results['accuracy']:.4f}")
    print(f"Precision: {results['precision']:.4f}")
    print(f"Recall:    {results['recall']:.4f}")
    print(f"F1 Score:  {results['f1']:.4f}")
    print(f"AUC ROC:   {results['auc']:.4f}")
    print("\nMatriz de Confusão:")
    print(results["confusion_matrix"])

    return results
