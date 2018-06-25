# Introdução
Este documento tem como objetivo apresentar o processo de implementação de cultura de DevOps no projeto Cardinals.

## Histórico de Revisão

Data | Versão | Alteração
:--: | :--: | :--:
18/06/2018 | 1.0 | Criação da versão inicial do  documento
19/06/2018 | 1.0 | Atualização do documento

# DevOps

O DevOps é a combinação de desenvolvimento de aplicações e operações, que visa minimizar ou eliminar a desconexão entre desenvolvedores de software que criam aplicações e administradores de sistemas que mantêm a infraestrutura em execução.
O papel de responsável por DevOps no projeto durante o projeto foi ocupado de acordo com a tabela a seguir:

| Alunos (as) | Período |
| :--: | :--: |
| Amanda e Marlon | Início do projeto - Release 1 |
| Amanda | Release 1 - Release 2 |

## Ciclo de vida
+ Planejamento
+ Código
+ Build
+ Teste
+ Integração
+ Deploy
+ Monitoramento

# Planejamento
O planejamento contínuo tem como objetivo dar uma visão comum do desenvolvimento do projeto aos envolvidos, provendo transparência a respeito dos objetivos do projeto, seu andamento e mudanças realizadas ou necessárias ao longo de seu desenvolvimento.

## Github
O Github foi utilizado para adicionar, atualizar e controlar as documentações do projeto relacionadas aos requisitos e do projeto e descrição e transparência da utilização da metodologia ágil no projeto.

### Github issues e Zenhub
Utilizados para:
+ Detalhar os requisitos do projeto em formato de histórias de usuário, incluindo tarefas e critérios de aceitação;
+ Informar bugs e necessidades emergentes do projeto;
+ Controlar o status das histórias, responsáveis, níveis de dificuldade;
+ Gerar estimativas a respeito da conclusão das funcionalidades.

[Monitoramento de issues no Cardinals](https://fga-gpp-mds.github.io/2018.1-Cardinals/documentos/Monitoramento-de-issues-pelo-Zenhub/)
[Zenhub board do Cardinals](https://github.com/fga-gpp-mds/2018.1-Cardinals#boards?repos=124142953)

## Google Drive
Utilizado para adicionar, atualizar e controlar as documentações relacionados ao gerenciamento do projeto e da equipe, como: quadro de disponibilidade, quadro de conhecimento, planilha de horas trabalhadas, atas de reunião, bem como disponibilização de materiais de estudo.

# Código
O desenvolvimento contínuo do código do projeto tem como objetivo implementar funcionalidades e recursos que constituem a interface e as regras de negócios da aplicação, atendendo à demanda do(s) cliente(s) formalizadas através dos requisitos da aplicação.

## Versionamento de controle
Foi utilizado as ferramentas Git e Github para realizar versionamento do código da aplicação bem como documentar as mudanças e evoluções no mesmo. Afim de manter um padrão e consistência nessa documentação, adotou-se alguns padrões e regras, detalhados a seguir:

### Padronização de Commits
+ Todos os commits devem estar em inglês e conter uma mensagem clara e objetiva.
+ Para commits pareados deve-se utilizar "Co-authored-by" na mensagem do commit incluindo as informações dos co autores.

### Padronização de Branchs
Foi adotada uma política de branchs baseada no [GitFlow](https://danielkummer.github.io/git-flow-cheatsheet/index.pt_BR.html).
+   **master**: Branch principal do projeto que contém versões estáveis e devidamente testadas do código.  
+   **develop**  - Branch de integração que reúne as últimas funcionalidades prontas e entregues que serve como base para o desenvolvimento de novas funcionalidades, correções de bugs e entrega de versão estável.
+   **feature_**  - Branchs que contém funcionalidades em desenvolvimento e são nomeadas de acordo com estas. Exemplo: `feature_login_with_github`.
+   **bugfix_**  - Branch que contém correções de bugs presentes na branch `develop`.
+   **hotfix_**  - Branch que contém correções de bugs presentes na branch `master`.


## Qualidade de código
Foram definidos alguns padrões padrões de desenvolvimento para garantir que o código  tivesse uma boa manutenibilidade,  legibilidade e coerência. Os padrões e ferramentas utilizadas para garantir seus cumprimentos estão listados abaixo:

+ [Flake8](http://flake8.pycqa.org/en/latest/index.html): biblioteca python utilizada através de script com configurações adaptadas ao projeto para capturar localmente erros que ferem as convenções de estilo adotadas pelo [PEP8](https://www.python.org/dev/peps/pep-0008/), os níveis de complexidade ciclomática estipulados e determinados erros de programação.
+ [Codeclimate](https://codeclimate.com): plataforma de revisão de código automatizada foi utilizada de forma adaptada ao projeto para detectar problemas que ferem a qualidade e manutenibilidade do código localmente e de forma integrada ao Github.
	+ Localmente: através da Interface de [Linha de comando do Codeclimate](https://github.com/codeclimate/codeclimate);
	+ Integrada ao Github: foit utilizado um webhook no Github para notificar eventos como pull request e commits ao Codeclimate, permitindo que este detectasse problemas relacionados à [duplicação de código](https://docs.codeclimate.com/docs/duplication), [complexidade ciclomática](https://docs.codeclimate.com/docs/radon), [complexidade cognitiva](https://docs.codeclimate.com/v1.0/docs/cognitive-complexity) e etc, e gerasse análises e revisões a respeito da manutenabilidade do código submetido. [Cardinals Codeclimate](https://codeclimate.com/github/fga-gpp-mds/2018.1-Cardinals);

# Build
Build contínuo visa garantir que o projeto possa ser facilmente construído, replicável, migrável e testável. Para tais fins foram utilizadass ferramentas de containerização e integração para construir os ambientes necessários ao projeto.

## Docker
o [Docker](https://www.docker.com) foi utilizado para criação e utilização de containers no desenvolvimento do código e testes, permitindo que o projeto pudesse ser construído, com todas suas dependências, rapidamente e facilitando a migração entre os ambientes de desenvolvimento, teste, homologação e produção.

# Teste

## Testes unitários
Foram utilizados testes unitários aplicados à métodos e classes para aferir a corretude do código, em sua menor fração. Os testes foram escritos pelos desenvolvedores seguindo orientações de documentações e comunidade [Python/Django](https://docs.djangoproject.com/en/2.0/topics/testing/).

## Cobertura de testes
Foram utilizadas algumas ferramentas para aferir e certificar o nível de cobertura de testes afim de avaliar se todas, ou a maioria, as partes da aplicação estavam sendo alcançadas.

+ [Coverage](https://coverage.readthedocs.io/en/coverage-4.5.1/): biblioteca Python utilizada localmente através de script e de forma integrada na ferramenta Travis para gerar relatório de cobertura de testes, detalhando para o desenvolvedor a porcetagem de código testada e fornecendo ao Codecov os dados necessários para gerar análises.
+ [Codecov](https://codecov.io/gh/fga-gpp-mds/2018.1-Cardinals): utilizado através de sua biblioteca Python e de sua plataforma para gerar análises de cobertura de testes disponibilizadas publicamente.


# Integração contínua
A Integração Contínua tem como objetivo mesclar pequenas alterações de código com frequência - em vez de mesclar em uma grande alteração no final de um ciclo de desenvolvimento. O objetivo é desenvolver softwares mais saudáveis, desenvolvendo e testando em incrementos menores.

## Travis

O Travis foi utilizado para dar suporte ao processo de desenvolvimento da aplicação criando builds e testes automatizados das alterações realizadas no código e fornecendo feedback imediato sobre o sucesso das alterações.
A ferramenta também foi utilizada para automatizar o processo de entrega contínua da aplicação.

# Deploy contínuo

## Travis e Heroku


# Monitoramento contínuo

O monitoramento contínuo tem como objetivos capturar, analisar e exibir dados e informações a respeito da execução de uma aplicação da web. As ferramentas de monitoramento fornecem transparência para que os desenvolvedores e as equipes de operações possam responder e corrigir problemas detectados durante a execução de uma aplicação a respeito de sua estabilidade, desempenho e erros.

### Librato
O Librato foi utilizado para monitorar e analisar as métricas que afetam o projeto. Através de integração com o Heroku é disponibilizado um link público do projeto ([Cardinals](https://metrics.librato.com/s/public/ce3wjrg32)) onde é disponibilizado um dashboard para visualização  das principais métricas, ifornecendo nformações detalhadas sobre o desempenho da aplicação, recursos do sistema e banco de dados.
