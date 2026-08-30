# 🎮 Catálogo de Jogos API

Projeto desenvolvido para o desafio **Workshop de Backend (Fábrica de Software 26.2)**.

API Django + Django REST Framework para cadastro, organização e avaliação de jogos, com autenticação JWT, documentação Swagger, consumo de API externa (Steam) e ambiente totalmente containerizado com Docker.

## 🚀 Funcionalidades

- CRUD completo de **Jogos**, **Plataformas**, **Gêneros** e **Avaliações**
- Relacionamentos entre entidades (FK e M2M)
- Autenticação via **JWT** (login, refresh token)
- Documentação interativa via **Swagger**
- Página funcional (HTML) para listar jogos e enviar avaliações
- Consumo da **Steam Store API**, com tratamento de erros (timeout, jogo não encontrado, falhas de rede)
- Banco de dados **PostgreSQL**
- Ambiente containerizado com **Docker Compose**

## 🛠️ Tecnologias

- Python 3.13
- Django 6.1 + Django REST Framework
- PostgreSQL 17
- djangorestframework-simplejwt (JWT)
- drf-spectacular (Swagger/OpenAPI)
- Docker & Docker Compose
- requests (consumo de API externa)

## 📦 Como rodar o projeto

Existem duas formas: **via Docker (recomendado)** ou **localmente**.

### Opção 1: Via Docker (recomendado)

**Pré-requisitos:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e em execução.

1. Clone o repositório:
```bash
   git clone https://github.com/joaogabriel33/wsBackendFabricaDeSoftware26.2.git
   cd wsBackendFabricaDeSoftware26.2
```

2. Copie o arquivo de exemplo de variáveis de ambiente e ajuste se necessário:
```bash
   cp .env.example .env
```

3. Suba os containers:
```bash
   docker-compose up --build
```

4. Em um **outro terminal**, aplique as migrations:
```bash
   docker-compose exec web python manage.py migrate
```

5. Crie um superusuário para acessar o Admin:
```bash
   docker-compose exec web python manage.py createsuperuser
```

6. Pronto! Acesse:
   - **Página principal:** http://127.0.0.1:8000/
   - **Admin:** http://127.0.0.1:8000/admin/
   - **Swagger:** http://127.0.0.1:8000/api/schema/swagger-ui/

### Opção 2: Localmente (sem Docker)

**Pré-requisitos:** Python 3.13, PostgreSQL instalado localmente.

1. Clone o repositório e entre na pasta:
```bash
   git clone https://github.com/joaogabriel33/wsBackendFabricaDeSoftware26.2.git
   cd wsBackendFabricaDeSoftware26.2
```

2. Crie e ative o ambiente virtual:
```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
```

3. Instale as dependências:
```bash
   pip install -r requirements.txt
```

4. Crie um banco PostgreSQL local chamado `fabrica_db` com um usuário `fabrica_user`.

5. Copie o `.env.example` para `.env` e preencha com as credenciais do seu banco local.

6. Aplique as migrations:
```bash
   python manage.py migrate
```

7. Crie um superusuário:
```bash
   python manage.py createsuperuser
```

8. Rode o servidor:
```bash
   python manage.py runserver
```

## 📍 Endpoints principais

| Endpoint | Descrição |
|---|---|
| `/` | Redireciona para a página funcional |
| `/api/pagina/jogos/` | Página HTML com lista de jogos e formulário de avaliação |
| `/admin/` | Painel administrativo do Django |
| `/api/schema/swagger-ui/` | Documentação interativa da API |
| `/api/token/` | Obtenção de token JWT (login) |
| `/api/plataformas/`, `/api/generos/`, `/api/jogos/`, `/api/avaliacoes/` | Endpoints CRUD da API |
| `/api/steam/<appid>/` | Busca dados de um jogo na Steam Store, por ID |

## 🗂️ Estrutura do projeto
catalogo/ → App principal (models, views, serializers, forms)
fabrica/ → Configurações do projeto Django
docker-compose.yml → Orquestração dos containers (app + banco)
Dockerfile → Definição da imagem da aplicação
requirements.txt → Dependências Python
.env.example → Modelo de variáveis de ambiente

## 👤 Autor

Desenvolvido por João Gabriel — Fábrica de Software 26.2.
