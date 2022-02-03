from typing import Union, Optional


def calc(a: Union[int, float], b: Union[int, float]) -> int:
    return a + b


def to_int(a_list: list[str]) -> list[int]:
    # в функцию передаем некий список, и она из его элементов делает int
    # пишем, что на входе список строк, на выходе список интов
    return [int(float(e)) for e in a_list]



if __name__ == '__main__':
    print(to_int(['1.5', 4, '5']))
