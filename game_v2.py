"""Игра угадай число"""
""" Компьютер сам загадывает и сам угадывает числа"""

import numpy as np

def random_predict(number: int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    minimum = 0
    maximum = 101
    predict_number = (minimum) + (maximum) // 2
    
    while predict_number != number:
        count += 1
        if number > predict_number:
            minimum = predict_number
        else:
            maximum= predict_number
        predict_number = (minimum) + (maximum) // 2    
    
    return (count)

def score_game(random_predict) -> int:
    """За какое  количество попыток в среднем за 10000 попыток угадвает наш алгаритм

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,100, size=(10000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score
        

print(f'Количество попыток: {random_predict(10)}')

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
