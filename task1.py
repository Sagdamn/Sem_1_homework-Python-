# Задача 1: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = input("Введите трехзначное число: ")
n = int(n)
 
k1 = n % 10
k2 = n % 100 // 10
k3 = n // 100
result = k1 + k2 + k3
print(f"{k1} + {k2} + {k3} = {result}")