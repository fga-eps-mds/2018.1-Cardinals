# Falko

## Sobre o projeto
O Falko é uma aplicação web para gestão de equipes ágeis. O objetivo do Falko é auxiliar membros de equipes ágeis, em particular os gestores, a monitorar o desenvolvimento de projetos a partir de informações que estão bem próximas do desenvolvimento: o próprio Git. Os projetos serão monitorados em nívels de repositório (issues, branches, pull requests), a nível de boas práticas (testes, análise estática de código, Docker) e a um nível de pessoas (como cada pessoa está contribuindo com o projeto?).

## Executando a aplicação

### Pré requisitos
Estar num ambiente Linux, com os seguintes programas já instalados: Git, Docker e Docker Compose. Consulte: [instalar Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md), [instalar Docker](https://docs.docker.com/install/) e [instalar Docker Compose](https://docs.docker.com/compose/install/) para mais informações.

### Executando a aplicação utilizando Docker num servidor local

1. Clone nosso repositório:

    `` $ git clone https://github.com/fga-gpp-mds/2018.1-Grupo2.git ``
    
2. Entre no diretório do projeto:

    `` $ cd  2018.1-Grupo2/ ``

3. Inicialize os serviços necessários para aplicação:

    `` $ sudo docker-compose up -d ``

4. Acesse a página por meio do seu browser favorito:

    `` htttp:/localhost:8000/ `` 


## Desenvolvedores
Os desenvolvedores podem ser contatados a partir deste [link](https://github.com/fga-gpp-mds/2018.1-Grupo2/wiki).

## Contribuir para o projeto
Por favor, leia [Contribuição](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/CONTRIBUTING.md) e [Código de Conduta](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/CODE_OF_CONDUCT.md) para mais detalhes sobre nosso código de conduta e orientações para envio de pull requests.

## Documentação
A documentação deste projeto pode ser acessada através da Wiki ([aqui](https://github.com/fga-gpp-mds/2018.1-Grupo2/wiki)).

## Licença
Este projeto é distribuído sob a licença MIT. Para mais detalhes consulte [LICENSE.md](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/LICENSE).
