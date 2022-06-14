
def solution(a, b, c):
    if a == 0:
        if b != 0:
            x1 = (-c/b) ** 0.5
            return x1, None
        elif c == 0:
            return 'all', 'all'
        else:
            return None, None
    d = b ** 2 - 4 * a * c
    if d < 0:
        x1, x2 = None, None
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = None
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2