from datetime import datetime

import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")
LOGIN = config["login"]
PASSWORD = config["password"]
DATABASE = config["database"]
with psycopg2.connect(database=DATABASE, user=LOGIN, password=PASSWORD) as connection:
    with connection.cursor() as cur:
        cur.execute("""UPDATE mars_client_report SET send_date = %s WHERE send_date = %s""", (datetime.now(), None))
