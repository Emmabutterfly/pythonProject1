
def s(a, b): return a + b
def p(a, b): return a * b
def ch(a, b): return a / b
def r(a, b): return a - b
while True:
    a = float(input('Введите первое число: '))
    c = input('Введите операцию + - / * 0-выход: ')
    if c == '0':
        break
    b = float(input('Введите второе число: '))
    if c == '+':
        print(s(a, b))
    elif c == '-':
        print(r(a, b))
    elif c == '*':
        print(p(a, b))
    elif c == '/':
        try:
            d = a / b
        except ZeroDivisionError:
            print('Деление на ноль')
        else:
            print(ch(a, b))