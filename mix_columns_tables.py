import numpy as np

# MATRIX VALUES FOR ENCRYPTION
encryption_matrix = [
    ["02", "03", "01", "01"],
    ["01", "02", "03", "01"],
    ["01", "01", "02", "03"],
    ["03", "01", "01", "02"],
]

# MATRIX VALUES FOR DECRYPTION
decryption_matrix = [
    ["0e", "0b", "0d", "09"],
    ["09", "0e", "0b", "0d"],
    ["0d", "09", "0e", "0b"],
    ["0b", "0d", "09", "0e"]
]

# TABLE OF RESULTS BASED OFF OF OUR e_lookup FUNCTION.
# THE VALUE NEEDED FOR THIS FUNCTION IS FOUND FROM OUR l_lookup FUNCTION
e_table = [
    ['--', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'xa', 'xb', 'xc', 'xd', 'xe', 'xf'],
    ['0x', '01', '03', '05', '0f', '11', '33', '55', 'ff', '1a', '2e', '72', '96', 'a1', 'f8', '13', '35'],
    ['1x', '5f', 'e1', '38', '48', 'd8', '73', '95', 'a4', 'f7', '02', '06', '0a', '1e', '22', '66', 'aa'],
    ['2x', 'e5', '34', '5c', 'e4', '37', '59', 'eb', '26', '6a', 'be', 'd9', '70', '90', 'ab', 'e6', '31'],
    ['3x', '53', 'f5', '04', '0c', '14', '3c', '44', 'cc', '4f', 'd1', '68', 'b8', 'd3', '6e', 'b2', 'cd'],
    ['4x', '4c', 'd4', '67', 'a9', 'e0', '3b', '4d', 'd7', '62', 'a6', 'f1', '08', '18', '28', '78', '88'],
    ['5x', '83', '9e', 'b9', 'd0', '6b', 'bd', 'dc', '7f', '81', '98', 'b3', 'ce', '49', 'db', '76', '9a'],
    ['6x', 'b5', 'c4', '57', 'f9', '10', '30', '50', 'f0', '0b', '1d', '27', '69', 'bb', 'd6', '61', 'a3'],
    ['7x', 'fe', '19', '2b', '7d', '87', '92', 'ad', 'ec', '2f', '71', '93', 'ae', 'e9', '20', '60', 'a0'],
    ['8x', 'fb', '16', '3a', '4e', 'd2', '6d', 'b7', 'c2', '5d', 'e7', '32', '56', 'fa', '15', '3f', '41'],
    ['9x', 'c3', '5e', 'e2', '3d', '47', 'c9', '40', 'c0', '5b', 'ed', '2c', '74', '9c', 'bf', 'da', '75'],
    ['ax', '9f', 'ba', 'd5', '64', 'ac', 'ef', '2a', '7e', '82', '9d', 'bc', 'df', '7a', '8e', '89', '80'],
    ['bx', '9b', 'b6', 'c1', '58', 'e8', '23', '65', 'af', 'ea', '25', '6f', 'b1', 'c8', '43', 'c5', '54'],
    ['cx', 'fc', '1f', '21', '63', 'a5', 'f4', '07', '09', '1b', '2d', '77', '99', 'b0', 'cb', '46', 'ca'],
    ['dx', '45', 'cf', '4a', 'de', '79', '8b', '86', '91', 'a8', 'e3', '3e', '42', 'c6', '51', 'f3', '0e'],
    ['ex', '12', '36', '5a', 'ee', '29', '7b', '8d', '8c', '8f', '8a', '85', '94', 'a7', 'f2', '0d', '17'],
    ['fx', '39', '4b', 'dd', '7c', '84', '97', 'a2', 'fd', '1c', '24', '6c', 'b4', 'c7', '52', 'f6', '01']
]

# TABLE OF RESULTS BASED OFF OF OUR l_lookup FUNCTION.
l_table = [
    ['--', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'xa', 'xb', 'xc', 'xd', 'xe', 'xf'],
    ['0x', '  ', '00', '19', '01', '32', '02', '1a', 'c6', '4b', 'c7', '1b', '68', '33', 'ee', 'df', '03'],
    ['1x', '64', '04', 'e0', '0e', '34', '8d', '81', 'ef', '4c', '71', '08', 'c8', 'f8', '69', '1c', 'c1'],
    ['2x', '7d', 'c2', '1d', 'b5', 'f9', 'b9', '27', '6a', '4d', 'e4', 'a6', '72', '9a', 'c9', '09', '78'],
    ['3x', '65', '2f', '8a', '05', '21', '0f', 'e1', '24', '12', 'f0', '82', '45', '35', '93', 'da', '8e'],
    ['4x', '96', '8f', 'db', 'bd', '36', 'd0', 'ce', '94', '13', '5c', 'd2', 'f1', '40', '46', '83', '38'],
    ['5x', '66', 'dd', 'fd', '30', 'bf', '06', '8b', '62', 'b3', '25', 'e2', '98', '22', '88', '91', '10'],
    ['6x', '7e', '6e', '48', 'c3', 'a3', 'b6', '1e', '42', '3a', '6b', '28', '54', 'fa', '85', '3d', 'ba'],
    ['7x', '2b', '79', '0a', '15', '9b', '9f', '5e', 'ca', '4e', 'd4', 'ac', 'e5', 'f3', '73', 'a7', '57'],
    ['8x', 'af', '58', 'a8', '50', 'f4', 'ea', 'd6', '74', '4f', 'ae', 'e9', 'd5', 'e7', 'e6', 'ad', 'e8'],
    ['9x', '2c', 'd7', '75', '7a', 'eb', '16', '0b', 'f5', '59', 'cb', '5f', 'b0', '9c', 'a9', '51', 'a0'],
    ['ax', '7f', '0c', 'f6', '6f', '17', 'c4', '49', 'ec', 'd8', '43', '1f', '2d', 'a4', '76', '7b', 'b7'],
    ['bx', 'cc', 'bb', '3e', '5a', 'fb', '60', 'b1', '86', '3b', '52', 'a1', '6c', 'aa', '55', '29', '9d'],
    ['cx', '97', 'b2', '87', '90', '61', 'be', 'dc', 'fc', 'bc', '95', 'cf', 'cd', '37', '3f', '5b', 'd1'],
    ['dx', '53', '39', '84', '3c', '41', 'a2', '6d', '47', '14', '2a', '9e', '5d', '56', 'f2', 'd3', 'ab'],
    ['ex', '44', '11', '92', 'd9', '23', '20', '2e', '89', 'b4', '7c', 'b8', '26', '77', '99', 'e3', 'a5'],
    ['fx', '67', '4a', 'ed', 'de', 'c5', '31', 'fe', '18', '0d', '63', '8c', '80', 'c0', 'f7', '70', '07']
]

# CALCULATE OUR CURRENT 4x4 WITH THE encryption_matrix TABLE
def mix_column_encryption(round_result):
    new_results = [
        [],
        [],
        [],
        []
    ]
    round_result_rows = np.array_split(round_result, 4)
    x = 0
    #print(round_result_rows)
    while x < 8:
        try:
            round_result_rows[0][x]
        except IndexError:
            #print("END OF MIXCOLUMNS")
            temp_new_results = new_results
            new_results = []
            new_results = temp_new_results[0] + temp_new_results[1] + temp_new_results[2] + temp_new_results[3]
            return new_results
        else:
            value_1 = matrix_xor(matrix_value_check(round_result_rows[0][x], encryption_matrix[0][0]), matrix_value_check(round_result_rows[1][x], encryption_matrix[0][1]), matrix_value_check(round_result_rows[2][x], encryption_matrix[0][2]), matrix_value_check(round_result_rows[3][x], encryption_matrix[0][3]))
            value_2 = matrix_xor(matrix_value_check(round_result_rows[0][x], encryption_matrix[1][0]), matrix_value_check(round_result_rows[1][x], encryption_matrix[1][1]), matrix_value_check(round_result_rows[2][x], encryption_matrix[1][2]), matrix_value_check(round_result_rows[3][x], encryption_matrix[1][3]))
            value_3 = matrix_xor(matrix_value_check(round_result_rows[0][x], encryption_matrix[2][0]), matrix_value_check(round_result_rows[1][x], encryption_matrix[2][1]), matrix_value_check(round_result_rows[2][x], encryption_matrix[2][2]), matrix_value_check(round_result_rows[3][x], encryption_matrix[2][3]))
            value_4 = matrix_xor(matrix_value_check(round_result_rows[0][x], encryption_matrix[3][0]), matrix_value_check(round_result_rows[1][x], encryption_matrix[3][1]), matrix_value_check(round_result_rows[2][x], encryption_matrix[3][2]), matrix_value_check(round_result_rows[3][x], encryption_matrix[3][3]))
            
            new_results[0].append(value_1)
            new_results[1].append(value_2)
            new_results[2].append(value_3)
            new_results[3].append(value_4)

            x += 1
    temp_new_results = new_results
    new_results = []
    new_results = temp_new_results[0] + temp_new_results[1] + temp_new_results[2] + temp_new_results[3]
    return new_results

# CALCULATE OUR CURRENT 4x4 WITH THE decryption_matrix TABLE
def mix_column_decryption(round_result):
    new_results = [
        [],
        [],
        [],
        []
    ]
    round_result_rows = np.array_split(round_result, 4)
    x = 0
    #print(round_result_rows[0])
    while x < 8:
        try:
            round_result_rows[0][x]
        except IndexError:
            #print("END OF INV MIXCOLUMNS")
            temp_new_results = new_results
            new_results = []
            new_results = temp_new_results[0] + temp_new_results[1] + temp_new_results[2] + temp_new_results[3]
            return new_results
        else:
            value_1 = matrix_xor(matrix_value_check(round_result_rows[0][x], decryption_matrix[0][0]), matrix_value_check(round_result_rows[1][x], decryption_matrix[0][1]), matrix_value_check(round_result_rows[2][x], decryption_matrix[0][2]), matrix_value_check(round_result_rows[3][x], decryption_matrix[0][3]))
            value_2 = matrix_xor(matrix_value_check(round_result_rows[0][x], decryption_matrix[1][0]), matrix_value_check(round_result_rows[1][x], decryption_matrix[1][1]), matrix_value_check(round_result_rows[2][x], decryption_matrix[1][2]), matrix_value_check(round_result_rows[3][x], decryption_matrix[1][3]))
            value_3 = matrix_xor(matrix_value_check(round_result_rows[0][x], decryption_matrix[2][0]), matrix_value_check(round_result_rows[1][x], decryption_matrix[2][1]), matrix_value_check(round_result_rows[2][x], decryption_matrix[2][2]), matrix_value_check(round_result_rows[3][x], decryption_matrix[2][3]))
            value_4 = matrix_xor(matrix_value_check(round_result_rows[0][x], decryption_matrix[3][0]), matrix_value_check(round_result_rows[1][x], decryption_matrix[3][1]), matrix_value_check(round_result_rows[2][x], decryption_matrix[3][2]), matrix_value_check(round_result_rows[3][x], decryption_matrix[3][3]))
            
            # new_results.append(value_1)
            # new_results.append(value_2)
            # new_results.append(value_3)
            # new_results.append(value_4)
            
            new_results[0].append(value_1)
            new_results[1].append(value_2)
            new_results[2].append(value_3)
            new_results[3].append(value_4)
            #print(value_1, value_2, value_3, value_4)
            x += 1
            
    temp_new_results = new_results
    new_results = []
    new_results = temp_new_results[0] + temp_new_results[1] + temp_new_results[2] + temp_new_results[3]
    return new_results

# LOOKING AT THE CORRESPONDING VALUE IN THE l_table BASED ON THE VALUE PROVIDED
def l_lookup(hex_value):
    i, j = 0, 0
    for i in range(17):
        if hex_value[0] in l_table[i][0]:
            i = i
            break
    for j in range(17):
        if hex_value[1] in l_table[0][j]:
            j = j
            break
    hex_value = l_table[i][j]

    return hex_value

# LOOKING AT THE CORRESPONDING VALUE IN THE e_table BASED ON THE VALUE PROVIDED
def e_lookup(hex_value):
    if len(hex_value) == 1:
        hex_value = "0" + hex_value
    i, j = 0, 0
    for i in range(17):
        if hex_value[0] in e_table[i][0]:
            i = i
            break
    for j in range(17):
        if hex_value[1] in e_table[0][j]:
            j = j
            break
    hex_value = e_table[i][j]

    return hex_value

# GETTING THE FINAL VALUE FROM ADDING THE HEX VALUE WITH THE CURRENT MATRIX VALUE AND THEN LOOKING IT UP IN THE e_table
def matrix_value_check(hex_value, matrix_value):
    if hex_value == "00":
        value = hex_value
    elif matrix_value == "01":
        value = hex_value
    else:
        value = int(l_lookup(hex_value), 16) + int(l_lookup(matrix_value), 16)
        if value > 255:
            value = value - 255
        value = e_lookup(hex(value)[2:])
        if len(value) == 1:
            value = "0" + value
    return value

# XORING all values from value1 - value4
def matrix_xor(value_1, value_2, value_3, value_4):
    result = ""
    result = hex(int(value_1, 16) ^ int(value_2, 16) ^ int(value_3, 16) ^ int(value_4, 16))[2:]
    if len(result) == 1:
        result = "0" + result
    return result












