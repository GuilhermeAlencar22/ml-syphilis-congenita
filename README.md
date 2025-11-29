🧬 Projeto: Predição de Sífilis Congênita

Integrantes do grupo:

Guilherme Alencar Augusto Corrêa – @GuilhermeAlencar22

Henrique Queiroz Lôbo – @HenriqueQL

Disciplina: Aprendizado de Máquina – 2025.2
Instituição: CESAR School

📖 1. Introdução

O projeto da disciplina Aprendizado de Máquina (AM) tem como objetivo a reprodução e aprimoramento de um artigo científico que explore o uso de técnicas de Machine Learning em um problema real.

Nesta edição, o desenvolvimento foi realizado sobre uma arquitetura moderna em contêineres Docker, integrando as etapas de coleta, processamento, modelagem e visualização em um pipeline executável via Docker Compose.

A implementação abrange as seguintes camadas principais:

Camada

Função

Ingestão (FastAPI)

Recebe e disponibiliza os dados para análise.

Armazenamento (MinIO/S3)

Guarda os dados brutos e modelos treinados.

Modelagem (JupyterLab)

Ambiente para análise exploratória e treinamento de modelos.

Rastreamento (MLflow)

Registro de parâmetros, métricas e artefatos de modelos.

Visualização (Trendz Analytics)

Dashboards interativos com métricas e resultados.

Essa integração visa consolidar as habilidades práticas em ciência de dados aplicada, com foco em reprodutibilidade, documentação e engenharia de aprendizado de máquina.

O projeto reproduz e aprimora o estudo “Predicting Congenital Syphilis Cases: A Performance Evaluation of Different Machine Learning Models” (PLoS ONE, 2022).

🎯 2. Objetivos

Reproduzir e avaliar o desempenho dos modelos apresentados no artigo científico selecionado.

Implementar o estudo dentro de um pipeline executável via Docker Compose.

Integrar todas as camadas da arquitetura de BI e ML (Ingestão, Armazenamento, Modelagem, Rastreamento e Visualização).

Aplicar técnicas de pré-processamento, modelagem supervisionada, avaliação e visualização dos resultados.

Documentar o processo em relatório técnico (mínimo 10 páginas), conforme exigência da disciplina.

⚙️ 3. Arquitetura e Tecnologias

A Figura 1 representa o fluxo do pipeline integrado implementado no projeto, garantindo a rastreabilidade e a reprodutibilidade dos experimentos.

          ┌───────────────┐
          │   FastAPI     │  ← Ingestão via /upload-dataset
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │    MinIO (S3) │  ← Armazena CSVs e modelos
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │   SQLite DB   │  ← Dados tratados (syphilis.db)
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │  JupyterLab   │  ← Modelagem e Treinamento
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │   MLflow UI   │  ← Rastreamento de runs e métricas
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ Trendz/Reports│ ← Visualização e análise final
          └───────────────┘


Figura 1: Arquitetura do pipeline de MLOps para Predição de Sífilis Congênita.

🧩 Serviços em Contêineres

Serviço

Função

Porta

FastAPI

Ingestão de dados e integração com MinIO

8000

MinIO

Armazenamento de dados brutos e modelos

9000 / 9001

SQLite

Banco estruturado local (substitui Snowflake)

Local

JupyterLab

Modelagem e pré-processamento

8888

MLflow

Rastreamento de modelos e métricas

5001

Trendz/Reports

Dashboards e relatórios finais

trendz/, reports/

📊 4. Dataset

Fonte: Mendeley Data – Sífilis Congênita Dataset

Artigo de referência:

Predicting congenital syphilis cases: A performance evaluation of different machine learning models.

PLoS ONE, 2022

Arquivos:

data/raw/data_set.csv – dados brutos das gestantes;

data/raw/attributes.csv – descrição dos atributos.

O dataset foi utilizado exclusivamente para fins acadêmicos.

🧠 5. Estrutura do Repositório

/
├── docker-compose.yml     # Orquestração dos contêineres
├── fastapi/               # API de ingestão (FastAPI + MinIO)
│   └── main.py
├── jupyterlab/            # Ambiente de análise (Dockerfile e configs)
├── mlflow/                # Rastreamento de experimentos
├── data/
│   ├── raw/               # Dados brutos
│   ├── processed/         # Dados tratados
│   └── syphilis.db        # Base estruturada SQLite
├── src/
│   ├── data/              # Scripts de ingestão e pré-processamento
│   └── models/            # Treinamento e avaliação
├── notebooks/             # Notebooks 01–03
├── reports/               # Gráficos e tabelas
├── trendz/                # Dashboards exportados
├── requirements.txt
└── README.md


🚀 6. Execução do Pipeline via Docker Compose

Pré-requisitos

Docker Desktop e Git instalados.

(Opcional) Python 3.11+ para testes locais.

Passos

Clonar o repositório:

git clone [https://github.com/GuilhermeAlencar22/ml-syphilis-congenita.git](https://github.com/GuilhermeAlencar22/ml-syphilis-congenita.git)
cd ml-syphilis-congenita


Construir e levantar a infraestrutura:

docker-compose up --build


Acessar os serviços

Serviço

URL

Função

JupyterLab

http://localhost:8888

Análise e modelagem

FastAPI (Swagger)

http://localhost:8000/docs

Upload de datasets

MinIO Console

http://localhost:9001

Armazenamento S3

MLflow UI

http://localhost:5001

Rastreamento de experimentos

🔐 Credenciais do MinIO:
Usuário: admin
Senha: admin12345

Para encerrar:

docker-compose down


🔄 7. Pipeline de Dados

FastAPI → MinIO: O endpoint /upload-dataset realiza upload de arquivos .csv para o bucket syphilis-datasets.

MinIO → SQLite: O notebook 02-preprocessamento.ipynb faz leitura, limpeza e gravação dos dados no banco data/syphilis.db.

SQLite → Jupyter (Modelagem): O notebook 03-treinamento.ipynb lê os dados estruturados, aplica o modelo Random Forest e registra resultados no MLflow.

MLflow → Trendz/Reports: Resultados e métricas são exportados para reports/ e visualizados em dashboards no Trendz Analytics.

📈 8. Resultados

Modelagem com Random Forest (n_estimators=300, max_depth=12)

Métrica Média

Valor

Accuracy

~0.84

F1-score

~0.81

ROC-AUC

~0.87

Gráficos e métricas exportados para reports/:

Matriz de confusão

Curva ROC e PR

Importância das features

🧩 9. Componentes do Pipeline

Componente

Função

Localização

FastAPI

Ingestão de dados e integração com MinIO

fastapi/main.py

MinIO

Armazenamento de datasets e modelos

minio/

SQLite

Base estruturada local

data/syphilis.db

MLflow

Registro de parâmetros e métricas

mlflow/

Trendz

Visualização de dashboards

trendz/

✅ 10. Itens Entregues

✅ Pipeline completo executável via Docker Compose

✅ API funcional com upload para MinIO

✅ Base estruturada em SQLite

✅ Treinamento com MLflow integrado

✅ Dashboards exportados para Trendz

✅ README e documentação técnica completos

🧑‍🏫 11. Observações Finais

Projeto de caráter acadêmico, sem finalidade diagnóstica.

SQLite foi utilizado no lugar de Snowflake, atendendo ao requisito de base estruturada.

Toda a arquitetura pode ser facilmente migrada para AWS (S3 + RDS + SageMaker + MLflow Tracking Server).

O projeto está pronto para reprodutibilidade e avaliação completa pela banca docente.

📜 Licença

Distribuído sob a licença MIT.

Consulte o arquivo LICENSE para mais detalhes.