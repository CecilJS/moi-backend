# Moi 💬

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)
![Docker](https://img.shields.io/badge/docker-enabled-blue)
![License](https://img.shields.io/badge/license-MIT-green)






Moi is a backend service built with FastAPI that provides a simple social networking API. Users can create posts, and other users can comment on those posts. It supports authentication, data persistence, and standard RESTful operations.

## Features

- User authentication and authorization delegated to Azure AD B2C
- Create, read, update, delete (CRUD) posts
- Comment on posts
- PostgreSQL database integration
- Dockerized for containerized deployment
- CI/CD setup with GitHub Actions


## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Docker (optional, for containerized deployment)

### Installation

```bash
git clone https://github.com/your-username/moi.git
cd moi
python -m venv venv
# Activate virtual environment:
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt

### Running Locally
uvicorn moi.main:app --reload
```

> Visit http://127.0.0.1:8000/docs for interactive API documentation.

### Testing
Run unit and integration tests with:

    `pytest`


#### Deployment

- Docker deployment:

    ```bash
    docker build -t moi .
    docker run -p 8000:8000 moi
    ```

> Aside: Infrastructure-as-Code (Terraform) for cloud infrastructure setup and deployment is maintained in a separate repository to enforce isolation and access control best practices.

### Project Structure

```bash
moi/
├─ auth/                # Azure B2C integration: token validation, role checks
├─ main.py              # Application entrypoint
├─ api/                 # API routes (users, posts, comments)
├─ core/                # Core configurations
├─ models/              # Database models (Post, Comment)
├─ schemas/             # Pydantic schemas
├─ services/            # Business logic / services
├─ tests/               # Unit & integration tests
```

### Contributing

> Contributions are welcome! Please follow the standard Git workflow: fork → branch → commit → pull request.

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)