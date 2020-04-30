

"""
CreateMatrix
"""

message = "abcdefghijklmnop"
for index in message:

    matrix = [[message[0], message[1], message[2], message[3]],
              [message[4], message[5], message[6], message[7]],
              [message[8], message[9], message[10], message[11]],
              [message[12], message[13], message[14], message[15]]
              ]
    continue
print(matrix)

"""
AddRoundKey
"""




"""
SubBytes
"""




"""
ShiftRows
"""

matrix[1].append(matrix[1].pop(0))
matrix[2].append(matrix[2].pop(0))
matrix[2].append(matrix[2].pop(0))
matrix[3].append(matrix[3].pop(0))
matrix[3].append(matrix[3].pop(0))
matrix[3].append(matrix[3].pop(0))
print(matrix)

"""
MixColumns
"""

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

