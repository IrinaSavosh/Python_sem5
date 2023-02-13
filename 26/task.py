# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

n = int(input('Введите число: '))
m = int(input('Введите степень: '))

def degree(number, deg):
   if deg==1:
       return number
   return(n * degree(number, deg-1))
   
print(degree(n,m))
