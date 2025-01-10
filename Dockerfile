# Usar a imagem oficial do Python como base
FROM python:3.12-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de dependências (pyproject.toml e poetry.lock)
COPY pyproject.toml poetry.lock /app/

# Instalar o Poetry
RUN pip install poetry

# Instalar as dependências do projeto
RUN poetry install --no-root

# Copiar o código do projeto para o contêiner
COPY . /app/

# Expor a porta do Django (padrão 8000)
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
