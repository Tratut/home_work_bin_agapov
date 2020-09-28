def ft_straight_code(x):
    cop = x
    b = 0
    i = 0

    while cop > 0:
        b = (cop % 2) * 10 ** i + b
        cop //= 2
        i += 1
    return b


print(ft_straight_code(30))