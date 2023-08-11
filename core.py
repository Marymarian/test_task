import sqlite3
from pandas import read_excel


def preparing_file(filename):
    """Обработка пустых ячеек и ошибок."""

    data = read_excel(
        filename, sheet_name='ИД', header=[0, 1, 2, 4, 5, 6, 7, 8]
    )
    data.dropna(axis=1, thresh=2, inplace=True)
    data.dropna(axis=0, thresh=10, inplace=True)
    return data


def load_sql(filename):
    """Создаем БД и загружаем подготовленный DataFrame.
    Если БД и таблица существует - добавляем данные в нее."""

    con = sqlite3.connect("sources_data.db")
    data = preparing_file(filename)
    data.to_sql(name='sources', con=con, if_exists='append', index=False)
    con.close()
    print(f'Данные из {filename} успешно загружены!')
