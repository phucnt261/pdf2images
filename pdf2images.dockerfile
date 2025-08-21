FROM python:3.10-slim

# Install poppler for pdf2image
RUN apt-get update && apt-get install -y poppler-utils && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Default PORT (fallback = 8000 if not set by Railway/Render)
ENV PORT=8000

# Run server (use $PORT if provided by Railway/Render)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
