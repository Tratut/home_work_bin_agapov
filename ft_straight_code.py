def ft_straight_code(x):
    cop = x
    b = 0
    i = 0
    bad = False

    if cop < 0:
        cop *= -1
        bad = True

    while cop > 0:
        b = (cop % 2) * 10 ** i + b
        cop //= 2
        i += 1
    if bad:
        return b + 1 * 10 ** 7
    else:
        return b
