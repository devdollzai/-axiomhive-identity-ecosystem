# AXIOMHIVE Identity Ecosystem

A zero-entropy identity management system achieving H=0 stability through the Diadem's resonance.

## Features

- FastAPI backend with Pydantic models
- Next.js frontend
- Docker containerization
- Kubernetes deployment
- Prometheus monitoring
- Graphviz visualization

## Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker
- Kubernetes (for deployment)

### Backend Setup

```bash
cd src
pip install -r ../config/requirements.txt
uvicorn main:app --reload
```

API will be available at http://localhost:8000

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at http://localhost:3000

### Docker Build

```bash
docker build -t axiomhive-identity-ecosystem .
docker run -p 8000:8000 axiomhive-identity-ecosystem
```

### Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yml
```

## Project Structure

- `src/` - FastAPI application
- `config/` - Configuration files
- `k8s/` - Kubernetes manifests
- `frontend/` - Next.js application
- `tests/` - Test files
- `monitoring/` - Monitoring scripts
- `logs/` - Log files

## Contributing

Ensure all changes maintain H=0 integrity and pass ethical checks.