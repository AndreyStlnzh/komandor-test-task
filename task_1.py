import os
import pandas as pd

from src.db.sales_model import SalesModel
from src.settings import DATA_DIR

try:
    cashier = pd.read_excel(os.path.join(DATA_DIR, "Продажи по кассам.xlsx"), index_col="cash_id")
except FileNotFoundError:
    print("Файл 'Продажи по кассам.xlsx' не найден")
    exit(1)
try:
    reference = pd.read_excel(os.path.join(DATA_DIR, "Справочник касс.xlsx"), index_col="cash_id")
except FileNotFoundError:
    print("Файл 'Справочник касс.xlsx' не найден")
    exit(1)

joined = cashier.join(reference, on="cash_id", lsuffix='_cash', rsuffix='_ref')

SalesModel.create_by_df(joined)
