# Cardinals

<p align="center">
    <image src="docs/images/logo_cardinals.png" width="40%">
</p>

[![Build Status](https://travis-ci.org/fga-gpp-mds/2018.1-Cardinals.svg?branch=master)](https://travis-ci.org/fga-gpp-mds/2018.1-Cardinals)
[![Maintainability](https://api.codeclimate.com/v1/badges/eed50c895d14a830236a/maintainability)](https://codeclimate.com/github/fga-gpp-mds/2018.1-Cardinals/maintainability)
[![Code coverage](https://codecov.io/gh/fga-gpp-mds/2018.1-Cardinals/branch/develop/graph/badge.svg)](https://codecov.io/gh/fga-gpp-mds/2018.1-Cardinals)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Sobre o projeto

<p align="justify">O Cardinals é uma aplicação web para gestão de equipes ágeis. O objetivo do Cardinals é auxiliar membros de equipes ágeis, em particular os gestores, a monitorar o desenvolvimento de projetos a partir de informações que estão bem próximas do desenvolvimento: o próprio Git. Os projetos serão monitorados em nívels de repositório (issues, branches, pull requests), a nível de boas práticas (testes, análise estática de código, Docker) e a um nível de pessoas (como cada pessoa está contribuindo com o projeto?).</p>

## Executando a aplicação

### Pré requisitos

Estar num ambiente Linux, com os seguintes programas já instalados: Git, Docker e Docker Compose. Consulte: [instalar Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md), [instalar Docker](https://docs.docker.com/install/) e [instalar Docker Compose](https://docs.docker.com/compose/install/) para mais informações.

### Executando a aplicação utilizando Docker num servidor local

1. Clone nosso repositório:

    ``$ git clone https://github.com/fga-gpp-mds/2018.1-Grupo2.git``

2. Entre no diretório do projeto:

    ``$ cd  2018.1-Grupo2/``

3. Inicialize os serviços necessários para aplicação:

    ``$ sudo docker-compose up -d``

4. Acesse a página por meio do seu browser favorito:

    ``htttp:/localhost:8000/``

### Rodando testes

Para avaliar a cobertura de testes localmente utilize os seguintes comandos no terminal do docker:

* Para rodar os testes:

    ``./run_tests.sh``

* Para gerar relatório de cobertura no terminal:

    ``coverage report``

* Para gerar relatório de cobertura em html:

    ``coverage html``

## Autores

Veja a lista de contribuidores deste projeto [aqui](https://github.com/fga-gpp-mds/2018.1-Cardinals/graphs/contributors).

## Contribuir para o projeto

Por favor, leia [Contribuição](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/CONTRIBUTING.md) e [Código de Conduta](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/CODE_OF_CONDUCT.md) para mais detalhes sobre nosso código de conduta e orientações para envio de pull requests.

## Documentação

A documentação deste projeto pode ser acessada [aqui](https://github.com/fga-gpp-mds/2018.1-Cardinals/tree/master/docs/documentos).

## Licença

Este projeto é distribuído sob a licença MIT. Para mais detalhes consulte [LICENSE.md](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/LICENSE).
