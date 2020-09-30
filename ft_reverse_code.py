from ft_straight_code import ft_straight_code


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
