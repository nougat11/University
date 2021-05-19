import textwrap
import binascii
import datetime


# Create 16 Subkeys, each of which is 48-bits long
def get_keys48(key64: str) -> list:
    key56 = get_pc_1_permutation(key64)

    left28 = [key56[: len(key56) // 2]]
    right28 = [key56[len(key56) // 2:]]
    left_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    for i in range(len(left_shifts)):
        l_key28, r_key28 = left28[i], right28[i]
        for q in range(left_shifts[i]):
            l_key28, r_key28 = l_key28[1:] + l_key28[0], r_key28[1:] + r_key28[0]

        left28.append(l_key28)
        right28.append(r_key28)

    keys48 = list()
    for i in range(len(left28)):
        keys48.append(get_pc_2_permutation(left28[i] + right28[i]))

    return keys48[1:17]


# Encode each 64-bit block of data
def encode_text64(text64: str, keys48: list) -> str:
    text64_ip = get_ip_permutation(text64)

    left32_ip = [text64_ip[: len(text64_ip) // 2]]
    right32_ip = [text64_ip[len(text64_ip) // 2:]]

    for i in range(1, 17):
        left32_ip.append(right32_ip[-1])
        right48_e = get_e_permutation(right32_ip[-1])
        r_key48 = get_xor(right48_e, keys48[i - 1])

        r_key32 = str()
        b_keys6 = textwrap.wrap(r_key48, 6)
        for q in range(len(b_keys6)):
            s_row = int(str.encode(b_keys6[q][0] + b_keys6[q][-1]), base=2)
            s_col = int(str.encode(b_keys6[q][1:5]), base=2)
            r_key32 += get_s_convertation(q, s_row, s_col)

        p_key32 = get_p_permutation(r_key32)
        right32_ip.append(get_xor(left32_ip[i - 1], p_key32))

    return bit_to_hex(get_ip_reverse_permutation(right32_ip[-1] + left32_ip[-1]))


# Usefull Functions
def get_permutation(key: str, table: list) -> str:
    return ''.join([key[table[i] - 1] for i in range(len(table))])


def get_xor(key_a: str, key_b: str) -> str:
    return ''.join([(str(int(key_a[i]) + int(key_b[i]))) for i in range(len(key_a))]).replace('2', '0')


def bit_to_hex(key: str) -> str:
    convert_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4',
                    '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9',
                    '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
    return ''.join([convert_dict[element] for element in textwrap.wrap(key, 4)])


def hex_to_bit(key: str) -> str:
    convert_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
                    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
                    'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    return ''.join([convert_dict[element] for element in key])


def get_hex_key(text: str) -> str:
    text = textwrap.wrap(text.encode().hex(), 16)
    if len(text[0]) != 16:
        text[0] = '0' * (16 - len(text[0])) + text[0]
    return text[0]


def time_compare(str_date_a: str, str_date_b: str, str_period: str) -> bool:
    date_a = datetime.datetime.strptime(str_date_a, '%Y-%m-%d %H:%M:%S.%f')
    date_b = datetime.datetime.strptime(str_date_b, '%Y-%m-%d %H:%M:%S.%f')

    time_period = datetime.timedelta(minutes=int(str_period))

    return date_a + time_period >= date_b


# Const permutation tables
def get_pc_1_permutation(key: str) -> str:
    permut_table = [57, 49, 41, 33, 25, 17, 9,
                    1, 58, 50, 42, 34, 26, 18,
                    10, 2, 59, 51, 43, 35, 27,
                    19, 11, 3, 60, 52, 44, 36,
                    63, 55, 47, 39, 31, 23, 15,
                    7, 62, 54, 46, 38, 30, 22,
                    14, 6, 61, 53, 45, 37, 29,
                    21, 13, 5, 28, 20, 12, 4]
    return get_permutation(key, permut_table)


def get_pc_2_permutation(key: str) -> str:
    permut_table = [14, 17, 11, 24, 1, 5,
                    3, 28, 15, 6, 21, 10,
                    23, 19, 12, 4, 26, 8,
                    16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32]
    return get_permutation(key, permut_table)


def get_ip_permutation(key: str) -> str:
    permut_table = [58, 50, 42, 34, 26, 18, 10, 2,
                    60, 52, 44, 36, 28, 20, 12, 4,
                    62, 54, 46, 38, 30, 22, 14, 6,
                    64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    61, 53, 45, 37, 29, 21, 13, 5,
                    63, 55, 47, 39, 31, 23, 15, 7]
    return get_permutation(key, permut_table)


def get_e_permutation(key: str) -> str:
    permut_table = [32, 1, 2, 3, 4, 5, 4, 5,
                    6, 7, 8, 9, 8, 9, 10, 11,
                    12, 13, 12, 13, 14, 15, 16, 17,
                    16, 17, 18, 19, 20, 21, 20, 21,
                    22, 23, 24, 25, 24, 25, 26, 27,
                    28, 29, 28, 29, 30, 31, 32, 1]
    return get_permutation(key, permut_table)


def get_s_permutation(key: str) -> str:
    permut_table = [32, 1, 2, 3, 4, 5, 4, 5,
                    6, 7, 8, 9, 8, 9, 10, 11,
                    12, 13, 12, 13, 14, 15, 16, 17,
                    16, 17, 18, 19, 20, 21, 20, 21,
                    22, 23, 24, 25, 24, 25, 26, 27,
                    28, 29, 28, 29, 30, 31, 32, 1]
    return get_permutation(key, permut_table)


def get_ip_reverse_permutation(key: str) -> str:
    permut_table = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]
    return get_permutation(key, permut_table)


def get_s_convertation(iteration: int, row: int, col: int) -> str:
    permut_table = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

                    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

                    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

                    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

                    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

                    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

                    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

                    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
    convert_dict = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 5: '0101',
                    6: '0110', 7: '0111', 8: '1000', 9: '1001', 10: '1010', 11: '1011',
                    12: '1100', 13: '1101', 14: '1110', 15: '1111'}

    return convert_dict[permut_table[iteration][row][col]]


def get_p_permutation(key: str) -> str:
    permut_table = [16, 7, 20, 21,
                    29, 12, 28, 17,
                    1, 15, 23, 26,
                    5, 18, 31, 10,
                    2, 8, 24, 14,
                    32, 27, 3, 9,
                    19, 13, 30, 6,
                    22, 11, 4, 25]

    return get_permutation(key, permut_table)


# MAIN ENCODE/DECODE
def des_encode(text: str, key: str, is_hex_hey: bool):
    if not is_hex_hey:
        key = get_hex_key(key)
    keys48 = get_keys48(hex_to_bit(key))

    text = textwrap.wrap(text.encode().hex(), 16)
    if len(text[-1]) != 16:
        text[-1] = '0' * (16 - len(text[-1])) + text[-1]

    hex_list = list()
    for hex_element in text:
        hex_list.append(encode_text64(hex_to_bit(hex_element), keys48))

    return ''.join(hex_list)


def des_decode(text: str, key: str, is_hex_hey: bool):
    if not is_hex_hey:
        key = get_hex_key(key)
    keys48 = get_keys48(hex_to_bit(key))[::-1]

    text = textwrap.wrap(text, 16)

    hex_list = list()
    for hex_element in text:
        hex_list.append(encode_text64(hex_to_bit(hex_element), keys48))

    text_decode = ''
    for hex_element in hex_list:
        hex_str = textwrap.wrap(hex_element, 2)
        for hex_char in hex_str:
            text_decode += binascii.unhexlify(hex_char.encode()).decode().rstrip('\x00')

    return text_decode
