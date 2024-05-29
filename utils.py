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
    return np.array(bit_decomp)

def matrixBitDecomp(A: np.array, l:int):
    """
    Matrix bit decomposition by applying bit decomposition to each matrix line, with values from Z_q
    """
    bit_decomp_A=[]
    for line in A:
        new_line=bitDecomp(line, l)
        bit_decomp_A.append(new_line)
    return np.array(bit_decomp_A)

def invBitDecomp(a: np.array, l:int):
    q = 2**(l-1)
    k = len(a)//l
    res = [0 for n in range(k)]
    for i in range(k):
        ai = a[l*i:l*i+l]
        aux = 0
        for j in range(l):
            aux += (2**j) * ai[j]
        res[i] = aux
    return np.array(res)%q

def Powersof2(b: np.array, l:int): #b has length k, l = floor(log2(q)) + 1
    k = len(b)
    res = [0 for x in range(k*l)]
    for i in range(k):
        res[i*l:i*l+l] = [(2**j)*b[i] for j in range(l)]
    return np.array(res)

def flatten(a: np.array, l:int):
    """
    Flatten operation on N-dimensional array "a"
    """
    return bitDecomp(invBitDecomp(a, l),l)

def matrixFlatten(A:np.array, l:int):
    """
    Matrix flatten by applying flatten function to each matrix line
    """
    flatten_A=[]
    for line in A:
        new_line=flatten(line, l)
        flatten_A.append(new_line)
    return np.array(flatten_A)

def MultConst(C: np.array, alpha: int, l:int):
    M_alpha=matrixFlatten(alpha*np.identity(C.shape[0]), l)
    return matrixFlatten(M_alpha@C, l)

def AddCipher(C1: np.array, C2: np.array, l:int):
    return matrixFlatten(C1+C2,l)

def MultCipher(C1: np.array, C2: np.array, l:int):
    return matrixFlatten(C1@C2,l)