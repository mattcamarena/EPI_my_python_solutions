def count_bits(x: int) -> int:
    res = 0
    index = 1
    while x != 0:
        if (x & index):
            res+=1

        x = x >> 1

    return res
