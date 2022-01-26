def multiply(x: int, y: int) -> int:
    res = 0
    while x != 0:
        if (x & 1) != 0:
            res = prim_add(y,res)
        x = x >> 1
        y = y << 1
    return res

def prim_add(x: int, y: int) -> int:
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
