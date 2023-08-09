import os
import sqlite3
from pandas import read_excel


os.chdir("C:/Dev/test_task/sources")


def preparing_file(filename):
    """Обработка пустых ячеек и ошибок."""
    data = read_excel(filename, sheet_name='ИД', header=[0, 1, 2, 3, 4, 5, 6, 7]) # skiprows=lambda x: 2<=x<=8
    # data = read_excel(filename, sheet_name='ИД', skiprows=[0, 1, 2, 4, 5, 6, 7]) - если скрыть вложенность заголовков
    data.dropna(axis=1, thresh=2, inplace=True)
    data.dropna(axis=0, thresh=10, inplace=True)
    return data

def load_sql(filename):
    """Создаем БД и загружаем подготовленный DataFrame."""
    con = sqlite3.connect('C:/Dev/test_task/sources_data.db')
    data = preparing_file(filename)
    data.to_sql(name='sources', con=con, if_exists='replace')
    con.commit()
    con.close()
