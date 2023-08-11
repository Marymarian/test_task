from pathlib import Path
from core import load_sql


filename = Path("sources", "working-pf-data1.xlsx")

"""Функции загрузки в БД подается загружаемый файл."""

load_sql(filename)
