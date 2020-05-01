from copy import copy


def number_of_matrixes(message):

    """This functin returns the number of matrixes"""

    n_o_m = len(message) // 16 + 1
    return n_o_m


def fill_places(message):

    """ This function fills all places in the matrix """

    reminder = len(message) % 16
    if reminder != 0:
        for p in range(0, 16 - reminder):
            message = message + " "
    return message


def convert_m(message):

    """ This function converts the message to list and hex """

    message = fill_places(message)
    message = list(message)
    conv_m = []
    for item in message:
        p = hex(int(ord(item))).replace("0x", "")
        conv_m.append(p)
    return conv_m


def create_matrix(message):

    """ This function divides the message into 16-lists """

    conv_m = convert_m(message)
    n_o_m = number_of_matrixes(message)
    matrix = []
    for q in range(n_o_m):
        p = []
        for r in range(16):
            p.append(conv_m[0])
            del conv_m[0]
        matrix.append(p)
    return matrix


def edit(message):

    """ This function edits the matrix (replaces columns with rows) """

    matrix = create_matrix(message)
    n_u_m = number_of_matrixes(message)
    new_matrix = []
    index = 0
    while n_u_m > 0:

        new_matrix.append([matrix[index][0], matrix[index][4], matrix[index][8], matrix[index][12],
                            matrix[index][1], matrix[index][5], matrix[index][9], matrix[index][13],
                            matrix[index][2], matrix[index][6], matrix[index][10], matrix[index][14],
                            matrix[index][3], matrix[index][7], matrix[index][11], matrix[index][15]])
        n_u_m -= 1
        index += 1

    return new_matrix


def add_round_key(new_matrix, key):

    """ This function add round key """

    mat = []
    mat_with_key = []
    for p in key:
        for q in p:
            mat.append(q)

    for i in range(16):
        k = hex(int(bin(int(new_matrix[i], 16) ^ int(mat[i], 16)), 2)).replace("0x", "")
        mat_with_key.append(k)
    return mat_with_key


def sub_bytes(matrix):

    """ This function replaces elements from matrix to element from sbox """

    converted_matrix = []
    s_matrix = []
    for items in matrix:
        for item in items:
            if item in hex_convert:
                item = hex_convert[item]
            converted_matrix.append(item)

    for item in range(len(matrix)):
        row = int(converted_matrix[item * 2])
        col = int(converted_matrix[item * 2 + 1])
        s_matrix.append(sbox[row][col])
    return s_matrix


def shift_rows(s_matrix):

    """ This function shifts rows of matrix """

    s_matrix[1].append(s_matrix[1].pop(0))
    s_matrix[2].append(s_matrix[2].pop(0))
    s_matrix[2].append(s_matrix[2].pop(0))
    s_matrix[3].append(s_matrix[3].pop(0))
    s_matrix[3].append(s_matrix[3].pop(0))
    s_matrix[3].append(s_matrix[3].pop(0))
    return s_matrix


"""
MixColumns
"""
# Galois Multiplication

def galoisMult(a, b):

    """ This function is  """

    p = 0
    set = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        set = a & 0x80
        a <<= 1
        if set == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256

# mixColumn

def mixColumn(column)

    """ This function """

    temp = copy(column)
    column[0] = galoisMult(temp[0], 2) ^ galoisMult(temp[3], 1) ^ \
                galoisMult(temp[2], 1) ^ galoisMult(temp[1], 3)
    column[1] = galoisMult(temp[1], 2) ^ galoisMult(temp[0], 1) ^ \
                galoisMult(temp[3], 1) ^ galoisMult(temp[2], 3)
    column[2] = galoisMult(temp[2], 2) ^ galoisMult(temp[1], 1) ^ \
                galoisMult(temp[0], 1) ^ galoisMult(temp[3], 3)
    column[3] = galoisMult(temp[3], 2) ^ galoisMult(temp[2], 1) ^ \
                galoisMult(temp[1], 1) ^ galoisMult(temp[0], 3)

# mixColumnInv

def mixColumnInv(column):

    """ This function """

        temp = copy(column)
        column[0] = galoisMult(temp[0], 14) ^ galoisMult(temp[3], 9) ^ \
                    galoisMult(temp[2], 13) ^ galoisMult(temp[1], 11)
        column[1] = galoisMult(temp[1], 14) ^ galoisMult(temp[0], 9) ^ \
                    galoisMult(temp[3], 13) ^ galoisMult(temp[2], 11)
        column[2] = galoisMult(temp[2], 14) ^ galoisMult(temp[1], 9) ^ \
                    galoisMult(temp[0], 13) ^ galoisMult(temp[3], 11)
        column[3] = galoisMult(temp[3], 14) ^ galoisMult(temp[2], 9) ^ \
                    galoisMult(temp[1], 13) ^ galoisMult(temp[0], 11)



def mixColumns(s_matrix):

    """ This function """

    for i in range(4):
        column = []

        for j in range(4):
            column.append(s_matrix[j*4+i])


        mixColumn(column)

        # transfer the new values back into the state table
        for j in range(4):
            s_matrix[j*4+i] = column[j]


def mixColumnsInv(s_matrix):

    """ This function  """

    for i in range(4):
        column = []

        for j in range(4):
            column.append(s_matrix[j*4+i])


        mixColumnInv(column)


        for j in range(4):
            s_matrix[j*4+i] = column[j]

mix = [
[2,3,1,1],
[1,2,3,1],
[1,1,2,3],
[3,1,1,2]]

result = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]


for l in range(len(matrix)):
    for m in range(len(mix[0])):
       for n in range(len(mix)):
           result[l][m] += matrix[l][n] * mix[n][m]

for r in result:
   print(r)







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

