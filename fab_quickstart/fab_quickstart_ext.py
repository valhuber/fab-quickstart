import sqlalchemy
import sqlalchemy.ext
from sqlalchemy import MetaData

import fab_quickstart

import logging
from typing import NewType
# not required: from app.models import *
import sys

TableModelInstance = NewType('TableModelInstance', object)


class FabQuickStartExt(fab_quickstart.FabQuickStart):
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
            You might want to override this, depending on
                your language (e.g., "nom", not "name"), or 
                db naming conventions.
        """
        return ["name", "description"]

log = logging.getLogger(__name__)
log.debug("fab_quickstart (overrides here)")

log = logging.getLogger(__name__)
log.debug("\n\nRunning: " + sys.argv[0] + "\n\n" + sys.version + "\n\n")


metadata = fab_quickstart.find_meta_data()

fab_views_gen = FabQuickStartExt()
generated_view = fab_views_gen.generate_view(metadata)

log.debug("\n\nCompleted, generated views.py-->\n\n\n\n")
print(generated_view)
