'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 19. Пират хочет зарыть К кладов на Т островах. Сформируйте разные варианты размещения кладов..
'''
import time
from itertools import product
import random

# Ввод значений K и T
K = int(input("Введите количество кладов (K): "))
T = int(input("Введите количество островов (T): "))

"""
-----ЧАСТЬ 1-----
"""
print('-----ЧАСТЬ 1-----')
"""
Алгоритмический вариант
"""
start_time_algor = time.time()

per = (T + 1) ** K

# Создание всех возможных вариантов размещения кладов
a = []
for i in range(per):
    a1 = []
    i1 = i
    for _ in range(K):
        a1.append(i1 % (T + 1))
        i1 //= (T + 1)
    a.append(a1)
    
# подсчет ненулевых элементов
def count_nonzero(lst):
    return sum(1 for i in lst if i != 0)
# Сортировка списка по количеству ненулевых элементов
a.sort(key=lambda x: (count_nonzero(x), x))

end_time_algor = time.time()
execution_time_algor = end_time_algor - start_time_algor
print(f"Время выполнения кода (Алгоритмический вариант): {execution_time_algor:.6f} секунд")

"""
С помощью функций
"""
start_time_function = time.time()

def generate_treasure_arrangements(K, T):

    # Создание всех возможных вариантов размещения кладов
    a = list(product(range(T + 1), repeat=K))
    
    # подсчет ненулевых элементов
    def count_nonzero(lst):
        return sum(1 for i in lst if i != 0)
    # Сортировка списка по количеству ненулевых элементов
    a.sort(key=lambda x: (count_nonzero(x), x))
    return a


a = generate_treasure_arrangements(K, T)

end_time_function = time.time()
execution_time_function = end_time_function - start_time_function
print(f"Время выполнения кода с использованием функций: {execution_time_function:.6f} секунд")

if execution_time_algor < execution_time_function:
    print(f"Код (Алгоритмический вариант) быстрее на {execution_time_function - execution_time_algor:.6f} секунд.")
elif execution_time_algor > execution_time_function:
    print(f"Код с использованием функций быстрее на {execution_time_algor - execution_time_function:.6f} секунд.")
else:
    print("Время выполнения кодов одинаково.")
    
want_table = input("Хотите вывести таблицу? (1 - ДА, 0 - НЕТ): ")
if want_table == "1":
    # Заголовок таблицы
    header = ["№ острова"] + [str(i) for i in range(1, T + 1)]

    # Определяем максимальную длину строки для красивого разделения
    max_length = max(len(word) for word in header)
    separator = "+" + "+".join(["-" * max_length for _ in header]) + "+"

    # Печатаем заголовок таблицы
    print(separator)
    print("|" + "|".join(f"{word:^{max_length}}" for word in header) + "|")
    print(separator.replace("-", "="))

    # Печатаем все варианты размещения кладов
    for idx, a1 in enumerate(a):
        row = [f"Вариант {idx + 1}"]
        island_clads = [[] for _ in range(T)]
        for j, island in enumerate(a1):
            if island != 0:
                island_clads[island - 1].append(j + 1)

        for island in island_clads:
            if island:
                row.append("".join(map(str, island)))
            else:
                row.append("0")

        print("|" + "|".join(f"{word:^{max_length}}" for word in row) + "|")
        print()
else:
    print("Таблица не будет выведена.")

"""
-----ЧАСТЬ 2-----
"""
print('-----ЧАСТЬ 2-----')

'''
Ограничение:
Пират хочет зарыть K кладов на T островах. Каждый клад имеет свою стоимость. Общая стоимость кладов должна быть не меньше M. Сформируйте разные варианты размещения кладов.
'''
M = int(input("Введите минимальную общую стоимость: "))

# Создание всех возможных вариантов размещения кладов с присвоением стоимости
a = []
cost = []  
maxcost = 0
for i in range((T + 1) ** K):
    a1 = []
    i1 = i
    cost1 = []
    total_cost = 0
    for _ in range(K):
        island = i1 % (T + 1)
        a1.append(island)
        if island != 0:
            cost_val = random.randint(0,10)
            cost1.append(cost_val)
            total_cost += cost_val
        else:
            cost1.append(0)
        i1 //= (T + 1)
    if total_cost >= M:
        a.append(a1)
        cost.append(cost1)  
        maxcost = max(maxcost, total_cost)
if not a:
    print('нет вариантов удовлетворяющих условию')
else:
    # Заголовок таблицы
    header = ["№ Варианта"] + ["Общая стоимость"] + [f"Остров {i}" for i in range(1, T + 1)]

    # Определяем максимальную длину строки для красивого разделения
    max_length = max(len(word) for word in header)
    separator = "+" + "+".join(["-" * max_length for _ in header]) + "+"

    # Печатаем заголовок таблицы
    print(separator)
    print("|" + "|".join(f"{word:^{max_length}}" for word in header) + "|")
    print(separator.replace("-", "="))

    # Печатаем все варианты размещения кладов
    for idx, (a1, cost1) in enumerate(zip(a, cost)):  
        row = [f"Вариант {idx + 1}"]
        island_clads = [[] for _ in range(T)]
        total_cost = sum(cost1)  
        for j, (island, cost_val) in enumerate(zip(a1, cost1)):
            if island != 0:
                island_clads[island - 1].append(f"{j + 1}({cost_val})")
        row.append(str(total_cost))
        for island in island_clads:
            if island:
                row.append(", ".join(island))
            else:
                row.append("0")

        print("|" + "|".join(f"{word:^{max_length}}" for word in row) + "|")
        print()
    print('Максимальная общая стоимость:', maxcost)

