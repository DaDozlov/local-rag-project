# Local RAG with DeepSeek‑R1

A **privacy‑first Retrieval‑Augmented‑Generation (RAG)** starter kit that runs completely on your laptop —or on‑prem Kubernetes —using

* **DeepSeek‑R1** (local LLM via **Ollama**)
* **LangChain** orchestration
* **ChromaDB** vector store
* **Streamlit** UI & **FastAPI** HTTP endpoint
* **MLflow** experiment tracking
* Optional **Kubeflow Pipelines** Helm chart for heavy‑duty workflows

---

## Repository layout

```
.
├── app/
│   ├── api/main.py
│   └── ui/main.py
├── docker/
│   ├── app.Dockerfile
│   └── mlflow.Dockerfile
├── infra/k8s/
│   ├── kubeflow/
│   └── ollama/
├── ml/
│   ├── models/rag_model.py
│   ├── pipelines/
│   └── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Quick start (local)

```bash
# 1.  Clone
$ git clone https://github.com/<your-user>/local-rag-project.git
$ cd local-rag-project

# 2.  Install Ollama and pull models
$ curl -fsSL https://ollama.com/install.sh | sh
$ ollama pull deepseek-r1:latest
$ ollama pull mxbai-embed-large

# 3.  Create virtual‑env and install deps
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
$ pip install -e .

# 4.  Launch Streamlit UI (spins up Ollama client under the hood)
$ streamlit run app/ui/main.py
# visit http://localhost:8501
```

---

## Run with Docker

Build the app image (includes all Python code; Ollama runs as a side‑car):

```bash
docker build -f docker/app.Dockerfile -t rag-app:dev .
ollama serve &
CONTAINER_ID=$(docker run -d -p 8501:8501 rag-app:dev)
```

A production‑grade setup would use `docker-compose.yml` or K8s manifests with three services: **ollama**, **rag‑app**, and **mlflow**.

---

## Tests & linting

```bash
pytest -q
black --check .
flake8
mypy ml app
```

All of these run automatically in **GitHub Actions** (see `.github/workflows/ci.yml`).

---

## Experiment tracking

Start MLflow locally:

```bash
docker build -f docker/mlflow.Dockerfile -t mlflow-server:local .
docker run -d -p 5000:5000 -v $(pwd)/mlruns:/mlruns mlflow-server:local
# open http://localhost:5000
```

The `rag_model.py` logs latency, precision and answer quality for each run.

---

## Deploy to Kubernetes (optional)

```bash
# add GPU node‑pool or use a local KIND cluster with GPU pass‑through
helm repo add rag-infra ./infra/k8s
helm install ollama rag-infra/ollama
helm install rag-ui rag-infra/kubeflow
```

Consult `infra/k8s/ollama/values.yaml` to switch between CPU & GPU.

---

## Security

* **Non‑root containers** & minimal `python:3.13-slim` base images.
* `.gitignore` hides `.env`, vector DB, MLflow artefacts, model files.
* [Trivy](https://aquasecurity.github.io/trivy/) scan runs weekly (`security-scan.yml`).
* Dependabot keeps Python & action dependencies patched.

---

## Configuration

Create a `.env` (copy from `.env.example`) to override defaults:

```
OLLAMA_HOST=http://localhost:11434
CHROMA_DIR=./chromadb
PROMPT_TEMPLATE="Answer the question using the context below"
```

All environment variables are read in `ml/models/rag_model.py`.

---

