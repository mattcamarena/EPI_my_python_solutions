    temp = x
    searchforzero = False

    for i in range(64):
        #found a 1 bit
        if not searchforzero and (x & 1) == 1:
            # edge case first num is a 1 find first 0
            if i == 0:
                searchforzero = True
            else:
                return swap_bits(temp,i,i-1)

        elif searchforzero and (x & 1) == 0: 
            #found the first 0 swap here and last element
            return swap_bits(temp,i,i-1)
        x = x >> 1

def swap_bits(x, i, j):
    # ith and jth bits
    ib = (x >> i) & 1 
    jb = (x >> j) & 1

    # if they are not equal create a mask to swap bits
    if ib != jb: 
        x ^= (1 << i) | (1 << j)
    return x
