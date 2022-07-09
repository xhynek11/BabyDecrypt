import sys
#   First argument is file that will be decrypted
#   HOW TO USE: EasyDecrypt.py <FILE YOU WANT TO DECRYPT>
#   EXAMPLE: EasyDecrypt.py enc.txt


f = open(sys.argv[1], 'r')
# from hex format to bytes
byte = bytes.fromhex(f.read())
output = []
for b in byte:
    yes = True
    asci = b
    # loop that will find original ascii code
    # code used for encrypt -->  (89 * ord(char) + 26) % 256 <-- every char of original text was encrypted by this code
    while yes:
        asciC = asci - 26
        asciC = asciC / 89
        if asciC.is_integer():
            yes = False
        else:
            asci = asci + 256
    output.append(chr(int(asciC)))
print(''.join(output))
