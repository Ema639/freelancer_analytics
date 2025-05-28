import pandas as pd
from db.database import engine
from sqlalchemy import text

from tabulate import tabulate


def load_data_from_csv():
    df = pd.read_csv("data/freelancer_earnings_bd.csv")
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]

    df.to_sql("freelancer_data", engine, if_exists="replace", index=False)
    print("CSV успешно загружен в базу PostgreSQL.")


def execute_query(query: str):
    with engine.connect() as connection:
        try:
            result = connection.execute(text(query))
            rows = result.fetchall()
            columns = result.keys()
            df = pd.DataFrame(rows, columns=columns)

            return tabulate(df, headers="keys", tablefmt="pretty", showindex=False)

        except Exception as e:
            return f"Ошибка при выполнении запроса: {e}"


if __name__ == "__main__":
    load_data_from_csv()
