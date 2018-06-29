# Instalação e Testes

## Pré requisitos

Estar num ambiente Linux, com os seguintes programas já instalados: Git, Docker e Docker Compose.         
Consulte: [instalar Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md), [instalar Docker](https://docs.docker.com/install/) e [instalar Docker Compose](https://docs.docker.com/compose/install/) para mais informações.

## Executando a aplicação utilizando Docker num servidor local

1. Clone nosso repositório:

~~~~~~~~~~~~~{.sh}
  $ git clone https://github.com/fga-gpp-mds/2018.1-Cardinals.git
~~~~~~~~~~~~~

2. Entre no diretório do projeto:

~~~~~~~~~~~~~{.sh}
  $ cd  2018.1-Cardinals
~~~~~~~~~~~~~

3. Crie um arquivo para as variáveis de ambiente:

~~~~~~~~~~~~~{.sh}
  $ echo -e "USERNAME=\nPASSWORD=\nSECRET_KEY=''\nSOCIAL_AUTH_GITHUB_KEY=\nSOCIAL_AUTH_GITHUB_SECRET=" >> .env
~~~~~~~~~~~~~

Para mais informações sobre as variáveis de ambiente veja o tópico [Variáveis de ambiente](#variaveis-de-ambiente).

3. Inicialize os serviços necessários para aplicação:

~~~~~~~~~~~~~{.sh}
  $ cd  sudo make up
~~~~~~~~~~~~~

4. Acesse a página por meio do seu browser favorito:

~~~~~~~~~~~~~{.sh}
  htttp:/localhost:8000/
~~~~~~~~~~~~~


## Variáveis de ambiente
Para aumentar o limite de requisições use credenciais de autenticação da API do Github. Para mais informações [acesse](https://developer.github.com/v3/?).

```
USERNAME='Meu_username'
PASSWORD='Minha_senha'
```

Adicione sua chave secreta da aplicação.      
Para gerar sua própria chave pode-se utilizar [Django Secret Key Generator](https://www.miniwebtool.com/django-secret-key-generator/) ou [django-secret-keygen.py](django-secret-keygen.py).     
Para mais informações acesse [Documentação Django](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-SECRET_KEY).

    SECRET_KEY='Minha_chave_secreta'

Para utilizar o sistema de login através do Github, utilize as chaves Client ID e Client Secret de uma aplicação do Github.         
Para mais informações acesse [Creating an OAuth App](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/).

    SOCIAL_AUTH_GITHUB_KEY='Minha_Client_ID'
    SOCIAL_AUTH_GITHUB_SECRET='Minha_Client_Secret'

## Rodando testes

Para avaliar a cobertura de testes localmente utilize os seguintes comandos no terminal do docker:

* Para rodar os testes:

~~~~~~~~~~~~~{.sh}
  $ sudo make test
~~~~~~~~~~~~~

## Avaliando a qualidade do código

* Para identificar problemas de estilo e complexidade utilizando o [Flake8](http://flake8.pycqa.org/en/latest/):

~~~~~~~~~~~~~{.sh}
  $ sudo make analyze-flake8
~~~~~~~~~~~~~

* Para realizar análises do [Codeclimate](https://docs.codeclimate.com) localmente:

~~~~~~~~~~~~~{.sh}
  $ sudo make analyze
~~~~~~~~~~~~~
