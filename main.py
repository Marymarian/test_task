from core import load_sql


"""Функции загрузки в БД подается загружаемый файл."""

filename = "working-pf-data.xlsx"
load_sql(filename)
