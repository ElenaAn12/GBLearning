"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""


def frequency_rate(upper_range, upper_divider, divider=2):
    div_count = len(list(range(divider, upper_range, divider)))
    print(f'В диапазоне 2-{upper_range-1}: {div_count} чисел кратны {divider}')
    if divider == upper_divider:
        return 'Вычисление закончено'
    return frequency_rate(upper_range, upper_divider, divider+1)


if __name__ == '__main__':
    print(frequency_rate(100, 9))
