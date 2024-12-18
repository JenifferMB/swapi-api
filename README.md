# SWAPI-API
## Sobre o projeto:
Ingestão de dados da [Swapi API](https://swapi.py4e.com).

1- Realização da ingestão das 5 primeiras páginas referente aos endpoints de "people", "planets" e "films". 
2- Padronização das strings para lower case e remoção dos caracteres especiais.
3- Organização dos repositórios> Raw - Arquivos referente as páginas, no formato csv, identificados em cada página; Work - Arquivos após o processamento, no formato csv.

## Dependências
Esse projeto utilza Poetry para a gestão de dependências e a execução do mesmo.

### Poetry
Antes de começar, é necessário ter `pipx` instalado. Se não tiver, siga as instruções clicando [aqui](https://github.com/pypa/pipx).

Após isso, instale o poetry com o seguinte comando:
```pipx install poetry```

## Como rodar:
Instalar as dependências:
```poetry install```

Ativar Virtual Environment:
```Poetry shell```

Rodar a aplicação com o comando: 
```Python swapi-etl.py```