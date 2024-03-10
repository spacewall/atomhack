import sqlalchemy
from sqlalchemy.schema import Table, MetaData
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import dotenv_values

config = dotenv_values(".env")
LOGIN = config["login"]
PASSWORD = config["password"]
DATABASE = config["database"]
data_source_name = f'postgresql://{LOGIN}:%s@localhost:5432/{DATABASE}' % quote_plus(PASSWORD)
engine = sqlalchemy.create_engine(data_source_name)

Base = declarative_base()

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

create_tables(engine)
Session = sessionmaker(engine)
session = Session()

metadata_obj = MetaData()
messages = Table('mars_client_report', metadata_obj, autoload_with=engine)
print([c.name for c in messages.columns])
