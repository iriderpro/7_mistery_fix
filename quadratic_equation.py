from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        return root1, None
    else:
        return None, None

print ('введите значение переменных')
A = float(input('a:'))
B = float(input('b:'))
C = float(input('c:'))

R = get_roots(A, B, C)
print ('x1,x2 =', R)
