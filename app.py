import codecs
import os

with open('pass.txt') as p:
    password = ''.join(p.readlines())

deneme = codecs.encode(password, 'rot13')
p = open('key.txt', 'w')
p.write(deneme)
p.close()

print('şirelendiniz \n',deneme)
a = codecs.decode(deneme,'rot13')
print('şirelendiniz \n',a)
