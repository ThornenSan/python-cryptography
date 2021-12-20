# Playfair Decryption Algorithm Implementation _ Sec C

import string

# Step 1 : Receive the keyword and create the key matrix based on the key

keyword = input("Enter the keyword : ")

reference_string = string.ascii_lowercase.replace("j", "")
print("Reference String is : ", reference_string)

# Creating Key Matrix [K] 5x5 matrix - List

key_matrix = ['', '', '', '', '']
print()
print("Initialised key matrix is : ")
print(key_matrix)

# Populate the key matrix initially based on unique keyword alphabets by traversing the keyword

row = 0
column = 0

for char in keyword:

    if char in reference_string:

        key_matrix[row] += char

        reference_string = reference_string.replace(char, "")

        column = column + 1

        if column > 4:
            column = 0
            row = row + 1

print()
print("The Key Matrix Populated using unique characters from the keyword : ")
print(key_matrix)

# Populate the key matrix with the remaining characters of reference string

for char in reference_string:

    key_matrix[row] += char
    column += 1

    if column > 4:
        column = 0
        row += 1

print()
print("The Final Key Matrix is : ")
print(key_matrix)
# Step 2 : Input the cipher text for decryption. And split it into  CT digrams.
# (Note : CT length is even and also there will be no adjacent identical characters. So no need for fillers)
print()
cipher_text = input("Enter The Cipher Text : ")

cipher_text_digrams = []  # list to which CT digrams will be added

i = 0

while i < len(cipher_text):
    char1 = cipher_text[i]
    char2 = cipher_text[i + 1]

    cipher_text_digrams.append(char1 + char2)

    i = i + 2

print()
print("Cipher Text Digrams is : ")
print(cipher_text_digrams)

# Step 3 : Take each digram and capture their indexes in the key matrix and based
# on their relative positions do the below to get PT digrams:
# Step 3.1 : if both CT characters belong to the same row of the key matrix , replace each with the character
# to the left (wrap)

plain_text_digrams = []

for digram in cipher_text_digrams:

    applied_rule = False

    for row in key_matrix:

        if digram[0] in row and digram[1] in row:
            col0 = row.find(digram[0])
            col1 = row.find(digram[1])

            # keep rows same but decrement cols to get the PT digram

            pt_digram = row[(col0 - 1) % 5] + row[(col1 - 1) % 5]

            plain_text_digrams.append(pt_digram)

            applied_rule = True

    if applied_rule:
        continue

    # Step 3.2 : if both the CT characters belong to the same column in the key matrix,
    # replace each with the char above them (wrap)

    for col in range(5):

        column = "".join([key_matrix[row][col] for row in range(5)])
        # print(column)

        if digram[0] in column and digram[1] in column:
            row0 = column.find(digram[0])
            row1 = column.find(digram[1])

            # keep columns same but decrement rows to get the PT digram

            pt_digram = column[(row0 - 1) % 5] + column[(row1 - 1) % 5]

            plain_text_digrams.append(pt_digram)

            applied_rule = True

    if applied_rule:
        continue

    # Step 3.3 : if both the characters of the CT digram are in different rows and columns of the
    # key matrix : replace each CT character with char in the same row as that of the CT char but
    # col as that of the other CT character in the CT digram

    i0 = 0
    j0 = 0
    # row and column indexes of digram[0]

    i1 = 0
    j1 = 0

    # row and column indexes of digram[1]

    for i in range(5):

        row = key_matrix[i]

        if digram[0] in row:
            i0 = i
            j0 = row.find(digram[0])

        if digram[1] in row:
            i1 = i
            j1 = row.find(digram[1])

    pt_digram = key_matrix[i0][j1] + key_matrix[i1][j0]

    plain_text_digrams.append(pt_digram)

print()
print("The Plain Text Digrams is : ")
print(plain_text_digrams)
print()

plain_text = "".join(plain_text_digrams)
print("Plain Text is : ", plain_text)
