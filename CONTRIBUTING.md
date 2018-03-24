# Contribuindo com Falko

Obrigado pelo interesse em colaborar com este projeto.

A seguir, algumas orientações:
- [Código de conduta](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/CODE_OF_CONDUCT.md)
- [Encontrou um bug?](#bug)
- [Sente falta de uma funcionalidade?](#funcionalidade)
- [Colaborar com novas funcionalidades](#colaborar)
- [Enviar Pull Request](#pullrequest)

## <a name="bug"></a> Encontrou um bug?
Reporte um bug abrindo uma issue. Utilize nosso [template de Issue](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/ISSUE_TEMPLATE.md).
Caso deseje corrigi-lo siga as [orientações para colaborar](#colaborar).

## <a name="funcionalidade"></a> Sente falta de uma funcionalidade?
Faça sugestões ou proponha soluções abrindo uma issue para esclarecer sua intenção. Utilize nosso [template de Issue](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/ISSUE_TEMPLATE.md).

## <a name="pullrequest"></a> Enviar Pull Request
1. Certifique-se de que a mudança proposta já não foi implementada.
2. Utilize nosso [template de Pull Request](https://github.com/fga-gpp-mds/2018.1-Grupo2/blob/master/PULL_REQUEST_TEMPLATE.md).

## <a name="#colaborar"></a> Colaborar com novas funcionalidades

1. Crie uma branch a partir da branch `develop`.
2. O nome desta branch deve começar com a palavra `feature_`, seguido do nome da feature, por exemplo: `feature_login_with_github`.
3. Ao finalizar seu trabalho, mande um pull request para a `develop` da upstream.

A partir daqui a equipe de desenvolvedores enviarão pull requests da branch `develop` para a branch `master` quando uma feature ou um conjunto de features estiverem completas e revisadas. 

## <a name="#colaborar"></a> Resolvendo bugs encontrados na master

1. Crie uma branch a partir da branch `master`.
2. O nome desta branch deve começar com a palavra `hotfix_`, seguido do nome do bug encontrado, por exemplo: `hotfix_login_crash`.
3. Ao finalizar seu trabalho, mande um pull request para a `master` da upstream.

## <a name="#colaborar"></a> Realizando releases

Quando a branch `develop` atingir um novo nível de maturidade de features, é hora de uma release. Nesta hora é necessário criar uma branch a partir da `develop`, onde esta branch mantém o projeto no estado de release, de forma que `develop` continue no seu fluxo de trabalho independentemente das branches de release.

1. Crie uma branch a partir da branch `develop`.
2. O nome desta branch deve começar com a palavra `release_`, seguido do nome/versão da release, por exemplo `release_v1.03`.
3. Ao finalizar seu trabalho, mande as modificações para o remoto. 

## <a name="#colaborar"></a> Documentação externa ao código

Branch exclusiva para arquivos dentro do diretório `docs/`.

1. Crie uma branch a partir da branch `docs`.
2. O nome desta branch deve começar com a palavra `docs_`, seguido do nome do documento ou trecho do documento a ser produzido, por exemplo: `docs_vision_stakeholders`.
3. Ao finalizar seu trabalho, mande um pull request para a `docs` da upstream.

A partir daqui a equipe de desenvolvedores enviarão pull requests da branch `docs` para a branch `master` quando documentos ou trechos de documentos forem finalizados e revisados.
