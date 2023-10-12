# Additive Constants
my_constants = [
    0x428A2F98D728AE22, 0x7137449123EF65CD, 0xB5C0FBCFEC4D3B2F, 0xE9B5DBA58189DBBC,
    0x3956C25BF348B538, 0x59F111F1B605D019, 0x923F82A4AF194F9B, 0xAB1C5ED5DA6D8118,
    0xD807AA98A3030242, 0x12835B0145706FBE, 0x243185BE4EE4B28C, 0x550C7DC3D5FFB4E2,
    0x72BE5D74F27B896F, 0x80DEB1FE3B1696B1, 0x9BDC06A725C71235, 0xC19BF174CF692694,
    0xE49B69C19EF14AD2, 0xEFBE4786384F25E3, 0x0FC19DC68B8CD5B5, 0x240CA1CC77AC9C65,
    0x2DE92C6F592B0275, 0x4A7484AA6EA6E483, 0x5CB0A9DCBD41FBD4, 0x76F988DA831153B5,
    0x983E5152EE66DFAB, 0xA831C66D2DB43210, 0xB00327C898FB213F, 0xBF597FC7BEEF0EE4,
    0xC6E00BF33DA88FC2, 0xD5A79147930AA725, 0x06CA6351E003826F, 0x142929670A0E6E70,
    0x27B70A8546D22FFC, 0x2E1B21385C26C926, 0x4D2C6DFC5AC42AED, 0x53380D139D95B3DF,
    0x650A73548BAF63DE, 0x766A0ABB3C77B2A8, 0x81C2C92E47EDAEE6, 0x92722C851482353B,
    0xA2BFE8A14CF10364, 0xA81A664BBC423001, 0xC24B8B70D0F89791, 0xC76C51A30654BE30,
    0xD192E819D6EF5218, 0xD69906245565A910, 0xF40E35855771202A, 0x106AA07032BBD1B8,
    0x19A4C116B8D2D0C8, 0x1E376C085141AB53, 0x2748774CDF8EEB99, 0x34B0BCB5E19B48A8,
    0x391C0CB3C5C95A63, 0x4ED8AA4AE3418ACB, 0x5B9CCA4F7763E373, 0x682E6FF3D6B2B8A3,
    0x748F82EE5DEFB2FC, 0x78A5636F43172F60, 0x84C87814A1F0AB72, 0x8CC702081A6439EC,
    0x90BEFFFA23631E28, 0xA4506CEBDE82BDE9, 0xBEF9A3F7B2C67915, 0xC67178F2E372532B,
    0xCA273ECEEA26619C, 0xD186B8C721C0C207, 0xEADA7DD6CDE0EB1E, 0xF57D4F7FEE6ED178,
    0x06F067AA72176FBA, 0x0A637DC5A2C898A6, 0x113F9804BEF90DAE, 0x1B710B35131C471B,
    0x28DB77F523047D84, 0x32CAAB7B40C72493, 0x3C9EBE0A15C9BEBC, 0x431D67C49C100D4C,
    0x4CC5D4BECB3E42B6, 0x597F299CFC657E2A, 0x5FCB6FAB3AD6FAEC, 0x6C44198C4A475817,
]

# Initial Hash Values
my_hash_values = [
    0x6A09E667F3BCC908, 0xBB67AE8584CAA73B, 0x3C6EF372FE94F82B, 0xA54FF53A5F1D36F1,
    0x510E527FADE682D1, 0x9B05688C2B3E6C1F, 0x1F83D9ABFB41BD6B, 0x5BE0CD19137E2179,
]

def my_rotr(x, n):
    return (x >> n) | (x << (64 - n))

def my_Maj(a, b, c):
    return (a & b) ^ (a & c) ^ (b & c)

def my_Ch(e, f, g):
    return (e & f) ^ (~e & g)

def my_sigma_0(word):
    return my_rotr(word, 1) ^ my_rotr(word, 8) ^ (word >> 7)

def my_sigma_1(word):
    return my_rotr(word, 19) ^ my_rotr(word, 61) ^ (word >> 6)

def my_summation_a(a):
    return my_rotr(a, 28) ^ my_rotr(a, 34) ^ my_rotr(a, 39)

def my_summation_e(e):
    return my_rotr(e, 14) ^ my_rotr(e, 18) ^ my_rotr(e, 41)


def my_addition_modulo_2_64(value):
    return value % (2**64)

def my_pad_message(message):
    message += b"\x80"  # Adding 1 byte (10000000)

    while len(message) % 128 != 112:
        message += b"\x00"

    message += (len(message) * 8).to_bytes(16, "big")

    return message
def my_divide_to_blocks(message):
    blocks = []
    for i in range(0, len(message), 128):
        blocks.append(message[i : i + 128])

    return blocks

my_W = [0] * 80

# My SHA-512 Compression Function
def my_compression_function(message):
    
    a, b, c, d, e, f, g, h = my_hash_values

    for t in range(16):
        my_W[t] = int.from_bytes(message[t * 8 : (t + 1) * 8], byteorder="big")

    for t in range(16, 80):
        my_W[t] = my_sigma_1(my_W[t - 2] + my_W[t - 7]) + my_sigma_0(my_W[t - 15] + my_W[t - 16])

    # Compression Loop
    for t in range(80):
        T1 = h + (my_Ch(e, f, g) + my_summation_e(e) + my_constants[t] + my_W[t])
        T2 = my_summation_a(a) + my_Maj(a, b, c)

        h = g
        g = f
        f = e
        e = my_addition_modulo_2_64(d + T1)
        d = c
        c = b
        b = a
        a = my_addition_modulo_2_64(T1 + T2)

    # Intermediate Hash values
    my_hash_values[0] = my_addition_modulo_2_64(my_hash_values[0] + a)
    my_hash_values[1] = my_addition_modulo_2_64(my_hash_values[1] + b)
    my_hash_values[2] = my_addition_modulo_2_64(my_hash_values[2] + c)
    my_hash_values[3] = my_addition_modulo_2_64(my_hash_values[3] + d)
    my_hash_values[4] = my_addition_modulo_2_64(my_hash_values[4] + e)
    my_hash_values[5] = my_addition_modulo_2_64(my_hash_values[5] + f)
    my_hash_values[6] = my_addition_modulo_2_64(my_hash_values[6] + g)
    my_hash_values[7] = my_addition_modulo_2_64(my_hash_values[7] + h)

message = input("Enter a message: ").encode("utf-8")

padded_message = my_pad_message(message)

blocks = my_divide_to_blocks(padded_message)

for block in blocks:
    my_compression_function(block)

final_hash = "".join(format(h, "016x") for h in my_hash_values)
print(final_hash)

