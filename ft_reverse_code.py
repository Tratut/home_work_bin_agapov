from ft_straight_code import ft_straight_code
from ft_len_num import ft_len_num


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
        print("0" * (8 - ft_len_num(cop)), end="")
        print(cop)
    else:
        print("0" * (8 - ft_len_num(cop)), end="")
        print(cop)
