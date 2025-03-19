# [SQLAlchemy: conceitos básicos, uma introdução a versão 2](https://www.youtube.com/watch?v=t4C1c62Z4Ag)

- Kit de ferramentas para trabalhar com bancos de dados SQL
- Toolkit suporta:
    - Async e Sync
    - Anotações de tipos e forma dinâmica
    - Implementa a DBAPI
    - Suporta cPython e PyPy
    - ORM
    - Sistemas de plugins
    - Eventos
- ORM: Object Relational Mapper (ORM)
    - Relacionar objetos python com bancos relacionais

- CORE:
    - Componente mais básico do SQLAlchemy
    - Responsável por criar conexão com o banco de dados, fazer buscas e definir tipos.
    - Componentes importantes:
        - Engine - fábrica de conexões com o banco de dados
            - Connection: Interface para se comunicar com o banco
            - Dialect: Mecanismos específicos para cada banco de dados
                - Dialetos são chamadas diretas para os drivers específicos para databases específicos.
            - Pool: Deixa conexões em memória para ser mais fácil reutilizar
                - A instrução de abertura de conexão é geralmente cara
        - SQL Expression Language: Construções em Python para representar SQL
        - Schemas/Types: Construções em python que representam tabelas, colunas e tipos de dados.

## Result
- O resultado obtido no execute é um objeto especial chamado Result.
- Ele implementa diversos métodos, além de ser um iterável.
- Alguns métodos:
    - .fetchone(): pega o primeiro
    - .fetchmany(3) / .patitions(3): pega alguns valores
    - .fetchall() / .all(): pega todos os valores
    - .first(): pega 1, mas não dá erro se não conseguir
    
## Schemas / Types
- Os metadados das tabelas podem ser descritos por Schemas e seus determinados Tipos

## Reflection
- Olha para o branco e traz relações
- Funções de inspeção são agregadas a construção de schemas
- Evitam a criação de metadados em um banco que já existe

## SQL Expression Language
- Queremos os metadados para usar no motor de busca: SQL Expression Language (query builder)
- É uma alternativa a função text() - em que escrevemos SQL na mão (string)
- O Core tem um grupo de funções e objetos que ajudam a montar o SQL:
    - DQL: Data Query Language
    - DML: Data Manipulation Language

## CompoundSelect
- O resultado do select é um builder
- Podemos encadear comandos e fazer busca mais complexa

## Conectivos lógicos

1:35:45