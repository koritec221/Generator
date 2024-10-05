import random

sogl = 'bcsqhgtrfplmnbvjzq'
glas= 'aeiuyo'
digit = '1234567890'
symbols='!@#+/+-'
for i in range (10):
    password = ''
    for i in range(random.randint(4,6)):
        password += random.choice(sogl)
        password += random.choice(glas)
        password += '-'
    for i in range(random.randint(2,4)):
        password+= random.choice(digit)
    for i in range(random.randint(1,3)):
        password += random.choice(symbols)
    print (password)
