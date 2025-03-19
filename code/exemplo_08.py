import sqlalchemy as sa

metadata = sa.MetaData()

t = sa.Table('comments', metadata,
             sa.Column('id', sa.Integer(), nullable=False),
             sa.Column('name', sa.String(), nullable=False),
             sa.PrimaryKeyConstraint('id')
)

engine = sa.create_engine('sqlite:///database.db')

metadata.create_all(engine)


sql = sa.select(t)

print(sql)

with engine.connect() as con:
    result = con.execute(sql)
    print(result.fetchmany(10))

stmt = (
    sa.select(t.c.id)
    .where(t.c.name == 'Lara')
    .limit(3)
    .order_by(t.c.id)
)

print(stmt)