# Dockerfile-jenkins

FROM jenkins/jenkins:lts

# Definir o diretório de trabalho no container
WORKDIR /app

# Use o usuário root para instalar pacotes
USER root

# Atualizar os pacotes e instalar o Python3 e o pip
RUN apt-get update

# Copiar o arquivo de requisitos
COPY requirements.txt /app/requirements.txt

# Instalar as dependências do Python
RUN rm -rf /var/lib/apt/lists/*

# Retornar ao usuário Jenkins
USER jenkins

# Instalar plugins adicionais do Jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
