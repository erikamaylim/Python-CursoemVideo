def fatorial(num, ver=False):
    f = 1
    if not ver:
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        for c in range(num, 0, -1):
            f *= c
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        print(f)
        return f


def dobro(num):
    return num * 2


def triplo(num):
    return num * 3
