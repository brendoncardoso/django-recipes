# Use uma imagem base oficial do Python
FROM python:3.10

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do projeto para o diretório de trabalho no contêiner
COPY . .

# Exponha a porta que o Django usará
EXPOSE 8000

# Defina o comando padrão para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]