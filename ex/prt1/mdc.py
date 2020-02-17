def mdc(a, b):
    if a == b:
        return b
    elif b > a:
        return mdc(a, b - a)
    else:
        return mdc(a - b, b)


print(mdc(20, 10))
