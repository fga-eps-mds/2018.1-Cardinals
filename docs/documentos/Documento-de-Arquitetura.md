## Histórico de Revisões

| Data | Versão | Descrição | Autor |
--------- | ------ | ------- | -------
| 22/03 | 1.0 | Introdução | Gustavo Duarte Moreira |
| 22/03 | 1.1 | Finalidade | Gustavo Duarte Moreira |
| 22/03 | 1.2 | Escopo | Gustavo Duarte Moreira |
| 22/03 | 1.3 | Visão Geral | Gustavo Duarte Moreira |
| 22/03 | 2.0 | Representação da Arquitetura | Mateus Augusto |
| 22/03 | 3.0 | Metas e Restrições da Arquitetura | Mateus Augusto |
| 22/03 | 3.1 | Ambiente e Ferramentas de Desenvolvimento | Mateus Augusto |
| 22/03 | 5.0 | Visão de Processos | Mateus Augusto |
| 24/03 | 6.0 | Visão de Implantação | Lorrany Azevedo, João Martins |
| 22/03 | 7.0 | Visão de Implementação | Mateus Augusto |
| 22/03 | 7.1 | Visão Geral | Mateus Augusto |
| 22/03 | 7.2 | Camadas | Mateus Augusto |
| 27/03 | 8.0 | Tamanho e Desempenho | Matheus Gomes |
| 27/03 | 9.0 | Qualidade | Matheus Gomes |
| 27/03 | 10.0 | Refêrencias | ------- |
## Sumário

1. [Introdução](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#1-introdu%C3%A7%C3%A3o)       
  1.1 [Finalidade]()            
  1.2 [Escopo]()   
  1.3 [Visão Geral]()

2. [Representação da Arquitetura](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#2-representa%C3%A7%C3%A3o-da-arquitetura)

3. [Metas e Restrições de Arquitetura](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#3-metas-e-restri%C3%A7%C3%B5es-da-arquitetura)        
  3.1 [Ambiente e Ferramentas de Desenvolvimento](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#31-ambiente-e-ferramentas-de-desenvolvimento)

4. [Visão Lógica](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#4-vis%C3%A3o-l%C3%B3gica)              
  4.1 [Visão Geral](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#41-vis%C3%A3o-geral)                 
  4.2 [Pacotes de Design Significativos do Ponto de Vista da Arquitetura](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#42-pacotes-de-design-significativos-do-ponto-de-vista-da-arquitetura)

5. [Visão de Processos](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#5-vis%C3%A3o-de-processos)

6. [Visão de Implantação](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#6-vis%C3%A3o-de-implanta%C3%A7%C3%A3o)

7. [Visão de Implementação](https://github.com/fga-gpp-mds/2018.1-Cardinals/wiki/Documento-de-Arquitetura#7-vis%C3%A3o-da-implementa%C3%A7%C3%A3o)         
  7.1 [Visão Geral]()           
  7.2 [Camadas]()              
    * [Model]()           
    * [View]()             
    * [Template]()             

8. [Tamanho e Desempenho]()                            

9. [Qualidade]()                    

10. [Referências]()                   


# 1. Introdução
## 1.1 Finalidade.  
<p align ="justify"></p>O objeto deste documento é fornecer uma visão geral da arquitetura que abrange o sistema Cardinals. Ele deve mostrar de forma clara e objetiva as decisões arquiteturais que foram tomadas em relação ao projeto. Para fornecer as informações necessárias desenvolvedores e demais envolvidos em termos de estrutura da aplicação e tecnologias utilizadas. 

## 1.2 Escopo     
<p align="justify"></p>O Documento de Arquiteturaa de Software se aplica ao sitema Cardinals. A plataforma tem o objetivo de facilitar a atividade de acompanhamento gerencial de projetos desenvolvidos com metodoligia Ágil.


## 1.3 Visão Geral
<p align="justify"></p>O projeto Cardinals tem como objetovo mostrar informações gerenciais referentes ao desenvolvineto de softwares que utilizam a metodologia Ágil. Ele irá oferecer a visualização de indicadores de desempenho, gerar relatórios de qualidade entre outros, mostrar um checklist das principais práticas adotadas no desenvolvimento como: utilização de Docker, realização de testes e sua porcentagem, se possui integração continua, entre outros.

# 2. Representação da Arquitetura
<p align="justify">Nosso projeto utilizará a arquitetura MTV (model, template, view), que trata-se de um padrão de arquitetura de software baseada na MVC mas adaptada pela framework Django. Ela separa a aplicação em 3 camadas tal como a tradicional MVC. A camada Model que manipula dos dados, a Template, onde há a interação com o usuário e a View, onde ficam as ações e trata as requisições do usuário</p>
<img src="https://raw.githubusercontent.com/wiki/fga-gpp-mds/2018.1-Cardinals/imagens/esquema-mtv.jpeg" alt="MTV">
<p>Figura 1</p>
<p>Fonte: https://pt.slideshare.net/CursosDevcode/fundamentos-dj-45913014</p>



# 3. Metas e Restrições da Arquitetura
## 3.1 Ambiente e Ferramentas de Desenvolvimento
<p align="justify">O sistema será desenvolvido para funcionar em todos os navegadores web e terá comportamento responsivo, portanto adaptando-se adequadamente a navegadores desktop e mobile.
Utilizaremos o modelo MTV como padrão arquitetural de nosso sistema e
todos os recursos do sistema deverão estar disponíveis em Português(Brasil). 
A aplicação será acessada por conexão de internet de qualquer computador ou mobile com acesso a mesma.
As ferramentas de desenvolvimento serão:</p>

+ Linguagem Python em sua última versão oficial 3.6.2;
+ Framework Django em sua última versão oficial 1.11.4.

# 4. Visão Lógica
## 4.1 Visão Geral
<p align="justify"> Design Responsivo é uma técnica de estruturação HTML e CSS, em que o site se adapta ao browser do usuário sem precisar definir diversas folhas de estilos para cada resolução.
Na arquitetura MTV, os dados serão lidos, escritos e validados na camada Model. Tudo que diz respeito aos dados serão tratados aqui. Por exemplo a validação dos dados de login do usuário será feita na Model. A camada Template, é a camada responsável por “comunicar-se com o usuário”. É onde as funcionalidades são mostradas na tela, usualmente é feita em XML ou HTML. E o por fim, a View que é responsável por receber todas as requisições do usuário. Seus métodos chamados actions são responsáveis por uma página, controlando qual model usar e qual template será mostrado ao usuário.</p>

<img src="https://raw.githubusercontent.com/wiki/fga-gpp-mds/2018.1-Cardinals/imagens/esquema-django.jpeg" alt="Django framework">
<p>Figura 2 </p>
<p>Fonte: https://pt.slideshare.net/AnushaChickermane/saasy-maps </p>



## 4.2 Pacotes de Design Significativos do Ponto de Vista da Arquitetura

  * Diagrama de Classes

# 5. Visão de Processos
<p align="justify">O software será implementado de forma que o mesmo possa ser utilizado simultaneamente, utilizando para isso o paralelismo (threads), em que a cada nova solicitação de conexão à base de dados, um novo processo (“processo filho”) é criado, fazendo com que o tempo de cpu do hardware sobre o qual roda o software seja compartilhado com todos os novos processos. Ao fim de cada processo “filho”, o mesmo é finalizado, devolvendo à cpu a porção de tempo (tempo de cpu) utilizada, que fica disponível para ser utilizado por um novo processo.</p>

# 6. Visão de Implantação
<p align="justify"></p>

# 7. Visão da Implementação.         

O sistema é construído na linguagem python utilizando o framework Django, com foco para web. A linguagem python ultiliza o seu interpretador para executar o sistema nas mais diversas plataformas, esse interpretador lê os arquivos de extesão ".py", executa o código e assim o converte para linguagem de máquina. O sistema funcionará da seguinte forma o usuário irá fazer uma requisição para o servidor, essa requisição irá se comunicar com um arquivo .py e esse arquivo irá através da API solicitar acesso os dados do GitHub.
 
## 7.1 Visão Geral.       
<p align="justify">Será desenvolvido um sistema baseado em camadas MTV (model, template e view), modelo esse utilizado pelo framework Django. A separação em camadas permite tornar independente, uma das outras, a lógica utilizada em cada camada, permitindo assim a modificação dessas camadas sem alterar o funcionamento das outras. Além disso,como pode se observar na imagem abaixo (figura 2), o sistema baseado em camadas permite uma melhor visualização da forma como as informações são tratadas no sistema, sendo cada camada responsável por uma determinada tarefa dentro do software.</p>

## 7.2 Camadas

###  Model

<p align="justify">É nessa camada que se implementa as classes que serão responsáveis por definir as informações que estarão presentes na tabela de dados (banco de dados) e como esses dados serão acessados , validados , relacionados e etc. Isto é, a model é responsável por conter todas as informações referentes à manipulação de dados.</p>

###  View

<p align="justify">A responsabilidade da camada de view é encapsular a lógica responsável para processar o pedido do usuário e retornar uma resposta. Esta resposta pode ser uma página web, uma imagem, uma página de erro, o que o desenvolvedor da view especificar</p>

###  Template

<p align="justify">Template é a camada mais externa e visual do software, é basicamente a interface aparente ao usuário, é nessa camada que se define como os dados das camadas inferiores serão apresentados.</p>

# 8. Tamanho e Desempenho
<p align="justify"></p>
<p align="justify"></p>

# 9. Qualidade

<p align="justify"></p>

# 10. Referências

+ FUNPAR.UFPR.com. Artefato: Documento de Arquitetura de Software. Disponível em: http://www.funpar.ufpr.br:8080/rup/process/artifact/ar_sadoc.htm. Acesso em 22 de Março de 2018.

+ GITHUB.com. Padrões Arquiteturais MVC x Arquitetura do Django. Disponível em:https://github.com/fga-gpp-mds/00-Disciplina/wiki/Padrões-Arquiteturais---MVC-X-Arquitetura-do-Django. Acesso em 22 de Março de 2018.
+ DOCS.DJANGOPROJECT.com. FAQ: General. Disponível em: https://docs.djangoproject.com/en/1.10/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names. Acesso em 22 de Março de 2018.
+ DEPLOYMENT DIAGRAMS. Disponível em: https://www.ibm.com/support/knowledgecenter/SS5JSH_9.5.0/com.ibm.xtools.modeler.doc/topics/cdepd.html. Acesso em 22 de Março de 2018.

+ TUTORIALSPOINT.com. Django Overview. Disponível em: https://www.tutorialspoint.com/django/django_overview.htm. Acesso em 22 de Março de 2018.
