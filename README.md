# 🔗 Encurtador de URLs (URL Shortener API)

Uma API RESTful para encurtamento de URLs desenvolvida em Python com **FastAPI**, **SQLAlchemy** e **PostgreSQL**. O projeto utiliza a estratégia de conversão em **Base62** a partir da chave primária auto-incremental do banco de dados, garantindo URLs extremamente curtas e sem riscos de colisão.

---

## 🚀 Tecnologias Utilizadas

- **[Python 3.11+](https://www.python.org/)**
- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno e de alta performance.
- **[SQLAlchemy 2.0](https://www.sqlalchemy.org/)**: ORM para mapeamento e manipulação de dados.
- **[PostgreSQL](https://www.postgresql.org/)**: Banco de dados relacional.
- **[Alembic](https://alembic.sqlalchemy.org/)**: Ferramenta de gerenciamento de migrações de banco de dados.
- **[Docker & Docker Compose](https://www.docker.com/)**: Containerização do ambiente de desenvolvimento.
- **[pybase62](https://github.com/aaron-ng/pybase62)**: Algoritmo para codificação de IDs em strings alfanuméricas curtas.

---

## 🛠️ Arquitetura e Lógica do Encurtamento

1. O cliente envia uma URL original via requisição `POST`.
2. A API salva o registro no banco de dados e o PostgreSQL atribui um `id` auto-incremental (ex: `1052`).
3. O `id` numérico é capturado via `db.flush()` e codificado para **Base62** (ex: `1052` $\rightarrow$ `gW`).
4. O código gerado (`short_code`) é persistido no banco e retornado ao cliente.
5. Ao acessar a rota `GET /{short_code}`, a API busca o registro e redireciona o usuário para a URL original via HTTP 307/302.

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
- [Git](https://git-scm.com)
- [Docker](https://www.docker.com/get-started) e **Docker Compose**

---

## 🔧 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
- [Git](https://git-scm.com)
- [Docker](https://www.docker.com/) e **Docker Compose**
- [Python 3.11+](https://www.python.org/) *(caso vá rodar a API fora do container)*

### 2. Clonar o Repositório
Use o git clone com o link do repositorio


### 3. Config .env
Crie um arquivo .env na raiz do projeto com a URL de conexão do PostgreSQL:
 - DATABASE_URL=postgresql://postgres:postgres@localhost:5432/shorturl_db


### 4. Subir um banco no Docker
 - docker compose up -d


### 5. Subir o Alembic e criar a tabela

 # Garanta que a base do Alembic está sincronizada
 alembic stamp head

 # Gere o arquivo de migration (caso não tenha gerado)
 alembic revision --autogenerate -m "create short_urls table"

 # Aplique as tabelas no PostgreSQL
 alembic upgrade head


### 6. Rodando Localmente com Ambiente Virtual
 # Criar e ativar a venv
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
 # .venv\Scripts\activate   # Windows

 # Instalar as dependências
    pip install -r requirements.txt

 # Subir a aplicação com Uvicorn
    uvicorn src.main:app --reload