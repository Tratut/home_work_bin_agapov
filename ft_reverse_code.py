from ft_len_num import ft_len_num
from ft_straight_code import ft_straight_code


def abss(x):
    if x < 0:
        x *= -1
    return x


def ft_reverse_code(x):
    cop = ft_straight_code(x)
    kol = ft_len_num(cop)
    out = 0

    for i in range(kol):
        kek = abss(cop % 10 - 1)
        out = kek * 10 ** i + out
        cop //= 10
    return out
