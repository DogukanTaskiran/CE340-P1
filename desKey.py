def permute10(key):
    p10_order = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    p10_key = [key[i] for i in p10_order]
    return p10_key

def split_key(p10_key):
    l_half = p10_key[:5]
    r_half = p10_key[5:]
    return l_half, r_half

def one_bit_left_shift(half):
    shifted_half = half[1:] + [half[0]]
    return shifted_half

def permute8(shifted_l, shifted_r):
    combined_key = shifted_l + shifted_r
    p8_order = [5, 2, 6, 3, 7, 4, 9, 8]
    subkey = [combined_key[i] for i in p8_order]
    return subkey

def generate_subkeys(key):
    p10_key = permute10(key)
    l_half, r_half = split_key(p10_key)


    shifted_l = one_bit_left_shift(l_half)
    shifted_r = one_bit_left_shift(r_half)

    k1 = permute8(shifted_l, shifted_r)

    
    shifted_l = one_bit_left_shift(l_half)
    shifted_r = one_bit_left_shift(r_half)

    shifted_l = one_bit_left_shift(shifted_l)
    shifted_r = one_bit_left_shift(shifted_r)

    k2 = permute8(shifted_l, shifted_r)

    return k1, k2


key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]


k1, k2 = generate_subkeys(key)

print("Key-1:", ''.join(map(str, k1)))
print("Key-2:", ''.join(map(str, k2)))
