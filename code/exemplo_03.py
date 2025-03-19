from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine # para async

engine = create_async_engine(
    'sqlite://',
    echo=True
)

con = engine.connect()

sql = text('select id, name, comment from comments')

result = con.execute(sql)

con.close()


# OU:
async with engine.connect() as con:
    sql = text('select id, name, comment from comments')
    result = await con.execute(sql)
    

# Retorna todos os dados:
result.fetchall()