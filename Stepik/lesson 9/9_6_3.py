"""
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и
использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе
люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять как именно
нужно декодировать данные сообщения. Напишите программу для декодирования этого шифра.
"""

num = int(input())
s = input()
for i in range(len(s)):
    decr = ord(s[i]) - num
    if decr < 97:
        decr = 122 - (96 - decr)
    print(chr(decr), end='')
