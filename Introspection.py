
import inspect
import sys

class Intro:
    def __init__(self, obj):
        self.value = obj


def introspection_info(num):
    a = Intro(num)
    return (f' type: {type(a.value)},\n '
            f'dir_a: {dir(a)},\n '
            f'attributes_value: {hasattr(a, 'value')},\n '
            f'getattr: {getattr(a, 'value')},\n'
            f' getattr_name: {getattr(a, 'name', 'нет такого')},\n '
            f'module:{inspect.getmodule(a)}, \n'
            f' is_class: {inspect.isclass(a)} \n'
            f' is_class: {inspect.isclass(Intro)} \n'
            f' is_istance_str: {isinstance(a.value, str)}\n')

number_info = introspection_info(42)
print(number_info)

