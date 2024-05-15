import numpy as np 
import math 
import random as rand

def bitDecomp(a: np.array, l: int):
    """
    Bit Decomposition for a single array with values from Z_q
    """
    bit_decomp=[]
    for a_i in a:
        binary_a_i=[]
        for k in range(l):
            binary_a_i.append(a_i%2)
            a_i//=2
        bit_decomp+=binary_a_i
    return bit_decomp

def matrixBitDecomp(A: np.array, l:int):
    """
    Matrix bit decomposition by applying bit decomposition to each matrix line, with values from Z_q
    """
    bit_decomp_A=[]
    for line in A:
        new_line=bitDecomp(line, l)
        bit_decomp_A.append(new_line)
    return np.array(bit_decomp_A)

def invBitDecomp(a, l):
    k = len(a)//l
    res = [0 for n in range(k)]
    for i in range(k):
        ai = a[l*i:l*i+l]
        aux = 0
        for j in range(l):
            aux += (2**j) * ai[j]
        res[i] = aux
    return res

def Powersof2(b, l): #b has length k, l = floor(log2(q)) + 1
    k = len(b)
    res = [0 for x in range(k*l)]
    print(res)
    for i in range(k):
        res[i*l:i*l+l] = [(2**j)*b[i] for j in range(l)]
    return res
