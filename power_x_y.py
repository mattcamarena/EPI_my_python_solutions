def power(x: float, y: int) -> float:
    # TODO - you fill in here
    res = 1
    if y < 0:
        y *= -1
        x = 1.0/x

    while y != 0:
        if (y & 1) != 0:
            res *= x
        x *= x
        y = y >> 1
        
    return res

