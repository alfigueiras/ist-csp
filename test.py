from utils import *
from keygen import *
from enc_dec import *

for i in range(100):
    a=gswKeys(15,4)

    # define params:
    N, q, l, m = a.N, a.q, a.l, a.m
    t, sk = a.t, a.sk

    A = a.pk
    
    plaintext_1 = 1
    ciphertext_1 = enc(N,q,l,m,A,plaintext_1)

    plaintext_2=1
    ciphertext_2 = enc(N,q,l,m,A,plaintext_2)

    decripted_message_1 = dec(l,q,sk,ciphertext_1)
    decripted_message_2 = dec(l,q,sk,ciphertext_2)

    decripted_sum=dec(l,q,sk,AddCipher(ciphertext_1, ciphertext_2, a.l))
    decripted_mult=dec(l,q,sk,MultCipher(ciphertext_1, ciphertext_2, a.l))

    print('decripted message 1 = ', decripted_message_1, '\n\n')
    print('decripted message 2 = ', decripted_message_2, '\n\n')
    print('decripted sum = ', decripted_sum, '\n\n')
    print('decripted mult = ', decripted_mult, '\n\n')

    

# print(decr)

# print('plaintext = ', plaintext, '\n\n')
# print('ciphertext = \n', ciphertext, '\n\n')
# print('decripted message = ', decripted_message, '\n\n')
