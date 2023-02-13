# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

n=int(input('введите число Фибоначчи ='))

def fibanacci(n):
    if n==1:
       return 0
    elif n==2:
        return 1
    return  fibanacci(n-1) + fibanacci(n-2)
print(fibanacci(n))

