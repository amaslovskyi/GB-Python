# На вход программе подаются два числа aa и bb. Напишите программу, которая для каждого кодового значения
# в диапазоне от a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.

num_a, num_b = int(input()), int(input())
for i in range(num_a, num_b + 1):
    print(chr(i), end=' ')
