
# Challenge Boa Vista
[![Build Status](https://travis-ci.org/lserra/challenge_boa.svg?branch=source)](https://travis-ci.org/lserra/challenge_boa)

BOA VISTA Challenge for a Vacancy

#### Problema
O presente problema se refere aos dados de uma empresa que produz e vende máquinas industriais.

#### Objetivo
O objetivo deste desafio é:

(1) Fazer a modelagem conceitual dos dados,

(2) Criar a infraestrutura necessária e 

(3) Criar todos os artefatos necessários para carregar os arquivos para o banco criado.

#### Catálogo dos Dados

• price_quote.csv: esse arquivo contém informações sobre price quotes dos fornecedores. Os preços podem ser cotados de 2 formas:

1. Bracket pricing: possui múltiplos níveis de compra, baseado em quantidades (isso significa que o custo é dado assumindo-se a compra de certa quantidade de tubos)

2. Non-bracket pricing: possui uma quantidade mínima a ser pedida (min_order) para que o preço seja aplicado. Cada uma dessas cotações é emitida com uma annual_usage, que se refere a estimativa de quantos conjuntos de tubos serão comprados em determinado ano.

• Bill_of_materials.csv: esse arquivo contém a lista de componentes e as quantidades que foram utilizadas em cada conjunto de tubos.

• comp_boss.csv: esse arquivo contém as informações sobre cada componente.

# O Plano

1- Conhecendo os dados

2- Brincando com as entidades e seus relacionamentos 

3- Pensando na arquitetura e seus desafios

4- Pensando na ingestão de dados (code blocks)

5- Construindo os code blocks

6- Montando o lego (encaixando as peças)

7- Deployment

## Conhecendo os Dados (EDA-Exploratory Data Analysis)

Análise exploratória dos dados usando o `Python/Pandas`.

O script usado para gerar os relatórios, pode ser encontrado na pasta: `/scripts/eda.py`.

Para gerar os relatórios, basta executar os comandos abaixo:

```shell script
$ cd challenge_boa
$ bash eda.sh
```

E os relatórios em formato HTML, podem ser encontrados na pasta: `/challenge_boa/analysis`.

## Modelagem dos Dados

O modelo de dados pode ser encontrado na pasta: `/doc`. [deprecated]

Esta informação está disponível no arquivo compartilhado [aqui](https://docs.google.com/presentation/d/1JjqCWYafxAh5RF5fwVPnWJyFFPNnlFRz-FXJQErQLjQ/edit?usp=sharing)

Na pasta `./challenge_boa/data` estão disponíveis todos os arquivos CSV (source/target).

Na pasta `/db` está disponível o banco de dados SQLite com as tabelas criadas a partir dos arquivos CSV (target).

## Sugestão de Arquitetura

Esta informação está disponível no arquivo compartilhado [aqui](https://docs.google.com/presentation/d/1JjqCWYafxAh5RF5fwVPnWJyFFPNnlFRz-FXJQErQLjQ/edit?usp=sharing)

#### PLANO A (Deprecated)

Em função de alguns problemas técnicos não previstos a ideia era apresentar a solução abaixo: 

- **Raw Data**: carregar os dados em seu estado bruto, para uma camada lógica de dados, chamada stage area.

- **Big Tables**: fazer algumas transformações nos dados e depois mover para esta camada lógica.

- **DW**: fazer o enriquecimento nos dados e depois mover para esta comada lógica. (*Business Intelligence Self-Service*).

Para esta solução seria usado o banco de dados: SQLite.

#### PLANO B

Depois da entrevista técnica realizada, percebi que era muito importante fazer uma mudança de rumo e adaptar a minha solução para os serviços do Google Cloud.
Então, a solução aqui apresentada faz uso dos seguintes serviços: 

- Google Cloud Storage (GCS)
- Google Cloud Functions (GCF)
- Google Cloud BigQery (GBQ)
- Google Colud Data Studio (GDS) 

## Fluxo dos Dados

Esta informação está disponível no arquivo compartilhado [aqui](https://docs.google.com/presentation/d/1JjqCWYafxAh5RF5fwVPnWJyFFPNnlFRz-FXJQErQLjQ/edit?usp=sharing)

## Como Executar e Monitorar o Processo

- Para executar a aplicação é necessário ter instalado na máquina o Python (3.7.7) ou mais recente. Execute o comando abaixo para verificar a versão do python instalado na sua máquina:

```shell script
$ python --version
```

Além disso, será necessário instalar as seguintes bibliotecas: pandas, sqlalchemy, google-cloud-storage, google-cloud-bigquery. Para instalar todas estas bibliotecas, basta executar os comandos abaixo:  

```shell script
$ cd challenge_boa
$ pip install -r requirements.txt
```

- CLI command: para executar a aplicação, basta executar os comandos abaixo.

```shell script
$ cd challenge_boa
$ bash start.sh
```

- Docker: para executar a aplicação usando o Docker, é necessário que você tenha o Docker instalado na sua máquina. Para verificar se você possui o Docker instalado, basta 
digitar o seguinte comando:

```shell script
$ docker --version
```

Em seguida, você deve executar o comando abaixo no mesmo diretório em que se encontra o Dockerfile.

```shell script
$ cd challenge_boa
$ docker build -t lserra/de_boa:latest . 
```

## Relatórios e Dashboard

**Relatórios EDA**:

- [Bill of Material](/challenge_boa/analysis/bill_of_materials.html)
- [Comp Boss](/challenge_boa/analysis/comp_boss.html)
- [Price Quote](/challenge_boa/analysis/price_quote.html)


**Executive Dashboard**: é possível visualizar o dashboard criado no Google Data Studio, através deste [link](https://datastudio.google.com/s/rzKQurvL8c0)

## Estutura de Pastas e Arquivos do Projeto

    challenge_boa
        |__ /analysis       => resultado da análise exploratória dos dados e relatório gerencial da empresa
        |__ /data           => arquivos CSV (source/target)
        |__ /db             => banco de dados SQLite 
        |__ /doc            => definição do escopo do projeto
        |__ /scripts        => processos de ingestão dos dados
        |__ README.md       => documentação do projeto
        |__ start.sh        => script de execução do projeto

## Agradecimentos

Agradeço a oportunidade de poder participar deste processo.

Segue abaixo outras referências do meu trabalho e coloco-me a disposição de todos para os esclarecimentos que forem necessários.

GitHub:

- [My Personal Blog](https://lserra.github.io/)
- [B2W](https://github.com/lserra/challenge_b2w)
- [ContaAzul](https://github.com/lserra/challenge_ca)
- [AWS EMR](https://github.com/lserra/BrodAI)
- [Diversos](https://github.com/lserra/blog_da/tree/master/notebooks)

THANK YOU !!! 🍺🍺
