def ft_len_num(x):
    cop = x
    kol = 0
    while cop != 0:
        cop = cop // 10
        kol += 1
    return kol
