"""
metrics.py
-----------
Funções utilitárias para visualização de métricas:

- plot_confusion_matrix: gráfico elegante da matriz de confusão
- print_classification_report: imprime resultados organizados
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_confusion_matrix(cm, labels=None, title="Matriz de Confusão"):
    """
    Plota a matriz de confusão usando Seaborn.

    Parameters
    ----------
    cm : array-like
        Matriz de confusão gerada pelo sklearn.
    labels : list[str]
        Lista com nomes das classes.
    title : str
        Título do gráfico.
    """

    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
                xticklabels=labels, yticklabels=labels)
    plt.title(title)
    plt.xlabel("Predição")
    plt.ylabel("Verdadeiro")
    plt.tight_layout()
    plt.show()


def print_metrics(results: dict):
    """
    Exibe as métricas de avaliação em formato organizado.

    Parameters
    ----------
    results : dict
        Dicionário retornado pelo evaluate_model().
    """

    print("\n====== MÉTRICAS DE AVALIAÇÃO ======")
    print(f"Accuracy :  {results['accuracy']:.4f}")
    print(f"Precision: {results['precision']:.4f}")
    print(f"Recall   : {results['recall']:.4f}")
    print(f"F1 Score : {results['f1']:.4f}")
    print("===================================\n")
