import psycopg2
from psycopg2 import sql
import logging

LOG_FILENAME = 'debug.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
logger = logging.getLogger(__name__)

dbname = "tribalwars"
user = "user"
password = "4202"
host = "localhost"
port = "5432"

# Your data
data = {
    '47199': {
        'village_id': '47199',
        'name': 'Aldeia de rpcg980',
        'x': '469',
        'y': '696',
        'continent': '64',
        'player_id': '265454',
        'points': '26',
        'server': 'en43'
    }
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()


def postgres_village_data(data, cur):
    # Create the table
    table_name = "village_data"
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            village_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            x VARCHAR(255),
            y VARCHAR(255),
            continent VARCHAR(255),
            player_id VARCHAR(255),
            points VARCHAR(255),
            server VARCHAR(255)
        )
    """).format(sql.Identifier(table_name))

    cur.execute(create_table_query)

    # Insert data into the table
    for village_id, village_data in data.items():
        insert_query = sql.SQL("""
            INSERT INTO {} (village_id, name, x, y, continent, player_id, points, server)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """).format(sql.Identifier(table_name))

        try:
            cur.execute(insert_query, (
                village_data['village_id'],
                village_data['name'],
                village_data['x'],
                village_data['y'],
                village_data['continent'],
                village_data['player_id'],
                village_data['points'],
                village_data['server']
            ))

        except psycopg2.errors.UniqueViolation:
            logger.info(f"Unique id violation -> {village_id}")

# Commit and close the connection
conn.commit()
conn.close()