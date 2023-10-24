import requests
import psycopg2
import json

class StarWarsAPI:
    def __init__(self):
        self._base_urls = {
            "films": "https://swapi.dev/api/films/",
            "people": "https://swapi.dev/api/people/",
            "planets": "https://swapi.dev/api/planets/",
            "species": "https://swapi.dev/api/species/",
            "starships": "https://swapi.dev/api/starships/",
            "vehicles": "https://swapi.dev/api/vehicles/"
        }

    def fetch_data(self, endpoint):
        response = requests.get(self._base_urls[endpoint])
        if response.status_code == 200:
            return response.json()['results']
        else:
            print(f"Request Error. Response Code : {response.status_code}")
            return None

class DatabaseDriver:
    def __init__(self, db_name):
        self._conn = psycopg2.connect(dbname=db_name, user='your_username', host='localhost')
        self._cur = self._conn.cursor()

    def execute_query(self, query):
        self._cur.execute(query)
        self._conn.commit()

    def setup(self):
        self.execute_query(create_starwars_schema)
        self.execute_query(create_planets_table)

    def close(self):
        self._cur.close()
        self._conn.close()

# Define your schema and table creation queries
create_starwars_schema = """CREATE SCHEMA IF NOT EXISTS starwars;"""

create_planets_table = """
CREATE TABLE IF NOT EXISTS starwars.planets (
    id SERIAL PRIMARY KEY,
    name TEXT,
    diameter TEXT,
    -- ... other columns
    url TEXT,
    created TEXT,
    edited TEXT
);
"""

def create_database(db_name):
    conn = psycopg2.connect(dbname='postgres', host='localhost')
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
    cur.close()
    conn.close()

def extract_id(url):
    return int(url.strip('/').split('/')[-1])

def main():
    db_name = 'starwars_db'
    create_database(db_name)  # Create the database
    
    api = StarWarsAPI()
    planets_data = api.fetch_data('planets')
    
    db = DatabaseDriver(db_name)  # Now pass the db_name to DatabaseDriver
    db.setup()
    
    for planet in planets_data:
        planet_id = extract_id(planet['url'])
        insert_query = f"""
        INSERT INTO starwars.planets (id, name, diameter, url, created, edited)
        VALUES ({planet_id}, '{planet['name']}', '{planet['diameter']}', '{planet['url']}', '{planet['created']}', '{planet['edited']}')
        ON CONFLICT (id) DO NOTHING;
        """
        db.execute_query(insert_query)
    
    db.close()  # Close the database connection

if __name__ == "__main__":
    main()
