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


