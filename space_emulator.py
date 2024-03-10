import json
from datetime import datetime

import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")
LOGIN = config["login"]
PASSWORD = config["password"]
DATABASE = config["database"]

with open('periods.json') as file:
    periods = json.load(file)

with psycopg2.connect(database=DATABASE, user=LOGIN, password=PASSWORD) as connection:
    with connection.cursor() as cur:
        cur.execute("""UPDATE mars_client_report SET send_date = %s WHERE id = %s""", (datetime.now(), 1))

        connection.commit()
