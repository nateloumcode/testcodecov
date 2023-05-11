def offset(a, b):
    return float(a) + float(b)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError()
    return float(a) / float(b)


def exponentiate(base, exponent):
    return float(base) ** float(exponent)
