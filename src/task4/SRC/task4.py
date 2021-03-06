"""
task4.

Напишите программу, которая сравнивает 2 строки одинаковые ли они. Результат: вывод «ОК», 
если строки идентичны, «КО», если не идентичны. Строки подаются в виде аргументов командной 
строки.

Примечание: во второй строке может быть символ ‘*’ – он заменяет собой любое количество 
любых символов.
На пример:
    «аааа» «аааа» - ОК
    «аааа» «аа*» - ОК
    «a» «*****» - ОК

Дополнение: конечно, в этом задании нас будет интересовать ваш код.
"""
import sys


def compare_two_strings(str1: str, str2: str) -> str:
    """
    Checks two strings for identity.
    Asterisk(if it exists in `str2`) replaces any number of any characters.
    """
    if '*' not in str2 and len(str1) != len(str2): return print('KO')

    for s1, s2 in zip(str1, str2):
        if s2 == '*': return print('OK')
        if s1 != s2: return print('KO')

    return print('OK')

try: compare_two_strings(sys.argv[1], sys.argv[2])
except IndexError: print('py task4.py <str1>? <str2>?')

print('Program finished')
