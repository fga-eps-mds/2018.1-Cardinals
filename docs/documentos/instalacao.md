# Instalação

## Pré requisitos

Estar num ambiente Linux, com os seguintes programas já instalados: Git, Docker e Docker Compose. Consulte: [instalar Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md), [instalar Docker](https://docs.docker.com/install/) e [instalar Docker Compose](https://docs.docker.com/compose/install/) para mais informações.

## Executando a aplicação utilizando Docker num servidor local

1. Clone nosso repositório:

    ``$ git clone https://github.com/fga-gpp-mds/2018.1-Grupo2.git``

2. Entre no diretório do projeto:

    ``$ cd  2018.1-Grupo2/``

3. Inicialize os serviços necessários para aplicação:

    ``$ sudo docker-compose up -d``

4. Acesse a página por meio do seu browser favorito:

    ``htttp:/localhost:8000/``

## Rodando testes

Para avaliar a cobertura de testes localmente utilize os seguintes comandos no terminal do docker:

* Para rodar os testes:

    ``./run_tests.sh``

* Para gerar relatório de cobertura no terminal:

    ``coverage report``

* Para gerar relatório de cobertura em html:

    ``coverage html``
