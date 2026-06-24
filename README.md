# Moi 💬

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)
![Docker](https://img.shields.io/badge/docker-enabled-blue)
![License](https://img.shields.io/badge/license-MIT-green)






> Moi is a backend service built with FastAPI that provides a simple social networking API. Users can create and comment or react on posts. It aims to demonstrate a keen appreciation for security building blocks like authentication, authorization, data integrity and persistence, and standard RESTful operations.


> Aside: Infrastructure-as-Code (Terraform) for cloud infrastructure setup and deployment is maintained in a separate repository to enforce isolation and access control best practices.

### Project Structure

```bash
moi/
├─ auth/                # Azure B2C integration: token validation, role checks
├─ main.py              # Application entrypoint
├─ routes/                 # API routes (users, endpoints, comments)
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