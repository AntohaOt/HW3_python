# Создаем переменную 'word':
word = input()
# Создаем переменную 'index1'. 
# Данная переменная будет равна координате (индексу), на которой нашлась буква 'f':
index1 = word.find('f')
# Создаем переменную 'index2'. 
# Данная переменная так же будет равна координате (индексу), на которой нашлась буква 'f', но используем команду rfind. Данная команда выполняет поиск с обратной стороны:
index2 = word.rfind('f')
# Теперь делаем условие: если координаты 1 и 2 индекса совпали, значит мы нашли одну единственную букву. 
if index1 == index2:
    index = index1 = index2
    # В ответе выводим общий индекс:
    print(index)
# Если же координаты не совпали, значит мы нашли 2 разные буквы. Причем, нам не важно сколкьо их всего в слове, т.к мы нашли сразу индекс первой и последней буквы:
else:
    # В ответ выводим 2 индекса: первый и последний:
    print(index1, index2)