from math import sqrt

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a != 0:
    if b != 0 and c != 0:
        d = b * b - 4 * a * c
        print('d = ', d)
        if d < 0:
            print('Нет корней')
        elif d == 0:
            print('Один корень')
            x = -b / (2 * a)
            print('x = ', x)
        else:
            print('Два корня')
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            print('x1 = ', x1, 'x2 = ', x2)
    elif b == 0 and c == 0:
        print('Неполное квадратное уравнение')
    else:
        x1 = 0
        x2 = (-b) / a
        print('x1 = ', x1, 'x2 = ', x2)

else:
    print('а не может быть = 0')