# Projeto: Predição de Sífilis Congênita

**Integrantes do grupo:**
* Guilherme Alencar Augusto Corrêa – [@GuilhermeAlencar22](https://github.com/GuilhermeAlencar22)
* Henrique Queiroz Lôbo – [@HenriqueQL](#)

**Disciplina:** Aprendizado de Máquina – 2025.2
**Instituição:** CESAR School

---

## 📘 Descrição do Projeto

Este projeto tem como objetivo aplicar técnicas de **aprendizado de máquina** para análise e predição de **Sífilis Congênita**, utilizando dados reais disponíveis publicamente.

O modelo desenvolvido busca auxiliar na **identificação de fatores associados à ocorrência da doença**, com base em dados sociodemográficos e clínicos de gestantes.

---

## 📊 Dataset Utilizado

* **Fonte:** [Mendeley Data – Sífilis Congênita Dataset](https://data.mendeley.com/datasets/3zkcvybvkz/1?authuser=0)
* **Referência científica:** [PLoS ONE – Machine learning models for congenital syphilis prediction](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0276150#abstract0)
* **Arquivos:**
    * `data/raw/data_set.csv`
    * `data/raw/attributes.csv`

> **Nota:** Os dados foram utilizados exclusivamente para fins acadêmicos.

---

## 🧠 Estrutura do Projeto



---

## ⚙️ Execução do Pipeline via Docker Compose

### 🧩 Pré-requisitos

* **Docker Desktop** instalado e em execução.
* **Git** instalado.
* (Opcional) Ambiente Python local com `venv` ativo para inspeções fora do Docker.

---

### 🚀 Passos para execução

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/GuilhermeAlencar22/ml-syphilis-congenita.git](https://github.com/GuilhermeAlencar22/ml-syphilis-congenita.git)
    cd ml-syphilis-congenita
    ```

2.  **Levantar toda a infraestrutura com Docker Compose:**
    ```bash
    docker-compose up --build
    ```

3.  **Acessar os serviços:**

| Serviço | Descrição | URL de acesso |
| :--- | :--- | :--- |
| **JupyterLab** | Ambiente de análise (notebooks) | `http://localhost:8888` |
| **FastAPI** | API de ingestão (Swagger UI) | `http://localhost:8000/docs` |
| **MLflow** | Interface de experimentos | `http://localhost:5001` |

> 💡 Se a porta `5000` já estiver em uso, o MLflow roda em `5001` conforme configuração atual.

4.  **Encerrar os containers:**
    ```bash
    docker-compose down
    ```

---

## 📈 Resultados e Visualizações

* Gráficos de avaliação, curvas **ROC** e **PR**, e **importância das features** são exportados automaticamente para a pasta `reports/`.
* Dashboards interativos podem ser exportados para `trendz/` e visualizados no ThingsBoard/Trendz.

---

## 🧩 Componentes do Pipeline

| Componente | Função | Localização |
| :--- | :--- | :--- |
| **Pré-processamento** | Limpeza e transformação de dados | `src/data/preprocess.py` |
| **Treinamento** | Treinamento do modelo **Random Forest** | `src/models/train.py` |
| **Avaliação** | Métricas, ROC, PR, importância de features | `src/models/evaluate.py` |
| **API** | Interface de predição (**FastAPI**) | `fastapi/main.py` |
| **Experimentação** | Rastreamento de modelos com **MLflow** | `mlflow/` |
| **Dashboards** | Visualização de métricas e resultados | `trendz/` |

---

## 📘 Itens Obrigatórios Entregues

* ✅ Pipeline executável via **Docker Compose**
* ✅ Código-fonte organizado (`src/`, `notebooks/`, `fastapi/`, etc.)
* ✅ Dashboard e relatórios (`reports/`, `trendz/`)
* ✅ README completo com instruções de execução
* ✅ Licença MIT incluída

---

## 🧑‍🏫 Observações Finais

* Este projeto tem fins puramente **acadêmicos**.
* As predições geradas **não substituem avaliação clínica**.
* O dataset e o artigo utilizados são de domínio público e seguem a política de uso do Mendeley Data e PLoS ONE.