### where is the iterator?

whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ\n')
f = open('dycyphered_string.txt', 'r')
string = f.read()
char_and_whitespace = ''.join(filter(whitelist.__contains__, string))
words = char_and_whitespace.split()
key = [4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100,
        30, 10, 26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 633, 27, 70, 77,
        45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]

for key_unit in key:
    print(words[key_unit][0], end ="")



    
