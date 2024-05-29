from utils import *
from keygen import *
from enc_dec import *

for i in range(1):
    print('\n')
    
    # For just encryption/decryption w/out homomorphic operations, larger errors are ok
    keys = gswKeys(15,4, 50)

    # define params:
    N, q, l, m, t, sk, A = keys.N, keys.q, keys.l, keys.m, keys.t, keys.sk, keys.pk
    
    print('\nModulus q =', q, '\n')
    
    # Generate random integer mod q, encrypt and decrypt:
    num = np.random.randint(0,q)
    print('num = ', num)
    encnum = encInt(N,q,l,m, A, num)
    
    decnum = decInt(l, q, sk, encnum)
    print('Decryption of num = ', decnum)
    
    mpdecnum = MPDec(l,q,sk, enc(N,q,l,m,A,num))
    print('MPDecryption of num = ', mpdecnum, '\n')
    
    
    # Must generate smaller errors for homomorphic operations:
    keys = gswKeys(15,4, 8)

    # define params:
    N, q, l, m, t, sk, A = keys.N, keys.q, keys.l, keys.m, keys.t, keys.sk, keys.pk
    
    '''
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
    '''
    
    
    # Generate and encrypt 2 random numbers mod q:
    plaintext1 = np.random.randint(0,q)
    ciphertext1 = enc(N,q,l,m,A,plaintext1)

    plaintext2 = np.random.randint(0,q)
    ciphertext2 = enc(N,q,l,m,A,plaintext2)
    
    # Store decryption of both bits for later comparison:
    dectext1 = MPDec(l,q,sk,ciphertext1)
    dectext2 = MPDec(l,q,sk,ciphertext2)
    
    # Generate random constant mod q for multiplication of ciphertext1 by constant:
    alpha = np.random.randint(0,q)
    
    # Perform homomorphic addition/multiplication of both numbers and decrypt
    decripted_sum = MPDec(l,q,sk,AddCipher(ciphertext1, ciphertext2, l))
    decripted_mult = MPDec(l,q,sk,MultCipher(ciphertext1, ciphertext2, l))
    decripted_mult_const = MPDec(l,q,sk,MultConst(ciphertext1, alpha,l))

    print('Decripted plaintext 1 = ', dectext1, '(plaintext 1 = ', plaintext1, ')')
    print('Decripted plaintext 2 = ', dectext2, '(plaintext 2 = ', plaintext2, ')\n')
    print('Decripted sum = ', decripted_sum, '(actual sum = ', (plaintext1 + plaintext2) % q, ')')
    print('Decripted product = ', decripted_mult, '(actual product = ', (plaintext1 * plaintext2) % q, ')\n')
    print('Multiplicative constant alpha = ', alpha)
    print('Number being multiplied = ', plaintext1)
    print('Decripted multiplication by alpha = ', decripted_mult_const, '(actual value = ', (alpha*plaintext1)%q, ')\n')

'''
For params (15,4):

enc/dec is fine for error variance around 50 to be safe (100 starts to fail)

homomorphic addition is fine for variance around 30 (50 starts to fail)

homomorphic multiplication really seems to need error 0 (!)

homomorphic multiplication by constant seems to need error variance around 8 (10 starts to fail sometimes)

'''