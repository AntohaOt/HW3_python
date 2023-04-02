# Создаем переменную 'add':
add = int(input())
# Создаем переменные 'index1' и 'index2', которые будут отвечать за координаты:
index1 = 0
index2 = 0
# Создаем список 'arr':
arr = list(map(int, input().split()))
# Создаем условие: если переменная 'index1' == 'index2' - в ответ выводим 'YES' 
if index1 == index2:
    print('NO')
# Иначе - выводим ответ выводим 'YES' 
else:
    print('YES')