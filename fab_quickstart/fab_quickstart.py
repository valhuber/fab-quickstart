import sqlalchemy
import sqlalchemy.ext
from sqlalchemy import MetaData

import fab_quickstart_base

import logging
from typing import NewType
# not required: from app.models import *
import sys

TableModelInstance = NewType('TableModelInstance', object)


class FabViewsGen(fab_quickstart_base.FabQuickStartBase):
    """
        @see fab_code_gen_base

        This extends it, to execute, and provide overrides as required
    """

    def model_name(self, table_name: str):  # override
        """
            You might want to override this
            depending on your table name.
        """
        return "ModelView"

    def favorite_column(self, a_table_def: TableModelInstance):
        """
            You might want to override this
            depending on your table name.
        """
        result = super().favorite_column(a_table_def)
        return result

    def favorite_name(self):
        """
            You might want to override this
            depending on your language, or db naming conventions.
        """
        return ["name", "description"]

log = logging.getLogger(__name__)
log.debug("fab_quickstart (overrides here)")

log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")

conn_string = "sqlite:///nw/nw.db"  #  TODO - use config file, per cmd line args

"""     FIXME - getting foreign_keys is still a mystery

    Why is this important
        Many DBs don't define FKs into the db
        Instead, they define "Virtual Keys" in their model files
    foreign_keys visible, using sqlite:///nw/nw.db
        I added fKeys to the db
    foreign_keys NOT visible, using sqlite:///nw/nw-no-fkeys.db
        Even explicitly loading model (see 3 lines below), metadata has no foreign_keys
        But *something* works for FAB... what is it??
    References
        https://stackoverflow.com/questions/62585890/how-does-flask-sqlalchemy-know-which-models-classes-youve-defined


import models  //  trying to get sqla to see fkeys
order = models.Order()
order.ShipCity = "Mountain View"

"""

engine = sqlalchemy.create_engine(conn_string)

connection = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine, resolve_fks=True)

fab_views_gen = FabViewsGen()
generated_view = fab_views_gen.generate_view(metadata)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)
