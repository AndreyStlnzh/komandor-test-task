import contextlib
import os

from playhouse.sqlite_ext import SqliteDatabase

from src.settings import DB_DIR, DB_FILENAME


with contextlib.suppress(FileExistsError):
    os.mkdir(DB_DIR)


db = SqliteDatabase(os.path.join(DB_DIR, DB_FILENAME))
