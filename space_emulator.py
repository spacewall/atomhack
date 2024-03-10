import json
from datetime import datetime, timedelta

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
        last_time = datetime.now()

        while True:
            cur.execute("""SELECT * FROM mars_client_report WHERE send_date IS NULL""")
            field = cur.fetchall()[-1]

            # UTF-8 encoding
            size = len(''.join([str(el) for el in field])) / 8

            for period in periods:
                now = datetime.now()
                speed = period['speed']
                file_time = size / speed
                time_from = datetime.strptime(period['from'], "%Y-%m-%d %H:%M:%S")
                time_to = datetime.strptime(period['to'], "%Y-%m-%d %H:%M:%S")
                
                if now >= time_from and now <= time_to:
                    if timedelta(seconds=file_time) < time_to - last_time:
                        last_time = now + file_time
                        
                        if last_time > time_to:
                            last_time = time_to

                        else:
                            cur.execute("""UPDATE mars_client_report SET send_date = %s WHERE id = %s""", (last_time, field[0]))

                            connection.commit()
                            