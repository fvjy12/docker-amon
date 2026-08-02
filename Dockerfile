# ============================================
#  AMON DOCKER - Production Ready
#  Multi-stage build for optimal size & speed
# ============================================

# ---------- Stage 1: Build ----------
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim AS runtime

# Create non-root user for security
RUN useradd -m -u 1000 amon && \
    mkdir -p /app/data && \
    chown -R amon:amon /app

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application
COPY --chown=amon:amon . .

# Switch to non-root user
USER amon

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

# Expose port
EXPOSE 8080

# Run with gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--threads", "2", "main:app"]
