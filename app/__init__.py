"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch138l33cv203buj4n80-a.oregon-postgres.render.com",
        database="todo_soce",
        user="root",
        password="Lo0G33HZJnmYIpW1C5e0hdOeFATjBddR")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
