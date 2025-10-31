from datetime import datetime
import peewee
import pandas as pd

from src.db.db_connection import db


class SalesModel(peewee.Model):
    date_fact = peewee.DateField(
        default=datetime.now().date()
    )
    store_id = peewee.IntegerField(null=False)
    store_name = peewee.CharField(null=False)
    cash_id = peewee.AutoField(
        primary_key=True,
    )
    cash_name = peewee.CharField(null=False)
    sale_sum = peewee.FloatField(null=False)

    class Meta:
        database = db
        db_table = "sales"


    @classmethod
    def create_by_df(
        cls,
        joined_df: pd.DataFrame,
    ):
        data = [
            {
                "cash_id": indx,
                "store_id": row["store_id"],
                "store_name": row["store_name"],
                "cash_name": row["cash_name_cash"],
                "sale_sum": row["sale_sum"],
            }
            for indx, row in joined_df.iterrows()
        ]
        
        try:
            cls.insert_many(data).execute()
            print("Данные успешно сохранены")
        except peewee.IntegrityError as e:
            print(f"Ошибка вставки: {e}")

    @classmethod
    def get_all_sales_as_df(
        cls
    ):
        
        # [self._dto_from_model(menu_item) for menu_item in self.dish_model.select()]
        # return [sale for sale in cls.select()]
        query = cls.select()
    
        df = pd.DataFrame(list(query.dicts()))
        return df

SalesModel.create_table()
