# 📌 Predicting Congenital Syphilis Cases — Pipeline Completo e Reprodutível

**Autores:** Henrique L. Q. Guimarães • Guilherme A. A. Corrêa • Gustavo H. M. Laporte • Paulo H. C. Portella  
**Instituição:** Cesar School — Ciência da Computação — Turma 6A — 2025.2

---

## 📄 Resumo

Este projeto implementa um **pipeline completo de aprendizado de máquina, inteiramente containerizado**, para reprodução, avaliação crítica e extensão do artigo *Predicting Congenital Syphilis Cases* (2023).

O pipeline integra as seguintes tecnologias para cobrir todo o ciclo ML:
* **Ingestão:** `FastAPI`
* **Armazenamento:** `MinIO/S3`
* **Processamento/Modelagem:** `JupyterLab`
* **Estruturação dos Dados:** `SQLite / PostgreSQL / Snowflake`
* **Rastreamento de Experimentos:** `MLFlow`
* **Dashboards Online:** `ThingsBoard + Trendz`

Os experimentos reproduziram rigorosamente a metodologia original, confirmando sua dificuldade e destacando os modelos **AdaBoost** e **SVM**, que atingiram **F1-Score próximo de 63%**.

---

## 🧠 Abstract (English)

This project delivers a **fully containerized, reproducible machine learning pipeline** for replicating and extending the scientific article *Predicting Congenital Syphilis Cases*. The system integrates `FastAPI`, `MinIO/S3`, `MLFlow`, `JupyterLab`, and `ThingsBoard`, covering ingestion, storage, processing, modeling, experiment tracking, and dashboard visualization. Results confirm the challenges of predicting congenital syphilis and highlight **AdaBoost** and **SVM** as the most effective models ($\approx 63\%$ F1-score).

---

## 🏗️ Arquitetura do Pipeline

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Ingestão** | `FastAPI` | Upload e versionamento dos arquivos |
| **Armazenamento** | `MinIO (S3)` | Repositório central do pipeline (dados brutos, tratados, modelos) |
| **Banco de Dados** | `SQLite / PostgreSQL / Snowflake` | Tabelas estruturadas e dados intermediários |
| **Processamento** | `JupyterLab` | Limpeza, EDA, modelagem |
| **Orquestração** | `MLFlow` | Registro completo de modelos e métricas |
| **Dashboards** | `ThingsBoard + Trendz` | Visualizações e insights |

---

## 📦 1. Estrutura de Containers

Todos os serviços rodam via **Docker Compose**:

```bash
docker compose up -d
```

## 🌐 **2. Descrição das Camadas**

### **2.1 FastAPI — Ingestão**

Endpoints implementados:

- `POST /upload`
- `GET /list-files`
- `GET /get-file/{id}`

Funções:

- Receber datasets enviados pelos usuários
- Validar estrutura e tamanho dos arquivos
- Enviar os arquivos validados diretamente para o bucket S3 (`raw/`)

---

### **2.2 MinIO — Armazenamento S3**

Buckets utilizados:

```
raw/
processed/
models/
dashboards/
```

O MinIO funciona como o repositório central para:

- Dados brutos
- Dados tratados
- Artefatos de modelagem
- Modelos registrados
- Arquivos de dashboards

---

### **2.3 Banco de Dados — Snowflake / SQLite / PostgreSQL**

Responsável por:

- Estruturar tabelas “limpas” após pré-processamento
- Armazenar versões intermediárias
- Registrar indicadores epidemiológicos
- Servir dados para dashboards e análises externas

---

### **2.4 JupyterLab — Processamento e Modelagem**

Etapas realizadas:

- Análise exploratória (EDA)
- Limpeza e padronização dos dados
- Engenharia de atributos
- Codificação (One-Hot)
- Balanceamento
- Recriação dos **6 datasets** definidos no artigo:
  - IDS, BDS, IODS, BODS, IODDS, BODDS
- Treinamento dos **7 modelos**
- Execução dos **6 experimentos**
- Total de execuções: **126** (com Grid Search)

---

### **2.5 MLFlow — Rastreamento de Experimentos**

Registros incluídos:

- Hiperparâmetros usados em cada modelo
- Métricas: Acurácia, F1-Score, Precisão, Sensibilidade
- Matriz de confusão
- Artefatos (modelos, gráficos e logs)
- Comparação automática entre execuções
- Pipeline completamente rastreável e reproduzível

---

### **2.6 ThingsBoard + Trendz — Dashboard Online**

Painéis implementados:

- Evolução temporal dos casos previstos
- Percentual de risco estimado
- Variáveis mais influentes nos modelos
- Gráficos comparativos entre datasets
- Indicadores epidemiológicos gerais e específicos

---

## 🧬 **3. Metodologia**

### **3.1 Dataset**

- Origem: dados reais do Programa Mãe Coruja Pernambucana
- Quantidade inicial:
  - **200k+ registros**
  - **210 atributos**
- Após limpeza e padronização:
  - **41.762 registros**
  - **26 atributos finais**
  - **826 positivos**
  - **40.936 negativos**

---

### **3.2 Pré-Processamento**

Incluiu:

- Remoção de variáveis com >70% de valores ausentes
- Padronização e correção de datas
- Normalização de variáveis numéricas
- Criação de novas features
- Remoção de outliers clínicos atípicos
- Padronização de valores categóricos

---

### **3.3 Balanceamento**

Seguindo o artigo original:

- Técnica usada: **Undersampling**
- Geração dos 6 datasets:
  - IDS, BDS, IODS, BODS, IODDS, BODDS

---

### **3.4 Codificação**

One-Hot Encoding aplicado:

- **26 → 97 variáveis**
- Versões:
  - Com valores “não informado”
  - Sem valores “não informado” (recomendado em alguns experimentos)

---

### **3.5 Seleção de Atributos**

Estratégias utilizadas:

- **SFS (Sequential Forward Selection)** – adiciona features
- **SBS (Sequential Backward Selection)** – remove features
- Seleção baseada em especialistas do PMCP

---

### **3.6 Modelagem**

Modelos utilizados:

- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost
- KNN
- SVM

Otimização:

- Grid Search
- Validação rigorosa conforme metodologia do artigo
- **120+ combinações testadas**

---

## 📊 **4. Resultados**

### **Modelos Finalistas**

| Modelo                   | Dataset | Técnica       | F1-Score   |
| ------------------------ | ------- | ------------- | ---------- |
| **AdaBoost-BODS-Expert** | BODS    | Especialistas | **63.51%** |
| **SVM-BDS-SFA**          | BDS     | SBS           | **63.04%** |

Ambos próximos aos valores do artigo original.

---

### **Principais Achados**

- O desbalanceamento extremo limita sensibilidade de todos os modelos
- Variáveis preenchidas como “não informado” afetam fortemente o desempenho
- AdaBoost apresentou melhor interpretabilidade
- SVM entregou desempenho marginalmente superior
- KNN e Decision Tree tiveram performance inferior

---

## 📈 **5. Dashboards e Insights**

Indicadores disponíveis:

- Distribuição de variáveis chave
- Histórico temporal das previsões
- Variáveis mais importantes de cada modelo
- Comparação entre datasets e técnicas
- Indicadores epidemiológicos do PMCP

---

## 🧪 **6. Conclusões**

O pipeline desenvolvido:

- ✔ Reproduz fielmente a metodologia do artigo
- ✔ Confirma a complexidade do problema
- ✔ Tem rastreamento completo via MLFlow
- ✔ Gera dashboards interpretáveis
- ✔ É modular, replicável e escalável

Melhores modelos:

- **AdaBoost-BODS-Expert**
- **SVM-BDS-SFA**

Ambos com F1 ≈ **63%**.

---

## 🚀 **7. Futuras Melhorias**

- Imputação avançada (MICE, missForest)
- Testar modelos modernos (CatBoost, LightGBM)
- Explicar modelos com SHAP
- Análise geoespacial e temporal
- Pipeline CI/CD para inferência contínua

---

## 🏁 **8. Como Executar o Projeto**

### **1. Clonar o repositório**

```bash
git clone https://github.com/usuario/ml-syphilis-congenita.git
cd ml-syphilis-congenita
```

### **2. Subir os serviços**

```bash
docker compose up -d
```

### **3. Acessar os serviços**

| Serviço       | URL                                                      |
| ------------- | -------------------------------------------------------- |
| FastAPI       | http://localhost:8000/docs                               |
| MinIO Console | http://localhost:9001                                    |
| MLFlow        | http://localhost:5001                                    |
| JupyterLab    | http://localhost:8888                                    |


