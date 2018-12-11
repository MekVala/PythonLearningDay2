# Module Check Wheather No Is Prime or not


def is_prime(x):
    flag = True
    x = int(x)
    for i in range(2, x):
        if x % i == 0:
            flag = False

    return flag
