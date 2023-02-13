# Write Python code that generates all possible combinations of 8 characters, 
# with each character is a lowercase English letter and also has a function, check_xor_sum, 
# to check the XOR sum of the 0th, 3rd, 6th characters is 0x6b, the XOR sum of the 1st, 4th, 7th characters is 0x76, 
# and the XOR sum of the 2nd and 5th characters is 0x12. If check_xor_sum returns true, 
# remember these valid combinations. Then write a function to generate all combinations of two lower case characters, 
# call x and y, insert x after 3rd position and insert y after 6th position of valid combinations. 
# The resultant new combination is 10 characters long strings. 
# Also add function to check sha1 hash of the 10-character strings starts with ff7b948953ac. Print final results.

import hashlib
import itertools

def check_xor_sum(string):
    if ord(string[0]) ^ ord(string[3]) ^ ord(string[6]) == 0x6b and \
       ord(string[1]) ^ ord(string[4]) ^ ord(string[7]) == 0x76 and \
       ord(string[2]) ^ ord(string[5]) == 0x12:
        return True
    return False

def generate_8_char_combinations():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    combinations = itertools.product(characters, repeat=8)
    valid_combinations = []
    for combination in combinations:
        string = "".join(combination)
        if check_xor_sum(string):
            valid_combinations.append(string)
    # valid_combinations = ["cgwpkexz"]
    return valid_combinations

def insert_letters(valid_combinations):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    new_combinations = []
    for x in characters:
        for y in characters:
            for valid_combination in valid_combinations:
                new_combination = valid_combination[:3] + x + \
                    valid_combination[3:6] + y + valid_combination[6:]
                new_combinations.append(new_combination)
    return new_combinations

def check_sha1_hash(new_combinations):
    final_results = []
    for new_combination in new_combinations:
        sha1_hash = hashlib.sha1(new_combination.encode('utf-8')).hexdigest()
        if sha1_hash.startswith("ff7b948953ac"):
            final_results.append(new_combination)
    return final_results

def main():
    valid_combinations = generate_8_char_combinations()
    new_combinations = insert_letters(valid_combinations)
    final_results = check_sha1_hash(new_combinations)
    print("Final results:")
    for result in final_results:
        print(result)

if __name__ == '__main__':
    main()
