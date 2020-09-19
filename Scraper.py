from Sources.AoE import AoE
from Client import Client
import mysql.connector

class Scraper:

    client = Client

    def __init__(self, client):
        self.client = client

    def get(self, url):
        return self.client.get(url)


scraper = Scraper(Client())
full_url = "https://ageofempires.fandom.com/wiki/Siege_weapons_(Age_of_Empires_II)"
response = scraper.get(full_url)

siege_units = AoE.format(response.content)
siege_units = filter(None, siege_units)

# Connect to server
mysql = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "scraper"
)

# Get a cursor
cursor = mysql.cursor()


for siege_unit in siege_units:
    sql = "INSERT INTO siege_weapons (name, hp) VALUES (%s, %s)"
    val = (siege_unit.name, siege_unit.hp)
    cursor.execute(sql, val)

    mysql.commit()