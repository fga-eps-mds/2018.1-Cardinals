from github import Github
from datetime import datetime


g = Github("mdscardinals", "(cardinals1)")

org = g.get_organization('fga-gpp-mds')
repo = org.get_repo('2018.1-Cardinals')

datacriacao = datetime(2018,4,1)
datafechamento = datetime(2018,4,4)
lista = []

estado="closed"


stes = repo.get_stats_contributors()


for i in stes:
        lista = i.author, i.total
        print(lista)