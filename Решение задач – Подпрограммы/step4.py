# 4. Напишите функцию поиск_максимального_элемента(), которая
# принимает список чисел в качестве аргумента и возвращает максимальное
# число из списка. Затем вызовите функцию с разными списками чисел.

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_max([1, 2, 3, 4, 5]))
print(find_max([10, 20, 30, 40, 50]))
print(find_max([-1, -2, -3, -4, -5]))
