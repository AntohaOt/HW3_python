def can_eat(a, b):
    dr = abs(a[0] - b[0]), abs(a[1] - b[1])
    return dr in ((1, 2), (2, 1))
 
k = (4, 4)
from itertools import product
for i, c in enumerate(product(range(8), repeat=2), 1):
    print('♞◯⛒'[(k!=c)+can_eat(k,c)], end=' \n'[i%8==0])
