# Создаем переменную 'add':
add = int(input())

# Создаем переменные 'x' и 'y', которые будут отвечать за координаты:
index1 = 0
index2 = 0

def is_symmetric(a):
    for x in range(add):
        for y in range(add):
            if a[index1][index2] == a[index2][index1]:
                return True
    return False
 

arr = [list(map(int, input().split())) for i in range(add)]

if is_symmetric(arr):
    
    print('YES')
else:
    print('NO')