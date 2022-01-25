def swap_bits(x, i, j):
    # ith and jth bits
    ib = (x >> i) & 1 
    jb = (x >> j) & 1

    # if they are not equal swap bits at position
    if ib != jb: 
        x ^= (1 << i) | (1 << j)
        
    return x
