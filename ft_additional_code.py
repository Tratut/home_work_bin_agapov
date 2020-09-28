from ft_reverse_code import ft_reverse_code
from ft_len_num import ft_len_num


def ft_additional_code(x):
    cop = ft_reverse_code(x)
    kol = ft_len_num(cop)
    ost = 1
    for i in range(kol):
        if cop // 10 ** i % 10 == 0:
            cop += ost * 10 ** i
            ost = 0
        elif cop // 10 ** i % 10 == 1:
            cop -= ost * 10 ** i
    return cop

# print(ft_additional_code(30))
