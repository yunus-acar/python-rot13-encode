import codecs
import os

with open('pass.txt') as p:
    password = ''.join(p.readlines())

deneme = codecs.encode(password, 'rot13')
p = open('key.txt', 'w')
p.write(deneme)
p.close()

print('┼čirelendiniz \n',deneme)
a = codecs.decode(deneme,'rot13')
print('┼čirelendiniz \n',a)
