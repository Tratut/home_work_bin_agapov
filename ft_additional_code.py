from ft_reverse_code import ft_reverse_code


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
        return cop
    else:
        return cop
