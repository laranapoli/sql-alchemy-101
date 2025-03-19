from sqlalchemy import create_engine, text

engine = create_engine('sqlite://')
query = 'select id from comments limit 10 offset {of}'


with engine.connect() as connection:
    with connection.begin():  # Define comandos que precisam acontecer juntos (na mesma conexão)
        sql = text(query.format(of=0))
        result1 = connection.execute(sql)
    with connection.begin():  # São vários blocos na mesma conexão
        sql = text(query.format(of=1))
        result2 = connection.execute(sql)
    with connection.begin():
        sql = text(query.format(of=2))
        resulr3 = connection.execute(sql)