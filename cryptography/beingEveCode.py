#### Diffie Helman 

powers_list=[]
multiples_list=[]
g= 17
p=61
## A=46 and B=5
def find_exponent(g,p,dif):
    for power in range(1,10000000000000000):
        if (g**power - dif) % p == 0:
            print(str(power) + ' is the exponent you seek for ' + str(dif))
            return power

a = find_exponent(g,p,46)
b = find_exponent(g,p,5)
key_k = (g**(a*b)%p)
print("The shared secret is: " + str(key_k))


#### RSA section
e = 31
n = 4661
prime_factors=[59,79]
d=0
message_encrypted = [2677, 4254, 1152, 4645, 4227, 1583, 2252, 426, 3492, \
    4227, 3889, 1789, 4254, 1704, 1301, 4227, 1420, 1789, 1821, 1466, 4227, \
    2252, 3303, 1420, 2234, 4227, 4227, 1789, 1420, 1420, 4402, 1466, 4070, 3278,\
    3278, 414, 414, 414, 2234, 1466, 1704, 1789, 2955, 4254, 1821, 4254, 4645, \
    2234, 1704, 2252, 3282, 3278, 426, 2991, 2252, 1604, 3278, 1152, 4645, 1704, \
    1789, 1821, 4484, 4254, 1466, 3278, 1512, 3602, 1221, 1872, 3278, 1221, 1512, \
    3278, 4254, 1435, 3282, 1152, 1821, 2991, 1945, 1420, 4645, 1152, 1704, 1301, \
    1821, 2955, 1604, 1945, 1221, 2234, 1789, 1420, 3282, 2991, 4227, 4410, 1821, \
    1301, 4254, 1466, 3454, 4227, 4410, 2252, 3303, 4645, 4227, 3815, 4645, 1821, \
    4254, 2955, 2566, 3492, 4227, 3563, 2991, 1821, 1704, 4254]
for d_temp in range(1,1000000):
    if (e * d_temp) % ((58) * (78)) == 1:
        d = d_temp
        break

message_decrypted=""

for number in message_encrypted:
    decrypted_number = ((number ** d) % n)
    message_decrypted+= chr(decrypted_number)

print(str(d)+" is the value for d")
print(message_decrypted)

