from copy import copy

hex_convert = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

inv_sbox = [["52", "09", "6a", "d5", "30", "36", "a5", "38", "bf", "40", "a3", "9e", "81", "f3", "d7", "fb"],
            ["7c", "e3", "39", "82", "9b", "2f", "ff", "87", "34", "8e", "43", "44", "c4", "de", "e9", "cb"],
            ["54", "7b", "94", "32", "a6", "c2", "23", "3d", "ee", "4c", "95", "0b", "42", "fa", "c3", "4e"],
            ["08", "2e", "a1", "66", "28", "d9", "24", "b2", "76", "5b", "a2", "49", "6d", "8b", "d1", "25"],
            ["72", "f8", "f6", "64", "86", "68", "98", "16", "d4", "a4", "5c", "cc", "5d", "65", "b6", "92"],
            ["6c", "70", "48", "50", "fd", "ed", "b9", "da", "5e", "15", "46", "57", "a7", "8d", "9d", "84"],
            ["90", "d8", "ab", "00", "8c", "bc", "d3", "0a", "f7", "e4", "58", "05", "b8", "b3", "45", "06"],
            ["d0", "2c", "1e", "8f", "ca", "3f", "0f", "02", "c1", "af", "bd", "03", "01", "13", "8a", "6b"],
            ["3a", "91", "11", "41", "4f", "67", "dc", "ea", "97", "f2", "cf", "ce", "f0", "b4", "e6", "73"],
            ["96", "ac", "74", "22", "e7", "ad", "35", "85", "e2", "f9", "37", "e8", "1c", "75", "df", "6e"],
            ["47", "f1", "1a", "71", "1d", "29", "c5", "89", "6f", "b7", "62", "0e", "aa", "18", "be", "1b"],
            ["fc", "56", "3e", "4b", "c6", "d2", "79", "20", "9a", "db", "c0", "fe", "78", "cd", "5a", "f4"],
            ["1f", "dd", "a8", "33", "88", "07", "c7", "31", "b1", "12", "10", "59", "27", "80", "ec", "5f"],
            ["60", "51", "7f", "a9", "19", "b5", "4a", "0d", "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef"],
            ["a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0", "c8", "eb", "bb", "3c", "83", "53", "99", "61"],
            ["17", "2b", "04", "7e", "ba", "77", "d6", "26", "e1", "69", "14", "63", "55", "21", "0c", "7d"]]

rcon = ["01", "02", "04", "08", "10", "20", "40", "80", "1b", "36"]



def inv_sub_bytes(matrix):

    """ This function replaces elements from the matrix to element from inv_sbox """

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
        s_matrix.append(inv_sbox[row][col])
    return s_matrix


def inv_shift_rows(s_matrix):

    """ This function shifts rows of the matrix """

    sh_matrix = [s_matrix[0][0], s_matrix[3][1], s_matrix[2][2], s_matrix[1][3],
                 s_matrix[1][0], s_matrix[0][1], s_matrix[3][2], s_matrix[2][3],
                 s_matrix[2][0], s_matrix[1][1], s_matrix[0][2], s_matrix[3][3],
                 s_matrix[3][0], s_matrix[2][1], s_matrix[1][2], s_matrix[0][3]]

    return sh_matrix


def galoisMult(x, y):
    p = 0
    for i in range(8):
        if y & 1 == 1:
            p ^= x
        hiBitSet = x & 0x80
        x <<= 1
        if hiBitSet == 0x80:
            x ^= 0x1b
        y >>= 1
    return p % 256


def inv_mix_column(column):

    """ This function mixes columns of the matrix """

    temp = copy(column)
    column[0] = galoisMult(temp[0], 14) ^ galoisMult(temp[3], 9) ^ \
                galoisMult(temp[2], 13) ^ galoisMult(temp[1], 11)
    column[1] = galoisMult(temp[1], 14) ^ galoisMult(temp[0], 9) ^ \
                galoisMult(temp[3], 13) ^ galoisMult(temp[2], 11)
    column[2] = galoisMult(temp[2], 14) ^ galoisMult(temp[1], 9) ^ \
                galoisMult(temp[0], 13) ^ galoisMult(temp[3], 11)
    column[3] = galoisMult(temp[3], 14) ^ galoisMult(temp[2], 9) ^ \
                galoisMult(temp[1], 13) ^ galoisMult(temp[0], 11)
    return column


def inv_mix_columns(state):

    """ This function mixes columns of the matrix """

    for p in range(4):
        column = []
        for q in range(4):
            column.append(state[q*4+p])
        inv_mix_column(column)
        for q in range(4):
            state[q*4+p] = column[q]
        return column


def inv_deconvert_m(m):

    """This transcript the message from hexadecimal"""

    dec_message = ""
    message = [m[0], m[4], m[8], m[12],
               m[1], m[5], m[9], m[13],
               m[2], m[6], m[10], m[14],
               m[3], m[7], m[11], m[15]]


    for p in message:
        dec_message = dec_message + (chr(int(p, 16)))
    return dec_message
