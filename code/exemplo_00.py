from sqlalchemy import create_engine

engine = create_engine(  # Padrão de projeto chamado Factory (fábrica de motores)
    'sqlite://',  # URI do BD - Isso cria um banco SQLite em memória
    echo=True,
)

print(engine)

engine_pg = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)

# print(engine_pg.dialect)
# print(engine_pg)

print(engine.pool, engine.pool.status())

con = engine.connect()

print(con.connection.dbapi_connection)

con.close()