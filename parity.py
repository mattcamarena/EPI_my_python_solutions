def parity(x: int) -> int:
    res  = 0
    while x != 0:
        res ^= (x & 1)
        x = x >> 1
    return res
