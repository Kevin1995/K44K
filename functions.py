import math
import random
import numpy as np
import movements
import sboxes
import required_tables
import mix_columns_tables

# CREATE MULTIPLE KEYS BASED ON LENGTH OF KEY. WE USE A DIFFERENT KEY FOR EACH ROUND OF ENCRYPTION/DECRYPTION
def key_schedule(secret_key, keys):
    # WE NEED TO MAKE THESE ARRAYS FOR EACH KEY
    current_key_0 = []
    final_key_0 = []
    # Hex the key before we start the key schedule
    secret_key = secret_key.encode('utf-8').hex()
    # WE FIX KEY 0 SO THAT IT GOES UP - DOWN INSTEAD OF LEFT TO RIGHT
    for i in range(4):
        current_key_0 = [secret_key[i:i+2] for i in range(0, len(secret_key), 2)]
        current_key_0 = [j for j in current_key_0[i::4]]
        for i in current_key_0:
            final_key_0.append(i)
    # ADD THE FIXED KEY INTO THE KEYS ARRAY. WE CAN REFERENCE THIS BY INDEX 0
    keys.append(final_key_0)
    if len(secret_key) == 32:
        # Make first column for key 1
        for i in range(0, 11):
            first_column = [keys[i][required_tables.last_array_index_16_bit[-1][0]], keys[i][required_tables.last_array_index_16_bit[-1][1]], keys[i][required_tables.last_array_index_16_bit[-1][2]], keys[i][required_tables.last_array_index_16_bit[-1][3]]]
            last_column = [keys[i][required_tables.current_array_index_16_bit[-1][0]], keys[i][required_tables.current_array_index_16_bit[-1][1]], keys[i][required_tables.current_array_index_16_bit[-1][2]], keys[i][required_tables.current_array_index_16_bit[-1][3]]]

            # Make next keys_array
            keys.append([None] * 12)

            last_column = ks_rotword(last_column)
            last_column = sboxes.encrypt_sbox(last_column)
            last_column = xor_with_rcon(first_column, last_column, i)

            keys[i+1].insert(required_tables.last_array_index_16_bit[-1][0], last_column[0])
            keys[i+1].insert(required_tables.last_array_index_16_bit[-1][1], last_column[1])
            keys[i+1].insert(required_tables.last_array_index_16_bit[-1][2], last_column[2])
            keys[i+1].insert(required_tables.last_array_index_16_bit[-1][3], last_column[3])

            j = 0
            while j < 4:
                value1 = non_array_xor(keys[i][required_tables.last_array_index_16_bit[j][0]], keys[i+1][required_tables.current_array_index_16_bit[j][0]])
                value2 = non_array_xor(keys[i][required_tables.last_array_index_16_bit[j][1]], keys[i+1][required_tables.current_array_index_16_bit[j][1]])
                value3 = non_array_xor(keys[i][required_tables.last_array_index_16_bit[j][2]], keys[i+1][required_tables.current_array_index_16_bit[j][2]])
                value4 = non_array_xor(keys[i][required_tables.last_array_index_16_bit[j][3]], keys[i+1][required_tables.current_array_index_16_bit[j][3]])

                keys[i+1][required_tables.current_array_index_16_bit[j+1][0]] = value1
                keys[i+1][required_tables.current_array_index_16_bit[j+1][1]] = value2
                keys[i+1][required_tables.current_array_index_16_bit[j+1][2]] = value3
                keys[i+1][required_tables.current_array_index_16_bit[j+1][3]] = value4
                j += 1

                # Break out of the while loop
                if j == 3:
                    j = 4
    elif len(secret_key) == 48:
        # Make first column for key 1
        for i in range(0, 12):
            first_column = [keys[i][required_tables.last_array_index_24_bit[-1][0]], keys[i][required_tables.last_array_index_24_bit[-1][1]], keys[i][required_tables.last_array_index_24_bit[-1][2]], keys[i][required_tables.last_array_index_24_bit[-1][3]]]
            last_column = [keys[i][required_tables.current_array_index_24_bit[-1][0]], keys[i][required_tables.current_array_index_24_bit[-1][1]], keys[i][required_tables.current_array_index_24_bit[-1][2]], keys[i][required_tables.current_array_index_24_bit[-1][3]]]

            # Make next keys_array
            keys.append([None] * 20)

            last_column = ks_rotword(last_column)
            last_column = sboxes.encrypt_sbox(last_column)
            last_column = xor_with_rcon(first_column, last_column, i)

            keys[i+1].insert(required_tables.last_array_index_24_bit[-1][0], last_column[0])
            keys[i+1].insert(required_tables.last_array_index_24_bit[-1][1], last_column[1])
            keys[i+1].insert(required_tables.last_array_index_24_bit[-1][2], last_column[2])
            keys[i+1].insert(required_tables.last_array_index_24_bit[-1][3], last_column[3])

            j = 0
            while j < 6:
                value1 = non_array_xor(keys[i][required_tables.last_array_index_24_bit[j][0]], keys[i+1][required_tables.current_array_index_24_bit[j][0]])
                value2 = non_array_xor(keys[i][required_tables.last_array_index_24_bit[j][1]], keys[i+1][required_tables.current_array_index_24_bit[j][1]])
                value3 = non_array_xor(keys[i][required_tables.last_array_index_24_bit[j][2]], keys[i+1][required_tables.current_array_index_24_bit[j][2]])
                value4 = non_array_xor(keys[i][required_tables.last_array_index_24_bit[j][3]], keys[i+1][required_tables.current_array_index_24_bit[j][3]])

                keys[i+1][required_tables.current_array_index_24_bit[j+1][0]] = value1
                keys[i+1][required_tables.current_array_index_24_bit[j+1][1]] = value2
                keys[i+1][required_tables.current_array_index_24_bit[j+1][2]] = value3
                keys[i+1][required_tables.current_array_index_24_bit[j+1][3]] = value4
                j += 1

                # Break out of the while loop
                if j == 5:
                    j = 6
    elif len(secret_key) == 64:
        # Make first column for key 1
        for i in range(0, 14):
            #print(f"key {i}")
            first_column = [keys[i][required_tables.last_array_index_32_bit[-1][0]], keys[i][required_tables.last_array_index_32_bit[-1][1]], keys[i][required_tables.last_array_index_32_bit[-1][2]], keys[i][required_tables.last_array_index_32_bit[-1][3]]]
            last_column = [keys[i][required_tables.current_array_index_32_bit[-1][0]], keys[i][required_tables.current_array_index_32_bit[-1][1]], keys[i][required_tables.current_array_index_32_bit[-1][2]], keys[i][required_tables.current_array_index_32_bit[-1][3]]]

            # Make next keys_array
            keys.append([None] * 28)

            last_column = ks_rotword(last_column)
            last_column = sboxes.encrypt_sbox(last_column)
            last_column = xor_with_rcon(first_column, last_column, i)

            keys[i+1].insert(required_tables.last_array_index_32_bit[-1][0], last_column[0])
            keys[i+1].insert(required_tables.last_array_index_32_bit[-1][1], last_column[1])
            keys[i+1].insert(required_tables.last_array_index_32_bit[-1][2], last_column[2])
            keys[i+1].insert(required_tables.last_array_index_32_bit[-1][3], last_column[3])

            j = 0
            while j < 8:
                if j == 4:
                    #print(f"4TH COLUMN OF KEY {i}")
                    first_column = [keys[i][required_tables.last_array_index_32_bit[j][0]], keys[i][required_tables.last_array_index_32_bit[j][1]], keys[i][required_tables.last_array_index_32_bit[j][2]], keys[i][required_tables.last_array_index_32_bit[j][3]]]
                    last_column = [keys[i+1][required_tables.current_array_index_32_bit[j][0]], keys[i+1][required_tables.current_array_index_32_bit[j][1]], keys[i+1][required_tables.current_array_index_32_bit[j][2]], keys[i+1][required_tables.current_array_index_32_bit[j][3]]]

                    last_column = sboxes.encrypt_sbox(last_column)
                    temp_holder = []
                    for index, value in enumerate(last_column):
                        xor_calc = non_array_xor(first_column[index], last_column[index])
                        temp_holder.append(xor_calc)

                    keys[i+1][required_tables.current_array_index_32_bit[j+1][0]] = temp_holder[0]
                    keys[i+1][required_tables.current_array_index_32_bit[j+1][1]] = temp_holder[1]
                    keys[i+1][required_tables.current_array_index_32_bit[j+1][2]] = temp_holder[2]
                    keys[i+1][required_tables.current_array_index_32_bit[j+1][3]] = temp_holder[3]
                    j += 1
                else:
                    value1 = non_array_xor(keys[i][required_tables.last_array_index_32_bit[j][0]], keys[i+1][required_tables.current_array_index_32_bit[j][0]])
                    value2 = non_array_xor(keys[i][required_tables.last_array_index_32_bit[j][1]], keys[i+1][required_tables.current_array_index_32_bit[j][1]])
                    value3 = non_array_xor(keys[i][required_tables.last_array_index_32_bit[j][2]], keys[i+1][required_tables.current_array_index_32_bit[j][2]])
                    value4 = non_array_xor(keys[i][required_tables.last_array_index_32_bit[j][3]], keys[i+1][required_tables.current_array_index_32_bit[j][3]])

                    keys[i+1][required_tables.current_array_index_32_bit[j+1][0]] = value1
                    keys[i+1][required_tables.current_array_index_32_bit[j+1][1]] = value2
                    keys[i+1][required_tables.current_array_index_32_bit[j+1][2]] = value3
                    keys[i+1][required_tables.current_array_index_32_bit[j+1][3]] = value4
                    j += 1

                    # Break out of the while loop
                    if j == 7:
                        j = 8
    else:
        print("KEY MUST BE IN EITHER 128, 192, OR 256 BITS OF LENGTH")
        print("PLEASE FIX THE LENGTH OF THE KEY")
        exit()
    for index, array in enumerate(keys):
        round_key = ""
        for j in array:
            round_key = round_key + j
        print(f"Key {index} is {round_key}")
    print("")
    return keys

# CREATE THE 4x4x4 CUBE (Total 96 faces)
def create_cube():
    up_face = np.full(16,"  ").reshape(4,4)
    down_face = np.full(16,"  ").reshape(4,4)
    left_face = np.full(16,"  ").reshape(4,4)
    front_face = np.full(16,"  ").reshape(4,4)
    right_face = np.full(16,"  ").reshape(4,4)
    back_face = np.full(16,"  ").reshape(4,4)
    return up_face, down_face, left_face, front_face, right_face, back_face

# WE CREATE OUR NEW CIPHERTEXT (BASED ON LENGTH OF KEY)
# WE DO DIFFERENT OPERATIONS TO ENCRYPT THE PLAINTEXT
def aes_operation(plaintext, keys_array):
    # SETUP ARRAY THAT WILL HOLD ALL THE VALUES NEEDED FOR RANDOM_ORIENTATION
    ciphertext_array = []
    plaintext_splitter = []
    # CHANGE THE PLAINTEXT SO IT GOES DOWN TO UP RATHER THAN LEFT TO RIGHT
    plaintext_hexed = plaintext
    plaintext_hexed = plaintext_hexed.encode('utf-8').hex()
    plaintext_splitter = [plaintext_hexed[i:i+2] for i in range(0, len(plaintext_hexed), 2)]
    for index, value in enumerate(keys_array):
        if index == 0:
            round_result = xor(plaintext_splitter, value)
            ciphertext_array.append(round_result)
        elif index == len(keys_array) - 1:
            round_result = sboxes.encrypt_sbox(ciphertext_array[index-1])
            round_result = shift_rows(round_result)
            round_result = xor(round_result, value)
            ciphertext_array.append(round_result)
        else:
            round_result = sboxes.encrypt_sbox(ciphertext_array[index-1])
            round_result = shift_rows(round_result)
            round_result = mix_columns_tables.mix_column_encryption(round_result)
            round_result = xor(round_result, value)
            ciphertext_array.append(round_result)

    # REMOVE THE FIRST 5/8/11 ELEMENTS SO WE HAVE 96 ELEMENTS FOR FACE
    if len(ciphertext_array) == 12:
        del ciphertext_array[0:6]
    elif len(ciphertext_array) == 13:
        del ciphertext_array[0:9]
    elif len(ciphertext_array) == 15:
        del ciphertext_array[0:12]
    
    return ciphertext_array

# WE CHOOSE THE NEXT FACE ON THE CUBNE THAT IS EMPTY AND PLACE THE NEXT HEX VALUE ON IT
# WE ALSO STORE THE FACE POSITIONS (VALUES 0 - 95) SO WE KNOW WHEN HEX VALUE EQAULS THE ORIENTATION VALUE
def random_orientation(up_face, down_face, left_face, front_face, right_face, back_face, xor, orientation):
    faces = [up_face, down_face, left_face, front_face, right_face, back_face]
    xor = np.array(xor)
    xor = xor.ravel()
    i = 0
    while i < 96:
        index, column, row = choose_random_face(faces)
        if faces[index][column][row] == "  ":
            faces[index][column][row] = xor[i]
            i += 1
            final_value = len(faces[index][column]) * 4 * index + len(faces[index][column]) * column + row
            orientation.append(final_value)
    up_face, down_face, left_face, front_face, right_face, back_face = faces[0], faces[1], faces[2], faces[3], faces[4], faces[5]
    print("4x4 Rubiks Cube after placing the Ciphertext.")
    print("Up Face")
    print(f"{up_face} \n")
    print("Down Face")
    print(f"{down_face} \n")
    print("Left Face")
    print(f"{left_face} \n")
    print("Front Face")
    print(f"{front_face} \n")
    print("Right Face")
    print(f"{right_face} \n")
    print("Back Face")
    print(f"{back_face} \n")
    return up_face, down_face, left_face, front_face, right_face, back_face, xor, orientation

# LOOP THROUGH OUT MULTIDIMENSIONAL ARRAY AND CHECK IF THE CURRENT FACE IS EMPTY
# WE THEN RETURN THE INDEXES NEEDED SO THE HEX VALUE CAN BE APPLIED TO THAT FACE
def choose_random_face(faces):
    for a in range(0, 6):
        for b in range(0, 4):
            for c in range(0, 4):
                if faces[a][b][c] == "  ":
                    return a, b, c

# WE WILL DO 96 RANDOM CUBE MOVEMENTS AND STORE THEM IN AN ARRAY
# THE ROT_KEY IS MADE BY JOINING THE MOVEMENTS AND THE CUBE POSITIONS TOGETHER.
def scramble_rot_key(up_face, down_face, left_face, front_face, right_face, back_face, orientation, final_key, ciphertext):
    faces = [up_face, down_face, left_face, front_face, right_face, back_face]
    rotation_key_array = []
    for i in range(96):
        index = random.randrange(0, len(movements.movements))
        up_face, down_face, left_face, front_face, right_face, back_face = movements.movements[index][1](up_face, down_face, left_face, front_face, right_face, back_face)
        rotation_key_array.append(movements.movements[index][0])

    faces = [up_face, down_face, left_face, front_face, right_face, back_face]
    random.shuffle(orientation)
    ciphertext = ciphertext_altering(orientation, ciphertext, faces)
    rotation_key_array.reverse()
    final_key = ""
    for i, v in enumerate(rotation_key_array):
        final_key = final_key + v + str(orientation[i])
    print("Ciphertext after cube rotation: " + ciphertext + '\n')
    
    print("4x4 Rubiks Cube after scramble")
    print("Up Face")
    print(f"{up_face} \n")
    print("Down Face")
    print(f"{down_face} \n")
    print("Left Face")
    print(f"{left_face} \n")
    print("Front Face")
    print(f"{front_face} \n")
    print("Right Face")
    print(f"{right_face} \n")
    print("Back Face")
    print(f"{back_face} \n")
    return up_face, down_face, left_face, front_face, right_face, back_face, final_key, ciphertext

# ORIENTATE THE CIPHERTEXT SO IT MATCHES OUR ORIENTATIONS VALUES.
# EX - IF A CUBE FACE VALUE OF INDEXES 0, 0, 0 ARE 6A
# THIS WILL BE THE FIRST VALUE OF THE CIPHERTEXT
def ciphertext_altering(orientation, ciphertext, faces):
    new_ciphertext = ""
    for i, v in enumerate(orientation):
        index = math.floor(int(v) / 16)
        column = math.floor((int(v) - (16 * index))) % 4
        row = math.floor((int(v) - (16 * index)) / 4) 
        new_ciphertext = new_ciphertext + faces[index][column][row]
    ciphertext = new_ciphertext
    return ciphertext

# HEX THE ROT_KEY WITH OUR ORIGINAL KEY TO MAKE THE ROT_CIP_KEY
def rot_cipher_key(r, k):
    k = (k * (len(r)//len(k)+ 1))[:len(r)]

    r_hexed = r.encode('utf-8').hex()
    k_hexed = k.encode('utf-8').hex()

    r_hexed_splitter = [r_hexed[i:i+2] for i in range(0, len(r_hexed), 2)]
    k_hexed_splitter = [k_hexed[i:i+2] for i in range(0, len(k_hexed), 2)]

    new_key = ""
    for index, value in enumerate(r_hexed_splitter):
        hexed = hex(int(r_hexed_splitter[index], 16) ^ int(k_hexed_splitter[index], 16))[2:]
        if len(hexed) == 1:
            hexed = "0" + hexed
        new_key = new_key + hexed

    return new_key

# GET OUR ROT_KEY BY XORING OUR ROT_CIP_KEY WITH OUR ORIGINAL KEY
def rot_from_rck_c(rck, c):
    uncovered_rot_key = ""
    # Get half of the hexed key length
    rck_len = round(len(rck)/2)

    #extend cipher key to half of length of hexed key
    c = (c * (rck_len//len(c)+ 1))[:rck_len]
    
    # Both keys will be same length after this hex
    # We will also split the 
    c = c.encode('utf-8').hex()

    # Lets split each key so we get hexs
    rck_hexed_splitter = [rck[i:i+2] for i in range(0, len(rck), 2)]
    c_hexed_splitter = [c[i:i+2] for i in range(0, len(c), 2)]

    # XOR the values of both the rck and Cipher key to get the rot key
    for index, value in enumerate(rck_hexed_splitter):
        rot_hex = hex(int(rck_hexed_splitter[index], 16) ^ int(c_hexed_splitter[index], 16))[2:]
        uncovered_rot_key = uncovered_rot_key + rot_hex
    
    # Decode the hex value back into normal text to uncover our ROT key
    uncovered_rot_key = bytes.fromhex(uncovered_rot_key).decode('utf-8')

    #print("UNCOVERED ROT KEY")
    #print(uncovered_rot_key)
    return uncovered_rot_key

# BREAKDOWN THE ROT_KEY BY THE MOVEMENT AND THE ORIENTATION VALUE.
# THIS WILL MAKE IT EASIER TO DO THE OPPOSITE CUBE MOVEMENT AND PLACE THE CORRECT CIPHERTEXT VALUE ONTO THE CORRECT CUBE FACE.
def get_move_pos(movements, position, rot_key):
    info = ""
    movements, position = [], []
    i = 0
    while i < len(rot_key):
        if str(rot_key[i]).isdigit():
            if str(rot_key[i - 1]).isalpha(): # Since movements end in a number. We need to check if the last index was a character. If so its a movement
                movements.append(info + str(rot_key[i]))
                info = ""
                i = i + 1
            try:
                if str(rot_key[i + 1]).isalpha(): # Check if the next string is a character, if not a position is being extracted
                    position.append(info + str(rot_key[i]))
                    info = ""
                    i = i + 1
            except IndexError: # If we are on the final index we add the position since it is the last one in the roation key
                position.append(info + str(rot_key[i]))
                info = ""
                i = i + 1 # Adding this will end the loop since the while statement isnt true
            else: # If none of the above statements are true, we keep adding to the string
                info = info + str(rot_key[i]) 
                i = i + 1
        else: # If none of the above statements are true, we keep adding to the string
            info = info + str(rot_key[i])
            i = i + 1
    return movements, position

# ASSIGN THE CIPHERTEXT TO THE CUBE FACES.
def assign_ciphertext_to_cube(up_face, down_face, left_face, front_face, right_face, back_face, position, ciphertext):
    faces = [up_face, down_face, left_face, front_face, right_face, back_face]
    ciphertext_splitter = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    for i, v in enumerate(position):
        index = math.floor(int(v) / 16)
        column = math.floor((int(v) - (16 * index))) % 4
        row = math.floor((int(v) - (16 * index)) / 4) 
        faces[index][column][row] = ciphertext_splitter[i]
    print("Ciphertext before placing onto cube")
    print(f"{ciphertext}\n")
    return up_face, down_face, left_face, front_face, right_face, back_face

# USING THE MOVEMENTS STORED IN THE ROT_KEY, WE DO THE OPPOSITE MOVEMENT TO DESCRAMBLE THE KEY
# WE THEN FIX THE CIPHERTEXT SO IT MATCHES WHAT IT LOOKS LIKE ON THE CUBE AFTER THE DESCRAMBLE
def key_cube_scramble(up_face, down_face, left_face, front_face, right_face, back_face, movements_array):
    j = 0
    for i, v in enumerate(movements_array):
        j = 0
        while j < 96:
            if v[0:3] == str(movements.movements[j][0]):
                if v[1] == "C":
                    #print(v, str(movements.movements[j-1][0]))
                    up_face, down_face, left_face, front_face, right_face, back_face = movements.movements[j-1][1](up_face, down_face, left_face, front_face, right_face, back_face)
                    j = 96
                elif v[1] == "A":
                    #print(v, str(movements.movements[j+1][0]))
                    up_face, down_face, left_face, front_face, right_face, back_face = movements.movements[j+1][1](up_face, down_face, left_face, front_face, right_face, back_face)
                    j = 96
            elif v[0:4] == str(movements.movements[j][0]):
                if v[2] == "C":
                    #print(v, str(movements.movements[j-1][0]))
                    up_face, down_face, left_face, front_face, right_face, back_face = movements.movements[j-1][1](up_face, down_face, left_face, front_face, right_face, back_face)
                    j = 96
                elif v[2] == "A":
                    #print(v, str(movements.movements[j+1][0]))
                    up_face, down_face, left_face, front_face, right_face, back_face = movements.movements[j+1][1](up_face, down_face, left_face, front_face, right_face, back_face)
                    j = 96
            else:
                j += 1
    # CHANGE THE POSTION OF CHARACTERS TO MAKE ORIGINAL CIPHERTEXT BEFORE CUBE MOVEMENTS HAPPENED
    faces = [up_face, down_face, left_face, front_face, right_face, back_face]
    ciphertext_altered = ""
    for a in range(0, 6):
        for b in range(0, 4):
            for c in range(0, 4):
                ciphertext_altered = ciphertext_altered + faces[a][b][c]

    print("4x4 Rubiks Cube after descrambling")
    print("Up Face")
    print(f"{up_face} \n")
    print("Down Face")
    print(f"{down_face} \n")
    print("Left Face")
    print(f"{left_face} \n")
    print("Front Face")
    print(f"{front_face} \n")
    print("Right Face")
    print(f"{right_face} \n")
    print("Back Face")
    print(f"{back_face} \n")

    print("Ciphertext after cube is descrambled")
    print(ciphertext_altered)
    print("")
    return up_face, down_face, left_face, front_face, right_face, back_face, ciphertext_altered

# THE SAME AS THE FACE_OPERATION FUNCTION EXCEPT WE DO THE OPPOSITE TO GET OUR ORIGINAL PLAINTEXT
def inv_aes_operation(ciphertext, keys_array):
    plaintext_array = []
    ciphertext_splitter = []

    # Reverse the key_scedhule results 
    keys_array.reverse()

    # Split and reverse the ciphertext so we can get the original plaintext
    temp_ciphertext_splitter = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    ciphertext_splitter = np.array_split(temp_ciphertext_splitter, 96 / len(keys_array[-1]))
    
    for index, value in enumerate(keys_array):
        if index == 0:
            round_result = xor(ciphertext_splitter[-1], value)
            ciphertext_splitter.clear()
            round_result = inv_shift_rows(round_result)
            round_result = sboxes.decrypt_sbox(round_result)
            plaintext_array.append(round_result)
        elif index == len(keys_array) - 1:
            plaintext_hexed = "".join(str(x) for x in xor(plaintext_array[-1], value))
            plaintext_hexed = bytes.fromhex(plaintext_hexed).decode('utf-8')
        else:
            round_result = xor(plaintext_array[index-1], value)
            round_result = mix_columns_tables.mix_column_decryption(round_result)
            round_result = inv_shift_rows(round_result)
            round_result = sboxes.decrypt_sbox(round_result)
            plaintext_array.append(round_result)
    return plaintext_hexed  

# KEY SCEHDILE SUB FUNCTION
# WE MOVE ALL ELEMENTS ONE UPWARDS (IN THE CODES EXECUTIION ITS ONE TO THE LEFT)
def ks_rotword(last_column):
    last_column = np.roll(last_column, -1)
    return last_column

# WE XOR THE FIRST COLUMN OF THE CUBE FACE BY THE LAST (WILL BE EITHER 4, 6 OR 8 AHEAD DEPENDING ON THE KEY SIZE)
# WE THEN XOR THIS VALUE WITH OUR RCON TABLE DEPENDING ON THE ROUND
def xor_with_rcon(first_column, last_column, iteration):
    new_column = []
    for i, v in enumerate(first_column):
        first_xor_last = hex(int(first_column[i], 16) ^ int(last_column[i], 16))[2:]
        first_xor_last_xor_rcon = hex(int(first_xor_last, 16) ^ int(str(required_tables.rcon_table[iteration][i]), 16))[2:]
        if len(first_xor_last_xor_rcon) == 1:
            first_xor_last_xor_rcon = "0" + first_xor_last_xor_rcon
        new_column.append(first_xor_last_xor_rcon)
    return new_column

# WE XOR THE FIRST COLUMN OF THE CUBE FACE BY THE LAST (WILL BE EITHER 4, 6 OR 8 AHEAD DEPENDING ON THE KEY SIZE)
def xor(first_column, last_column):
    new_column = []
    for i, v in enumerate(first_column):
        first_xor_last = hex(int(first_column[i], 16) ^ int(last_column[i], 16))[2:]
        if len(first_xor_last) == 1:
            first_xor_last = "0" + first_xor_last
        new_column.append(first_xor_last)
    return new_column

# THIS VERSION XOR CUBE VALUES ONE AT A TIME RATHER THEN THE PREVIOUS FUNCTIONS WHICH WORK BASED ON ARRAYS
def non_array_xor(value1, value2):
    first_xor_last = hex(int(value1, 16) ^ int(value2, 16))[2:]
    if len(first_xor_last) == 1:
        first_xor_last = "0" + first_xor_last
    return first_xor_last

# OUR 4X4 TABLE IS SHIFTED BY A CERTAIN AMOUNT BASED ON 
# 1. THE KEY SIZE
# 2. WHICH ROW WE ARE ON IN THE ITERATION
def shift_rows(round_result):
    if len(round_result) == 16:
        round_result_rows = np.array_split(round_result, 4)
        for index, value in enumerate(round_result_rows):
            round_result_rows[index] = np.roll(round_result_rows[index], -index)
        round_result = []
        i, j = 0, 0
        while i < 4:
            while j < 4:
                round_result.append(round_result_rows[i][j])
                j += 1
            j = 0
            i += 1
    elif len(round_result) == 24:
        round_result_rows = np.array_split(round_result, 4)
        for index, value in enumerate(round_result_rows):
            round_result_rows[index] = np.roll(round_result_rows[index], -index-2)
        round_result = []
        i, j = 0, 0
        while i < 4:
            while j < 6:
                round_result.append(round_result_rows[i][j])
                j += 1
            j = 0
            i += 1
    elif len(round_result) == 32:
        round_result_rows = np.array_split(round_result, 4)
        for index, value in enumerate(round_result_rows):
            round_result_rows[index] = np.roll(round_result_rows[index], -index-4)
        round_result = []
        i, j = 0, 0
        while i < 4:
            while j < 8:
                round_result.append(round_result_rows[i][j])
                j += 1
            j = 0
            i += 1
    return round_result

# OUR 4X4 TABLE IS SHIFTED BY A CERTAIN AMOUNT BASED ON 
# 1. THE KEY SIZE
# 2. WHICH ROW WE ARE ON IN THE ITERATION
# THESE VALUES ARE OPPOSITE OF THE shift_rows FUNCTION
def inv_shift_rows(round_result):
    if len(round_result) == 16:
        round_result_rows = np.array_split(round_result, 4)
        for index, value in enumerate(round_result_rows):
            round_result_rows[index] = np.roll(round_result_rows[index], index)
        round_result = []
        i, j = 0, 0
        while i < 4:
            while j < 4:
                round_result.append(round_result_rows[i][j])
                j += 1
            j = 0
            i += 1
    elif len(round_result) == 24:
        round_result_rows = np.array_split(round_result, 4)
        for index, value in enumerate(round_result_rows):
            round_result_rows[index] = np.roll(round_result_rows[index], index+2)
        round_result = []
        i, j = 0, 0
        while i < 4:
            while j < 6:
                round_result.append(round_result_rows[i][j])
                j += 1
            j = 0
            i += 1
    elif len(round_result) == 32:
        round_result_rows = np.array_split(round_result, 4)
        for index, value in enumerate(round_result_rows):
            round_result_rows[index] = np.roll(round_result_rows[index], index+4)
        round_result = []
        i, j = 0, 0
        while i < 4:
            while j < 8:
                round_result.append(round_result_rows[i][j])
                j += 1
            j = 0
            i += 1
    return round_result

