# 📌 Predicting Congenital Syphilis Cases — Pipeline Completo e Reprodutível

**Autores:** Henrique L. Q. Guimarães • Guilherme A. A. Corrêa • Gustavo H. M. Laporte • Paulo H. C. Portella  
**Instituição:** Cesar School — Ciência da Computação — Turma 6A — 2025.2

---

## 📄 Resumo

Este projeto implementa um **pipeline completo de aprendizado de máquina, inteiramente containerizado**, para reprodução, avaliação crítica e extensão do artigo *Predicting Congenital Syphilis Cases* (2023). O pipeline cobre todo o ciclo ML/MLOps, desde a ingestão até a visualização.

Os experimentos reproduziram rigorosamente a metodologia original, confirmando sua dificuldade e destacando os modelos **AdaBoost** e **SVM**, que atingiram **F1-Score próximo de 63%** em datasets balanceados.

---

## 🧠 Abstract (English)

This project delivers a **fully containerized, reproducible machine learning pipeline** for replicating and extending the scientific article *Predicting Congenital Syphilis Cases*. The system integrates `FastAPI`, `MinIO/S3`, `MLFlow`, `JupyterLab`, and `ThingsBoard`, covering ingestion, storage, processing, modeling, experiment tracking, and dashboard visualization. Results confirm the challenges of predicting congenital syphilis and highlight **AdaBoost** and **SVM** as the most effective models ($\approx 63\%$ F1-score).

---

## 🏗️ Arquitetura do Pipeline

A arquitetura é modular e orquestrada via **Docker Compose**, garantindo reprodutibilidade em qualquer ambiente.

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Ingestão** | `FastAPI` | API REST para Upload e versionamento dos arquivos |
| **Armazenamento** | `MinIO (S3)` | Repositório central de artefatos (dados brutos, tratados, modelos) |
| **Banco de Dados** | `SQLite / PostgreSQL / Snowflake` | Tabelas estruturadas e dados intermediários |
| **Processamento** | `JupyterLab` | Limpeza, EDA, modelagem e scripts de treinamento |
| **Orquestração** | `MLFlow` | Registro completo de modelos, métricas e comparação de experimentos |
| **Dashboards** | `ThingsBoard + Trendz` | Visualizações interativas e insights online |

---

## ⚡ Passo a Passo para Rodar o Pipeline (MLOps)

Todo o ambiente de desenvolvimento e produção é isolado e iniciado com um único comando.

### 1️⃣ Clonar o Repositório

```bash
git clone [https://github.com/usuario/ml-syphilis-congenita.git](https://github.com/usuario/ml-syphilis-congenita.git)
cd ml-syphilis-congenita
```
## 🌐 **2. Descrição das Camadas**

### **2.1 FastAPI — Ingestão**

| Endpoint | Método | Função |
| :--- | :--- | :--- |
| `POST /upload` | `POST` | Receber datasets, validar estrutura e enviar diretamente para o bucket S3 (`raw/`). |
| `GET /list-files` | `GET` | Listar arquivos disponíveis para download. |
| `GET /get-file/{id}` | `GET` | Baixar um arquivo específico pelo nome/ID. |

**Funções:**
* Receber datasets enviados pelos usuários.
* Validar estrutura e tamanho dos arquivos.
* Enviar os arquivos validados diretamente para o bucket S3 (`raw/`).

---

### **2.2 MinIO — Armazenamento S3**

O MinIO atua como o **repositório central do Data Lake**.

| Bucket | Conteúdo |
| :--- | :--- |
| `syphilis-datasets` | Dados brutos (`raw/`) após ingestão via FastAPI. |
| `processed` | Dados limpos, balanceados, codificados e prontos para modelagem. |
| `models` | Modelos registrados e artefatos de treinamento (logs, gráficos). |
| `dashboards` | Arquivos de configuração e dados para visualização. |

---

### **2.3 Banco de Dados — Snowflake / SQLite / PostgreSQL**

**Responsável por:**
* Estruturar tabelas “limpas” após o pré-processamento.
* Armazenar versões intermediárias e dados para *reproducibility checks*.
* Registrar indicadores epidemiológicos para consulta rápida.
* Servir dados estruturados para dashboards e análises externas.

---

### **2.4 JupyterLab — Processamento e Modelagem**

**Etapas realizadas:**
* **Análise Exploratória (EDA):** Entendimento e visualização dos dados.
* **Limpeza e Padronização:** Tratamento de valores ausentes, correção de tipos.
* **Engenharia de Atributos:** Criação de *features* e Codificação (One-Hot).
* **Balanceamento:** Aplicação da técnica **Undersampling**.
* **Criação dos 6 Datasets:** Recriação dos conjuntos de dados definidos no artigo (IDS, BDS, IODS, BODS, IODDS, BODDS).
* **Treinamento:** Execução dos **7 modelos** e **6 experimentos**, totalizando **126 execuções** (incluindo *Grid Search*).

---

### **2.5 MLFlow — Rastreamento de Experimentos**

O MLFlow garante a rastreabilidade completa e a reprodutibilidade dos resultados.

**Registros incluídos:**
* **Hiperparâmetros:** Usados em cada *run* de treinamento.
* **Métricas:** Acurácia, F1-Score, Precisão, Sensibilidade.
* **Artefatos:** Matriz de confusão, modelos serializados e logs.
* **Funcionalidade:** Comparação automática entre execuções e *deployment* de modelos.

---

### **2.6 ThingsBoard + Trendz — Dashboard Online**

**Painéis implementados:**
* Evolução temporal dos casos previstos.
* Percentual de risco estimado.
* Visualização das variáveis mais influentes (importância de *features*).
* Gráficos comparativos de desempenho entre os 6 datasets.
* Indicadores epidemiológicos gerais e específicos do PMCP.

## 🧬 **3. Metodologia**

### **3.1 Dataset**

Os dados utilizados são a base para a reprodução rigorosa do artigo científico.

* **Origem:** Dados reais do **Programa Mãe Coruja Pernambucana (PMCP)**.
* **Quantidade Inicial:**
    * **200k+ registros**
    * **210 atributos**
* **Quantidade Final (Pós-limpeza):**
    * **41.762 registros**
    * **26 atributos finais**
    * **Distribuição da Variável Alvo:**
        * **826 positivos**
        * **40.936 negativos** (Extremo desbalanceamento)

---

### **3.2 Pré-Processamento**

Etapas essenciais para garantir a qualidade e comparabilidade dos dados:

* Remoção de variáveis com mais de 70% de valores ausentes.
* Padronização e correção de formato de datas.
* Normalização de variáveis numéricas.
* Criação de novas *features* baseadas em dados clínicos e demográficos.
* Remoção de *outliers* clínicos atípicos para evitar ruído.
* Padronização de valores categóricos (e.g., correção de *typos*).

---

### **3.3 Balanceamento**

Seguindo estritamente a metodologia do artigo para mitigar o desbalanceamento:

* **Técnica usada:** **Undersampling** (Remoção da maioria de registros negativos).
* **Geração dos 6 Datasets:** A combinação de diferentes conjuntos de atributos e codificações gerou as seis bases de teste:
    * IDS, BDS, IODS, BODS, IODDS, BODDS

---

### **3.4 Codificação**

Ajuste das variáveis categóricas para o treinamento dos modelos:

* **Técnica:** **One-Hot Encoding** aplicada às variáveis categóricas.
* **Resultado:** O número de variáveis cresceu de **26 → 97 variáveis**.
* **Versões:** Foram testadas versões com e sem a inclusão de valores “não informado” como uma categoria separada.

---

### **3.5 Seleção de Atributos**

Estratégias para otimizar o desempenho do modelo e a interpretabilidade:

* **SFS (Sequential Forward Selection):** Adiciona *features* iterativamente.
* **SBS (Sequential Backward Selection):** Remove *features* iterativamente.
* **Seleção Baseada em Especialistas:** Utilização do conhecimento de profissionais do PMCP para definir o conjunto de *features* mais clinicamente relevantes.

---

### **3.6 Modelagem**

O treinamento e otimização foram registrados integralmente no MLFlow.

* **Modelos Utilizados:**
    * Decision Tree
    * Random Forest
    * AdaBoost
    * Gradient Boosting
    * XGBoost
    * KNN
    * SVM
* **Otimização:**
    * **Grid Search** para ajuste fino de hiperparâmetros.
    * **Validação Rigorosa** em conjunto de teste separado.
    * Total de **120+ combinações testadas** para encontrar o melhor F1-Score.

    ## 📊 **4. Resultados**

Os resultados confirmaram a complexidade inerente à previsão de sífilis congênita, dada a extrema raridade da classe positiva. O rastreamento completo das execuções e métricas está disponível no **MLFlow** (`http://localhost:5001`).

---

### **Modelos Finalistas**

Os modelos a seguir atingiram os melhores resultados de **F1-Score**, a métrica de prioridade clínica que equilibra Precisão (relevância dos positivos) e Sensibilidade (cobertura dos positivos).

| Modelo | Dataset | Técnica de Seleção de Atributos | F1-Score |
| :--- | :--- | :--- | :--- |
| **AdaBoost-BODS-Expert** | BODS | Especialistas (PMCP) | **63.51%** |
| **SVM-BDS-SFA** | BDS | SBS (Seleção Backward) | **63.04%** |

> Ambos os modelos reproduziram fielmente o desempenho do artigo original, validando a metodologia do pipeline.

---

### **Principais Achados e Limitações**

* **Impacto do Desbalanceamento:** O desbalanceamento extremo na variável alvo ($\approx 1:50$) limitou a **Sensibilidade** (Recall) de todos os modelos. Mesmo os melhores modelos tendem a ter dificuldade em identificar *todos* os casos positivos.
* **Variáveis Ausentes:** A presença de variáveis preenchidas como **“não informado”** afetou fortemente o desempenho de muitos modelos, indicando a necessidade de estratégias de imputação mais robustas (MICE, *missForest*) no futuro.
* **Interpretabilidade vs. Performance:** O **AdaBoost** apresentou a melhor combinação de interpretabilidade (capacidade de explicar as decisões) e desempenho. O **SVM** entregou um desempenho marginalmente superior, mas com menor interpretabilidade.
* **Performance Inferior:** Os modelos **KNN** e **Decision Tree** apresentaram performance significativamente inferior em comparação com os modelos de *ensemble* (AdaBoost, Gradient Boosting).

## 📈 **5. Dashboards e Insights**

A camada de visualização em **ThingsBoard + Trendz** transforma os resultados dos modelos e os dados epidemiológicos em insights acionáveis e compreensíveis.

**Indicadores Disponíveis:**

* **Distribuição de Variáveis Chave:** Visualização da frequência e impacto das principais *features* no resultado.
* **Histórico Temporal das Previsões:** Evolução dos casos previstos ao longo do tempo.
* **Variáveis Mais Importantes:** Gráficos de importância de *features* para cada modelo finalista.
* **Comparação de Desempenho:** Visualização lado a lado do F1-Score, Precisão e Sensibilidade para diferentes datasets e modelos.
* **Indicadores Epidemiológicos:** Dados gerais e específicos do Programa Mãe Coruja Pernambucana (PMCP).

---

## 🧪 **6. Conclusões**

O projeto validou a metodologia proposta no artigo e construiu um pipeline MLOps completo, modular e pronto para produção/extensão.

**Pontos-Chave do Pipeline:**

* ✔ **Reprodução Fiel:** A metodologia do artigo foi replicada integralmente, incluindo a criação dos 6 datasets e a aplicação das técnicas de balanceamento.
* ✔ **Rastreamento Completo:** Todo o ciclo de experimentação e métricas está registrado no **MLFlow**.
* ✔ **Modularidade e Escalabilidade:** A arquitetura containerizada permite que o projeto seja replicado e expandido facilmente.

**Melhores Modelos (F1-Score $\approx 63\%$):**

* **AdaBoost-BODS-Expert**
* **SVM-BDS-SFA**

---

## 🚀 **7. Futuras Melhorias**

O pipeline está estabelecido e pode ser aprimorado nas seguintes áreas:

* **Imputação Avançada:** Implementar métodos mais sofisticados de tratamento de dados ausentes, como MICE (*Multiple Imputation by Chained Equations*) ou *missForest*.
* **Testar Modelos Modernos:** Incluir **CatBoost** e **LightGBM**, conhecidos por lidar bem com dados categóricos e grandes volumes.
* **Explicabilidade (XAI):** Utilizar a biblioteca **SHAP** para entender e justificar as predições de modelos complexos (e.g., AdaBoost, XGBoost).
* **Análise Geoespacial e Temporal:** Integrar a dimensão espacial e temporal para predições mais ricas.
* **Pipeline CI/CD:** Configurar um *workflow* de Integração/Entrega Contínua para automatizar a inferência contínua e a atualização de modelos.

---

## 🏁 **8. Como Executar o Projeto**

Este guia rápido permite que qualquer usuário inicie o pipeline completo em poucos minutos.

### **1. Clonar o repositório**

```bash
git clone [https://github.com/usuario/ml-syphilis-congenita.git](https://github.com/usuario/ml-syphilis-congenita.git)
cd ml-syphilis-congenita
```

### **2. Subir os serviços**

Todos os serviços rodam via **Docker Compose** e são iniciados em segundo plano (`-d`):

```bash
docker compose up -d
```
### **3. Acessar os serviços**

| Serviço | URL | Observação |
| :--- | :--- | :--- |
| **FastAPI** | `http://localhost:8000/docs` | API para ingestão de datasets e download de arquivos. |
| **MinIO Console** | `http://localhost:9001` | **Login:** admin / admin12345. Gerenciamento S3. |
| **MLFlow** | `http://localhost:5001` | Console de rastreamento de experimentos (métricas e modelos). |
| **JupyterLab** | `http://localhost:8888` | Ambiente para rodar os notebooks de pré-processamento e treinamento. |
