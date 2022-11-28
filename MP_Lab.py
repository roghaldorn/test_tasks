import re


# 1
def string_check(regular):
    def wrapper(arg):
        try:
            regular()
        except TypeError:
            return 'Please enter a String'

    return wrapper


@string_check
def to_camel_case(text):
    """
    Принимает строку, разбивает на слова по разделителю, и возвращает в формате Camel Case.
    В изначальном условии код был в одну строку, но для дальнейшей поддержки лучше использовать
    функцию to_camel_case_zen()
    :param text: String
    :return: String
    """
    return ''.join(list(map(lambda word: word.capitalize(), re.split('_|-', text))))


@string_check
def to_camel_case_zen(text):
    """
    То же самое, но читается лучше.
    :param text: String
    :return: String
    """
    text_list = re.split('_|-', text)
    words_list = list(map(lambda word: word.capitalize(), text_list))
    return ''.join(words_list)


# print(to_camel_case('hello_world'))

# 2
class SingletonMeta(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# 3
count_bits = lambda n: bin(n).count('1')


# 4
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# 5.
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
