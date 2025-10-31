import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = os.path.join(BASE_DIR, "db")
DB_FILENAME = "sales_db.db"
