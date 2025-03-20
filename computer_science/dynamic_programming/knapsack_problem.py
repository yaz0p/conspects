'''
    Задача о рюкзаке является NP-полной задачей, в которой нужно разместить
    максимальное количество ценных предметов, не выходя за пределы "емкости" емкости

    ________________
    Пример формулировки задачи:

    Даны предметы с весами weights и ценностями values.
    Нужно выбрать предметы с максимальной суммарной ценностью, не превышающей вместимость рюкзака capacity.

    ________________
    Примерное решение:

    Создаём таблицу dp, где dp[i][w] — максимальная ценность для первых i предметов и веса w.

    Заполняем таблицу:
        Если вес текущего предмета больше w, пропускаем его.
        Иначе выбираем максимум из двух вариантов: взять или не взять предмет.
'''

def knapsack(weights, values, capacity):
    '''
    На вход подаются:
        
        - weights - список весов предметов
        - values - список ценности предметов
        - capacity - емкость рюкзака
    '''

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        for w in range(capacity + 1):
            # Вес текущего элемента
            current_weight = weights[i - 1]
            # Ценности текущего элемента
            current_value = values[i - 1]
            if current_weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], current_value + dp[i-1][w - current_weight])
    print(dp)
    return dp[n][capacity]


if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    print(knapsack(weights, values, capacity))  # Вывод: 22

