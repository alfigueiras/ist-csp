from utils import *
from keygen import *
from enc_dec import *

for i in range(1):
    
    # For just encryption/decryption w/out homomorphic operations, larger errors are ok
    keys = gswKeys(15,4, 100)

    # define params:
    N, q, l, m, t, sk, A = keys.N, keys.q, keys.l, keys.m, keys.t, keys.sk, keys.pk
    
    print('\nModulus q =', q, '\n')
    
    # Generate random integer mod q, encrypt and decrypt:
    num = np.random.randint(0,q)
    print('num = ', num)
    encnum = encInt(N,q,l,m, A, num)
    decnum = decInt(l, q, sk, encnum)
    print('Decryption of num = ', decnum, '\n')
    
    
    # Must generate smaller errors for homomorphic operations:
    keys = gswKeys(15,4, 1)

    # define params:
    N, q, l, m, t, sk, A = keys.N, keys.q, keys.l, keys.m, keys.t, keys.sk, keys.pk
    
    
    # Generate and encrypt 2 random bits:
    plainbit1 = np.random.randint(0,2)
    cipherbit1 = enc(N,q,l,m,A,plainbit1)

    plainbit2 = np.random.randint(0,2)
    cipherbit2 = enc(N,q,l,m,A,plainbit2)
    
    # Store decryption of both bits for later comparison:
    decbit1 = dec(l,q,sk,cipherbit1)
    decbit2 = dec(l,q,sk,cipherbit2)
    
    # Perform homomorphic addition/multiplication of both bits and decrypt
    decripted_sum = dec(l,q,sk,AddCipher(cipherbit1, cipherbit2, l))
    decripted_mult = dec(l,q,sk,MultCipher(cipherbit1, cipherbit2, l))

    print('Decripted bit 1 = ', decbit1, '(bit 1 = ', plainbit1, ')')
    print('Decripted bit 2 = ', decbit2, '(bit 2 = ', plainbit2, ')\n')
    print('Decripted sum = ', decripted_sum, '(actual sum = ', (plainbit1 + plainbit2) % 2, ')')
    print('Decripted product = ', decripted_mult, '(actual product = ', (plainbit1 * plainbit2) % 2, ')\n')
