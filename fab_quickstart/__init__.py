"""
import logging

this is part of the (failing) experiment to make run.py executable

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

""
 Logging configuration
""
print ("__init__ for build_views")
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
# app.config.from_object("../config")
db = SQLA(app)
# should not need this, right??  appbuilder = AppBuilder(app, db.session)



from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


from . import views
"""
