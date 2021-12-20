# IMPLEMENTING PLAYFAIR CIPHER : Sec C

import string

# Step 1 : Creating the Key Matrix (5x5 matrix) based on
# a secret keyword - “playfair example”

keyword = input("enter the KEYWORD : ")  # keyword for creating the key matrix
keyword = keyword.replace(" ", "")
print("Keyword is : ", keyword)

english_alphabets = string.ascii_lowercase
english_alphabets = english_alphabets.replace("j", ".")

print("Reference String is : ", english_alphabets)
print()

# initialise the key matrix

key_matrix = ['' for i in range(5)]
print("Initialised KEY MATRIX : ")
print(key_matrix)
print()

# Populating the key matrix based on the secret keyword

row = 0
column = 0

for char in keyword:

    if char in english_alphabets:

        key_matrix[row] += char
        # print(key_matrix)
        english_alphabets = english_alphabets.replace(char, ".")
        # print(english_alphabets)
        column = column + 1

        if column > 4:
            row += 1
            column = 0

print("Key Matrix Populated only with the Key Word Characters :")
print(key_matrix)
print()

for char in english_alphabets:

    if char != ".":

        key_matrix[row] += char
        column += 1

        if column > 4:
            row = row + 1
            column = 0

print("The Final Key Matrix is ")
print(key_matrix)
print()

# Step 2 : Accepting the plain Text to be encrypted and converting it
# into digrams based on below rules :

plain_text = input("Enter the plain text : ")
plain_text = plain_text.replace(" ", "")
plain_text = plain_text.replace("j", "i")
print()

# Creating Plain Text Digram based the rules :

plain_text_digrams = []

# Rule 1 : No two digram characters can be identical
# (so if they are identical , split them and add filler character - ‘X’)
# Rule 2 : If the any character stands alone after the execution of rule 1 in step 2 ,
# add filler character to that

i = 0

while i < len(plain_text):

    char1 = plain_text[i]
    char2 = ''

    if (i + 1) == len(plain_text):

        char2 = 'x'

    else:

        char2 = plain_text[i + 1]

    if char1 != char2:

        plain_text_digrams.append(char1 + char2)
        i = i + 2

    else:

        plain_text_digrams.append(char1 + 'x')
        i = i + 1

print()
print("The Plain Text Divided into Digrams is : ")
print(plain_text_digrams)

# Encryption Process Starts here :

cipher_text_digrams = []  # store all the cipher text digrams as and when we encrypt them

for digram in plain_text_digrams:

    # Rule 1 : Both digram characters belong to same row then Replace each
    # of them with the immediate character to the right (wrap around)
    # [ or , an ,ge ] - or - digram[0] = 'a' digram[1] = 'n'

    applied_rule = False

    for row in key_matrix:

        if digram[0] in row and digram[1] in row:
            col0 = row.find(digram[0])
            col1 = row.find(digram[1])

            ct_pair = row[(col0 + 1) % 5] + row[(col1 + 1) % 5]

            cipher_text_digrams.append(ct_pair)

            applied_rule = True

    if applied_rule:
        continue

    # Rule 2 : If both the plain text digram characters fall in the same
    # column then Replace each character of the digram with the character immediately below that character
    # 2. cellular - [ ce , lu , la , rx] || PT = [ el , um , sm , r = [0][4] ; x = [4][3]
    # Ct:  r = [0][3] = a ; x = [4][4] z || ra : az

    for j in range(5):

        col = "".join([key_matrix[i][j] for i in range(5)])

        if digram[0] in col and digram[1] in col:
            row0 = col.find(digram[0])
            row1 = col.find(digram[1])

            ct_pair = col[(row0 + 1) % 5] + col[(row1 + 1) % 5]

            cipher_text_digrams.append(ct_pair)

            applied_rule = True

    if applied_rule:
        continue

    # Rule 3 : if both the characters of the digram belong to different rows and columns,
    # replace each character with a character that belongs to the same row as that of the
    #  character but column as that of the other character

    # Capture both the rows and columns of each character of the digram

    # For char1 of the digram
    row0 = 0
    col0 = 0

    # For char 2 of the digram

    row1 = 0
    col1 = 0

    for i in range(5):

        row = key_matrix[i]

        if digram[0] in row:
            row0 = i
            col0 = row.find(digram[0])

        if digram[1] in row:
            row1 = i
            col1 = row.find(digram[1])

    ct_pair = key_matrix[row0][col1] + key_matrix[row1][col0]

    cipher_text_digrams.append(ct_pair)

# - O/P Cipher Text Digrams - combine them to get the cipher text
print()
print("Cipher Text Digrams is : ")
print(cipher_text_digrams)

# Cipher Text is got by combining all the digrams into a string

cipher_text = "".join(cipher_text_digrams)
print()
print("The Cipher Text is : ", cipher_text)
