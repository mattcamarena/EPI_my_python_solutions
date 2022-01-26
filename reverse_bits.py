def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    res = 0
    for i in range(64):
        res = res << 1
        res += x & 1
        x = x >> 1
    return res
