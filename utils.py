import re
from typing import Iterator, Union, Any, List


def build_query(cmd: str, value: str, file_list: Iterator) -> list:
    """Сортировка данных в зависимости от запроса"""
    methods_list = ["filter", "map", "unique", "sorted", "limit"]

    if cmd not in methods_list:
        raise TypeError("Параметры некорректны")

    else:
        if cmd == "filter":
            # res = [x for x in file_list if value in x]
            res = list(filter(lambda x: value in x, file_list))
            return res

        if cmd == "map":
            value = int(value)
            res = [x.split()[value] for x in file_list]
            print(res)
            return res

        if cmd == "unique":
            res = list(set(file_list))
            # print(len(res))
            return res

        if cmd == "sorted":
            reverse = value = "desc"
            res = list(sorted(file_list, reverse=reverse))
            # print(res)
            return res

        if cmd == "limit":
            value = int(value)
            res = list(file_list)[:value]
            return res

        if cmd == "regex":
            value = re.compile(cmd)
            res = list(file_list)[:value]
            return res
        return []
