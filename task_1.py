import pandas as pd

from src.db.sales_model import SalesModel

cashier = pd.read_excel("data\Продажи по кассам.xlsx", index_col="cash_id")
reference = pd.read_excel("data\Справочник касс.xlsx", index_col="cash_id")

joined = cashier.join(reference, on="cash_id", lsuffix='_cash', rsuffix='_ref')

SalesModel.create_by_df(joined)
