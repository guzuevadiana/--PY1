import random


def get_unique_list_numbers() -> list[int]:
    list_of_numbers = list(range(-10, 11))
    numbers = 15
    unique_list_numbers = []
    for i in range(numbers):
        random_index = random.randint(0, len(list_of_numbers) - 1)
        unique_list_numbers.append(list_of_numbers.pop(random_index))
    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
