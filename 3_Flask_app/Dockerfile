FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8010

# Comando para rodar a aplicação
CMD ["python", "app.py"]
