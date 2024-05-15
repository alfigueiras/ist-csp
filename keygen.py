from math import floor, log2
from utils import *
import numpy as np 
import random as rand

class gswKeys:
    def __init__(self, lbda, L):
        self.n, self.k, self.q, self.l, self.m, self.N, self.error_dist = self.setup(lbda, L)
        
        self.t,self.sk,self.v=self.secret_key_gen()

        self.pk=self.public_key_gen()


    def setup(self, lbda, L):
        #q with k bits
        #k = O(L log n)
        #n quasi-linear on lambda
        n=lbda
        k=int(L*log2(n))
        q=2**k #generate q between 2**(k-something) and 2**k
        l=floor(log2(q))+1
        m=n*l
        N=(n+1)*l
        error_distr = lambda : floor(np.random.standard_normal())#*q/(8*(N+1)**L))
        return n,k,q,l,m,N,error_distr
    
    def public_key_gen(self):
        B=np.random.randint(0, self.q, (self.m, self.n), dtype=np.int64)
        errors=np.array([self.error_dist() for i in range(self.m)]).T
        b=np.matmul(B,self.t)+errors
        b=b.reshape((-1,1))
        pk=np.hstack((b, B))
        return pk

    def secret_key_gen(self):
        t = [-(rand.randint(0,self.q)) for j in range(self.n)]
        sk = [1]+t
        return t,sk,Powersof2(sk, self.l)
    
a=gswKeys(13,5)




