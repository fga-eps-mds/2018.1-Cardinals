# Falko

## Sobre o projeto
O Falko é uma aplicação web para gestão de equipes ágeis. O objetivo do Falko é auxiliar membros de equipes ágeis, em particular os gestores, a monitorar o desenvolvimento de projetos a partir de informações que estão bem próximas do desenvolvimento: o próprio Git. Os projetos serão monitorados em nívels de repositório (issues, branches, pull requests), a nível de boas práticas (testes, análise estática de código, Docker) e a um nível de pessoas (como cada pessoa está contribuindo com o projeto?).

## Guia de Uso do Docker

### Pré requisitos
Ter instalado Docker e Docker Compose. Consulte [instalar Docker](https://docs.docker.com/install/) e [instalar Docker Compose](https://docs.docker.com/compose/install/) para mais informações.

### Comandos básicos para utilização do ambiente
Criar e inicializar containers em background:

```docker-compose up -d```

Criar e inicializar containers com visualização de logs:

```docker-compose up```

Parar containers:

```docker-compose stop```

Religar containers parados:

```docker-compose start```

Listar todos os containers:

```docker ps -a```

Listar apenas containers em execução:

```docker ps```

Executar comando dentro do container:

```docker-compose exec nome_do_container  comando_desejado```

Abrir bash do container:

```docker-compose exec -it  nome_do_container  bash```

## Desenvolvedores
Os desenvolvedores podem ser contatados a partir deste [link](https://github.com/fga-gpp-mds/2018.1-Grupo2/wiki).

## Contribuir para o projeto
Por favor, leia [Contribuição](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/CONTRIBUTING.md) e [Código de Conduta](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/CODE_OF_CONDUCT.md) para mais detalhes sobre nosso código de conduta e orientações para envio de pull requests.

## Documentação
A documentação deste projeto pode ser acessada através da Wiki ([aqui](https://github.com/fga-gpp-mds/2018.1-Grupo2/wiki)).

## Licença
Este projeto é distribuído sob a licença MIT. Para mais detalhes consulte [LICENSE.md](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/LICENSE).
