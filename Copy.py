#얕은 복사와 깊은 복사

x = [[1,2,3],[4,5,6]]

y = x.copy()

x[0][1] = 9

print(x)
print(y)

import copy

x = [[1,2,3],[4,5,6]]

y = copy.deepcopy(x)

x[0][1] = 9

print(x)
print(y)
