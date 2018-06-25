# Instalação e Testes

## Pré requisitos

Estar num ambiente Linux, com os seguintes programas já instalados: Git, Docker e Docker Compose. Consulte: [instalar Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md), [instalar Docker](https://docs.docker.com/install/) e [instalar Docker Compose](https://docs.docker.com/compose/install/) para mais informações.

## Executando a aplicação utilizando Docker num servidor local

1. Clone nosso repositório:

    ``$ git clone https://github.com/fga-gpp-mds/2018.1-Cardinals.git``

2. Entre no diretório do projeto:

    ``$ cd  2018.1-Cardinals`

3. Inicialize os serviços necessários para aplicação:

    ``$ sudo make up``

4. Acesse a página por meio do seu browser favorito:

    ``htttp:/localhost:8000/``

## Rodando testes

Para avaliar a cobertura de testes localmente utilize os seguintes comandos no terminal do docker:

* Para rodar os testes:

    ``sudo make test``

## Avaliando a qualidade do código

* Para identificar problemas de estilo e complexidade utilizando o [Flake8](http://flake8.pycqa.org/en/latest/):

    ``sudo make analyze-flake8:``

* Para realizar análises do [Codeclimate](https://docs.codeclimate.com) localmente:
    ``sudo make analyze``

