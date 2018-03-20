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

1. Create a new branch from `develop`. That new branch's name must start with `feature_`
   
    `$ git checkout develop`
    
    `$ git checkout -b feature_name`

2. Always write (in english) a clear log messages for your commits. One line comments are prefered.
  
     `$ git commit -m "An english comment with a clear messaget about thtis commit`
     
3. Open a pull request using the Github web page
 
3. Or if you are a repo member, you can merge `feature_` into `develop`.
     
     1. Merge with develop
       
        `$ git checkout develop`
     
        `$ git merge feature_name`
    
     2. Solve the conflits (if any).
     
     3. Delete the feature branch:
     
        `$ git branch -d feature_name`
     
     4. Push changes
