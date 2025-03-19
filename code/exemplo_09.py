import sqlalchemy as sa

metadata = sa.MetaData()
engine = sa.create_engine('sqlite:///database.db')

# metadata.create_all(engine)

inspect = sa.inspect(engine)
# print(inspect.get_table_names())
# print(inspect.get_columns(table_name='comments'))

t = sa.Table('comments', metadata, autoload_with=engine)

print(t)
print(t.columns)
print(t.c.id)