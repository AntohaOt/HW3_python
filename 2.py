# Создаем переменную 'a':
a = int(input())
# Создаем список, в котором изначально находиться только одно число - 0:
arr = [0]
# Создаем переменную 'i':
i = 0
# Создаем цикл, который будет присваивать 'b' все количество переменных в списке 'arr':
for b in range(len(arr)):
    # Создаем цикл, который будет присваивать 'n' значение 'arr':
    for n in arr:
        # Создаем условие: если элементы последовательности в списке равны 0 - меняем их на 1, путем добавления единицы:
        if arr[i] == 0:
            arr[i] = n + 1
            # Проверяем дальше:
            i += 1
        # Создаем условие: если элементы последовательности в списке равны 1 - меняем их на 0, путем вычитания единицы:
        elif arr[i] == 1:
            arr[i] = n - 1
            # Проверяем дальше:
            i += 1
    # После завершения цикла, добавляем получившиеся значения в конец нашего списка, и повторяем те же действия, пока не дойдем до нужного результата:
    arr.append(*arr)
# В ответе выводим значения списка, начиная с первого элемента, и заканчивая элементом на 'a' месте:
print(*arr[0 : a])
