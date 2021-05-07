#Password Cracking code 2
#Authors: Eric Gassel and Josiah Misplon

import hashlib
import binascii

words = [line.strip().lower() for line in open('passwordWords.txt')]
usernamePasswords = [line.strip().lower() for line in open('passwordsSalted.txt')]
f = open('passwords2.txt', 'w')
f.write('Format- username:password\n')
hashCounter=0
passwordCounter=0

for string in usernamePasswords:
    usernameAndHashedPasswordList = string.split(':', 2)
    username = usernameAndHashedPasswordList[0]
    saltAndPassword = usernameAndHashedPasswordList[1].split('$')
    salt = saltAndPassword[0]
    hashedSaltAndPassword = saltAndPassword[1]
    print(passwordCounter)
    passwordCounter+=1

    
    for password in words:
        saltedPassword = salt + password
        encodedPassword = saltedPassword.encode('utf-8')
        md5 = hashlib.md5(encodedPassword)
        hashCounter+=1
        passwordHash = md5.digest()
        passwordHashAsHex = binascii.hexlify(passwordHash)
        passwordHashAsHexString = passwordHashAsHex.decode('utf-8')
        if passwordHashAsHexString == hashedSaltAndPassword:
            f.write(username+':'+password+'\n')
            break

f.close()  

print(hashCounter)