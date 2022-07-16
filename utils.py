import re
from typing import Iterator, Any


def build_query(cmd: str, value: str, file_list: Iterator) -> list[Any]:
    """Сортировка данных в зависимости от запроса"""
    methods_list = ["filter", "map", "unique", "sorted", "limit", "regex"]

    if cmd not in methods_list:
        raise TypeError("Параметры некорректны")

    else:
        if cmd == "filter":
            # res = [x for x in file_list if value in x]
            res = list(filter(lambda x: value in x, file_list))
            return res

        if cmd == "map":
            res = list([x.split()[int(value)] for x in file_list])
            print(res)
            return res

        if cmd == "unique":
            res = list(set(file_list))
            # print(len(res))
            return res

        if cmd == "sorted":
            # Если значение value передано, то обратная сортировка, иначе прямая
            if value == "desc":
                reverse = True
            else:
                reverse = False
            # reverse = value == "desc"
            res = list(sorted(file_list, reverse=reverse))
            return res

        if cmd == "limit":
            res = list(file_list)[:int(value)]
            return res

        if cmd == "regex":
            regex = re.compile(value)
            res = list(filter(lambda x: regex.search(x), file_list))
            return res
        return []
