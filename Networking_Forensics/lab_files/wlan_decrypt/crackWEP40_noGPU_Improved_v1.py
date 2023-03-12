import itertools
import string
import hashlib


def generate_combinations():
    characters = string.ascii_lowercase
    combinations = itertools.product(characters, repeat=8)
    # For testing only
    # combinations = ["aaaaaaaa", "cgwpkexz", "cgwpkexa", "cgwpkexa", "cgwpkexa", "cgwpkexa"]
    return combinations


def check_xor_sum(combination):
    if ord(combination[0]) ^ ord(
        combination[3]) ^ ord(combination[6])  != 0x6b :
        return False
    if ord(combination[1]) ^ ord(
        combination[4]) ^ ord(combination[7]) != 0x76:
        return False
    if ord(combination[2]) ^ ord(combination[5]) != 0x12:
        return False
    return True


def insert_letters(valid_combination):
    new_combinations = []
    characters = 'abcdefghijklmnopqrstuvwxyz'
    for x in characters:
        for y in characters:
            new_combination = tuple(list(valid_combination[:3]) + [x] +
                                    list(valid_combination[3:6]) + [y] +
                                    list(valid_combination[6:]))
            new_combinations.append(new_combination)
    return new_combinations

def check_sha1_hash(combination):
    combination_str = ''.join(combination)
    sha1_hash = hashlib.sha1(combination_str.encode('utf-8'))
    return sha1_hash.hexdigest().startswith('ff7b948953ac')


cracked= False
for combination in generate_combinations():
    # print("process: ", ''.join(combination))
    if check_xor_sum(combination): 
        print("Match xor sum: ", ''.join(combination))
        for comb_x_y in insert_letters(combination):
            if check_sha1_hash(comb_x_y):
                cracked = True
                print("Cracked: ", ''.join(comb_x_y))
                break
        if cracked:
            break

