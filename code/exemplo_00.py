from sqlalchemy import create_engine

engine = create_engine(  # Padrão de projeto chamado Factory (fábrica de motores)
    'sqlite://'  # URI do BD - Isso cria um banco SQLite em memória
)

print(engine)

engine_pg = create_engine(
    'postgresql+psycopg://app_user:app_password@localhost:5432/app_db'
)

print(engine_pg.dialect)
print(engine_pg)