hex_convert = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

sbox = [["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
         ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
         ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
         ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
         ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
         ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
         ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
         ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
         ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
         ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
         ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
         ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
         ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
         ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
         ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
         ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]]

rcon = ["01", "02", "04", "08", "10", "20", "40", "80", "1b", "36"]


# nb = number of coloumns
# nr = number of rounds
# nk = the key length

def input_k():

    """ This function takes input the key """

    key_length = input("Choose the key length (128, 192 or 256 bites): ")
    if key_length == "128":
        cipher_key = "I__am__20__y.o.!"
        nk = 4
        nr = 10
        return nr, nk, cipher_key
    elif key_length == "192":
        cipher_key = "I__am__from__Slovakia__!"
        nk = 6
        nr = 12
        return nr, nk, cipher_key
    elif key_length == "256":
        cipher_key = "Hi__,__my__name__is__Teso__12__!"
        nk = 8
        nr = 14
        return nr, nk, cipher_key
    else:
        print("Wrong input...")
        return input_k()


def convert_k():

    """ This function converts the key to list and hex """

    nr, nk, cipher_key = input_k()
    cipher_key = list(cipher_key)
    conv_k = []
    for item in cipher_key:
        p = hex(int(ord(item))).replace("0x", "")
        conv_k.append(p)
    return conv_k, nr, nk


def divide_k():

    """ This function divides the key into 4-lists """

    conv_k, nr, nk = convert_k()
    key = []
    for q in range(nk):
        p = []
        for r in range(4):
            p.append(conv_k[0])
            del conv_k[0]
        key.append(p)
    return key, nr


def shift_k(key):

    """ This function shifts the items in last row of the key """

    sh_k = key[-1].copy()
    sh_k.append(sh_k.pop(0))
    return sh_k


def sub_k(key):

    """ This function replaces elements from the key by element from sbox """

    sh_k = shift_k(key)
    converted_key = []
    su_k = []
    for items in sh_k:
        for item in items:
            if item in hex_convert:
                item = hex_convert[item]
            converted_key.append(item)

    for item in range(4):
        row = int(converted_key[item * 2])
        col = int(converted_key[item * 2 + 1])
        su_k.append(sbox[row][col])
    return su_k


def sub(sh_k):

    """ This function replaces elements from the key by element from sbox """

    converted_key = []
    s_key = []
    for items in sh_k:
        for item in items:
            if item in hex_convert:
                item = hex_convert[item]
            converted_key.append(item)

    for item in range(4):
        row = int(converted_key[item * 2])
        col = int(converted_key[item * 2 + 1])
        s_key.append(sbox[row][col])
    return s_key


def xor_rcon(key, p):

    """ This function does XOR operation """

    su_k = sub_k(key)
    su_k[0] = hex(int(bin(int(su_k[0], 16) ^ int(rcon[p], 16)), 2)).replace("0x", "")
    return su_k


def xor_k(x, y):

    """ This function does XOR operation """

    xor_k = []
    for q in range(4):
        xor_k.append("{0:02x}".format(int(bin(int(x[q], 16) ^ int(y[q], 16)), 2)).replace("0x", ""))
    return xor_k


def expand_k():

    """ This function expands the key """

    key, nr = divide_k()
    if nr == 10:
        for p in range(10):
            s_key = xor_rcon(key, p)
            key.append(xor_k(s_key, key[p * 4]))
            key.append(xor_k(key[p * 4 + 1], key[p * 4 + 4]))
            key.append(xor_k(key[p * 4 + 2], key[p * 4 + 5]))
            key.append(xor_k(key[p * 4 + 3], key[p * 4 + 6]))
    if nr == 12:
        for p in range(8):
            s_key = xor_rcon(key, p)
            key.append(xor_k(s_key, key[p * 6]))
            key.append(xor_k(key[p * 6 + 1], key[p * 6 + 6]))
            key.append(xor_k(key[p * 6 + 2], key[p * 6 + 7]))
            key.append(xor_k(key[p * 6 + 3], key[p * 6 + 8]))
            key.append(xor_k(key[p * 6 + 4], key[p * 6 + 9]))
            key.append(xor_k(key[p * 6 + 5], key[p * 6 + 10]))
    if nr == 14:
        for p in range(7):
            s_key = xor_rcon(key, p)
            key.append(xor_k(s_key, key[p * 8]))
            key.append(xor_k(key[p * 8 + 1], key[p * 8 + 8]))
            key.append(xor_k(key[p * 8 + 2], key[p * 8 + 9]))
            key.append(xor_k(key[p * 8 + 3], key[p * 8 + 10]))
            key.append(xor_k(key[p * 8 + 4], sub(key[p * 8 + 11])))
            key.append(xor_k(key[p * 8 + 5], key[p * 8 + 12]))
            key.append(xor_k(key[p * 8 + 6], key[p * 8 + 13]))
            key.append(xor_k(key[p * 8 + 7], key[p * 8 + 14]))
    return key, nr
