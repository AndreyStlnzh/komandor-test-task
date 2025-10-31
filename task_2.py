import os
import pandas as pd
from src.settings import DATA_DIR
from src.db.sales_model import SalesModel


sales = SalesModel.get_all_sales_as_df()

aggregated = sales.groupby(["store_id"]).agg({
    "sale_sum": "sum",
}).round(2)

try:
    store = pd.read_excel(os.path.join(DATA_DIR, "Продажи по магазинам.xlsx"), index_col="store_id")
except FileNotFoundError:
    print("Файл 'Продажи по магазинам' не найден")
    exit(1)


# Индексы совпадают и имеют одинаковый порядок
diff_mask = aggregated["sale_sum"] != store["sale_sum"]
mismatched = aggregated[diff_mask].copy()
mismatched["store_sale_sum"] = store.loc[diff_mask, "sale_sum"]
mismatched[["sale_sum", "store_sale_sum"]]

print("Магазины с различающимися суммами: ", mismatched.index.values.tolist())