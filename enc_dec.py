from math import log2
from utils import *
import numpy as np 

#Encodes message "mu" in {0,1}
def enc(N, q, l, m, A, mu):
    R = np.random.randint(0, 2, (N, m), dtype=np.int64)
    C = matrixFlatten(mu * np.identity(N) + matrixBitDecomp(R @ A, l), l) % q
    return C

#Decodes ciphertext C from message "mu" in {0,1}
def dec(l, q, sk, C):
    #since q=2^k = 2^(l-1), v_i = q/2 = 2^(l-2).
    #So, we want row l-2 of C
    v = Powersof2(sk, l) % q
    return int(np.rint(C[l-2]@(v))%q / v[l-2])

# Encodes number "mu" mod q
def encInt(N, q, l, m, A, mu):
    res = []
    binary = bin(mu)[2:]
    for bit in binary[::-1]:
        res += [enc(N, q, l, m, A, int(bit))]
    return res

#Decodes ciphertext C from message "mu" mod q
def decInt(l, q, sk, Clist):
    res = 0
    i = 0
    for C in Clist:
        res += dec(l, q, sk, C)*(2**i)
        i+=1
    return res

def MPDec(l,q,sk,C):
    v = Powersof2(sk, l) % q
    bitlist = [0 for i in range(l)]
    i = l-3
    bitlist[0] = int(np.rint(C[l-2]@(v))%q / v[l-2])
    for j in range(1,l):
        s = sum([bitlist[k]*(2**k)*v[i] for k in range(j)])
        bitlist[j] = int(np.rint( ((C[i]@(v)) - s)%q / v[l-2]) )
        i-=1
    res = 0
    for j in range(l):
        res += bitlist[j]*(2**j)
    return res % q