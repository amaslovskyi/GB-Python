# На вход программе подается строка. Напишите программу, которая подсчитывает количество
# буквенных символов в нижнем регистре.
s = input()
total = 0
for i in range(len(s)):
    su = s.upper()
    if s[i] != su[i]:
        total += 1
print(total)
