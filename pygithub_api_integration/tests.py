from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class RepoInfoTests(TestCase):


    def test_get_repo_name(self):

        organization = 'fga-gpp-mds'
        repo_name = '2018.1-Cardinals'
        repo_path = organization + '/' + repo_name

        url = reverse('getRepoInfo')
        content = {'repository': repo_path}

        #A váriavel response retorna a reposta da requisição que o client faz a url('getRepoInfo'), a variável repository
        #é um objeto do tipo repositório, a váriavel repo_path é uma basicamente a url do repositório que você quer pesquisar.
        #e a váriavel context é um dicionario do tipo repositório que vai ser preenchido por váriaveis repo_path que são do tipo path.
        
        response =  self.client.post(url, content)

        #esta variável vai pegar a variável response(que é a resposta do tipo https que damos ao usuário), pegar o seu contexto que é um dicionário 
        #de variáveis do tipo repo (repositório = repo) e depois chamar o método name para ver o nome da váriavel/objeto repo.
        
        response_repo_name = response.context['repo'].name
        
        #esse método usa o self para falar que o método é desta classe, e chama oo assertEquals que verifica que as váriaveis passadas
        #na assinatura são iguais (repo_name = response_repo_name)
        
        self.assertEquals(repo_name, response_repo_name)


    def test_get_contributors_name(self):
        organization = 'fga-gpp-mds'
        repo_name = '2018.1-Cardinals'
        repo_path = organization + '/' + repo_name

        url = reverse('getRepoInfo')
        content = {'repository': repo_path}
        response = self.client.post(url, content)

        contributors = response.context['contributors']

        contributors_name_expected = ['Amanda Bezerra', 'Mateus Augusto Sousa e Silva', 'Marlon Mendes', 'Guilherme da Luz',
                                      'Lucas Costa', 'Gustavo Duarte Moreira', 'Matheus Gomes', 'Lorrany Azevedo',
                                      'João Pedro', 'Mik', 'Victor Moura' ]

        contributors_name_expected = set(contributors_name_expected)

        contributors_name = set([contributor.name for contributor in contributors])

        self.assertEquals(contributors_name, contributors_name_expected)


    def test_get_contributors_login(self):

        organization = 'fga-gpp-mds'
        repo_name = '2018.1-Cardinals'
        repo_path = organization + '/' + repo_name

        url = reverse('getRepoInfo')
        content = {'repository': repo_path}
        response =  self.client.post(url, content)

        contributors =  response.context['contributors']

        contributors_login_expected = ['amandabezerra', 'Mateusas3s', 'marlonbymendes', 'daluzguilherme',
                                       'gustavoduartemoreira', 'matheusgomesf', 'jpmartins201', 'lorryaze',
                                       'lucasca73', 'victorcmoura', 'MiguelNery']

        contributors_login_expected = set(contributors_login_expected)

        contributors_login = set([contributor.login for contributor in contributors])

        self.assertEquals(contributors_login, contributors_login_expected)


