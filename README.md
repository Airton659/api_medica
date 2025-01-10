# API de Gerenciamento de Consultas Médicas

Este projeto é uma API RESTful para gerenciamento de consultas médicas, desenvolvida com Django e Django Rest Framework.

## 🚀 Tecnologias Utilizadas

- Python 3.12
- Django 5.1.4
- Django Rest Framework
- PostgreSQL
- Docker e Docker Compose
- Poetry para gerenciamento de dependências

## 🛠️ Arquitetura

O projeto segue uma arquitetura REST, com as seguintes características:

- **Models**: Representação das entidades do sistema (Profissional e Consulta)
- **Views**: Utilizando ViewSets do DRF para operações CRUD
- **Serializers**: Conversão de dados entre Python e JSON
- **Filters**: Implementação de filtros para consultas
- **Docker**: Containerização da aplicação e banco de dados

## 🔧 Configuração do Ambiente

### Pré-requisitos

- Docker
- Docker Compose
- Git

### Instalação

1. Clone o repositório:
```bash
git clone [https://github.com/Airton659/api_medica.git]
cd api_medica
```

2. Construa e inicie os containers:
```bash
docker-compose up --build
```

3. Execute as migrações:
```bash
docker-compose exec web poetry run python manage.py migrate
```

## 📝 Uso da API

### Endpoints Disponíveis

#### Profissionais
- `GET /api/profissionais/`: Lista todos os profissionais
- `GET /api/profissionais/{id}/`: Recupera detalhes de um profissional específico
- `POST /api/profissionais/`: Cadastra um novo profissional
- `PUT /api/profissionais/{id}/`: Atualiza dados de um profissional
- `DELETE /api/profissionais/{id}/`: Remove um profissional

#### Consultas
- `GET /api/consultas/`: Lista todas as consultas
- `GET /api/consultas/?profissional_id={id}`: Lista todas as consultas de um profissional específico
- `POST /api/consultas/`: Agenda uma nova consulta
- `GET /api/consultas/{id}/`: Recupera uma consulta específica
- `PUT /api/consultas/{id}/`: Atualiza uma consulta
- `DELETE /api/consultas/{id}/`: Remove uma consulta

### Exemplos de Requisições

1. Criar um novo profissional:
```bash
curl -X POST http://localhost:8000/api/profissionais/ \
     -H "Content-Type: application/json" \
     -d '{
       "nome_completo": "Dr. João Silva",
       "nome_social": "Dr. João",
       "profissao": "Cardiologista",
       "endereco": "Rua das Flores, 123",
       "contato": "(11) 99999-9999"
     }'
```

2. Criar uma nova consulta:
```bash
curl -X POST http://localhost:8000/api/consultas/ \
     -H "Content-Type: application/json" \
     -d '{
       "data": "2025-01-10T10:00:00Z",
       "profissional": "Dr. João Silva"
     }'
```

3. Listar consultas de um profissional específico:
```bash
curl http://localhost:8000/api/consultas/?profissional_id=1
```

## ⚙️ Executando os Testes

Para executar os testes unitários:

```bash
docker-compose exec web poetry run python manage.py test
```

### Cobertura de Testes

O projeto inclui testes para as principais funcionalidades:

- Criação de consultas
- Validação de dados
- Relacionamentos entre modelos

## 📦 Estrutura do Projeto

```
api-medica/
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── pyproject.toml
└── README.md
```

## 🤝 Contribuição

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE) - veja o arquivo LICENSE para detalhes.
