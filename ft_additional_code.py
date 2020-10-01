def ft_len_num(x):
    cop = x
    kol = 0
    while cop != 0:
        cop = cop // 10
        kol += 1
    return kol


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


def ft_reverse_code(x):
    cop = ft_straight_code(x)
    if x < 0:
        for i in range(8):
            fragment = cop % 10 ** i
            cop //= 10 ** i
            if cop % 10 == 1:
                cop -= 1
            elif cop % 10 == 0:
                cop += 1
            cop = cop * 10 ** i + fragment
        return cop
    else:
        return cop


def ft_additional_code(x):
    cop = ft_reverse_code(x)
    ost = 1
    if x < 0:
        for i in range(8):
            if cop // 10 ** i % 10 == 0:
                cop += ost * 10 ** i
                ost = 0
            elif cop // 10 ** i % 10 == 1:
                cop -= ost * 10 ** i
        print("0" * (8 - ft_len_num(cop)), end="")
        print(cop)
    else:
        print("0" * (8 - ft_len_num(cop)), end="")
        print(cop)


ft_additional_code(127)
