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

49:36