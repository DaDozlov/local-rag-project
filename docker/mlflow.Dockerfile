FROM ghcr.io/mlflow/mlflow:v2.10.1
ENV MLFLOW_TRACKING_URI=http://0.0.0.0:5000
EXPOSE 5000
CMD ["mlflow", "server", "--backend-store-uri", "sqlite:///mlflow.db", "--default-artifact-root", "/mlruns", "--host", "0.0.0.0"]