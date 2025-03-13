from sqlalchemy import create_engine, text

engine = create_engine(
    'sqlite://',
    echo=True
)

con = engine.connect()

sql = text('select id, name, comment from comments')

result = con.execute(sql)

con.close()


# OU:
with engine.connect() as con:
    sql = text('select id, name, comment from comments')
    result = con.execute(sql)
    