# build stage
FROM python:3.13-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /build
COPY requirements.txt ./
RUN pip install --user -r requirements.txt

# -------- runtime stage --------
FROM python:3.13-slim AS runtime
LABEL org.opencontainers.image.source="https://github.com/<your-username>/rag-deepseek"
ENV PATH="/home/appuser/.local/bin:${PATH}"
RUN adduser --disabled-password --uid 1000 appuser && mkdir -p /app
WORKDIR /app
COPY --from=builder /home /home
COPY app/ app/
COPY ml/ ml/
USER appuser
EXPOSE 8501
CMD ["streamlit", "run", "app/ui/main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]