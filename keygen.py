from math import floor, log2
from utils import *
import numpy as np 

class gswKeys:
    def __init__(self, lbda, L):
        self.n, self.k, self.q, self.l, self.m, self.N, self.error_distr = self.setup(lbda, L)
        
        self.t,self.sk=self.secret_key_gen()

        self.pk=self.public_key_gen()

    def setup(self, lbda, L):
        #q with k bits
        #k = O(L log n)
        #n quasi-linear on lambda
        n=lbda
        k=int(L*log2(n))
        q=2**k #generate q between 2**(k-something) and 2**k
        l=int(np.floor(log2(q))+1)
        m=(n+1)*l
        N=(n+1)*l

        def error_distr(size):
            # Step 1: Generate samples from a normal distribution
            samples = np.random.normal(0, 0.5, size) 
            
            # Step 2: Compute the absolute value mod q
            modified_values = np.abs(samples) % self.q
            
            return np.rint(modified_values)
        return n,k,q,l,m,N,error_distr
    
    def public_key_gen(self):
        B=np.random.randint(0, self.q, (self.m, self.n), dtype=np.int64)
        errors=self.error_distr(size=self.m).T
        b= (B @ self.t) + errors
        b=b.reshape((-1,1))
        pk=np.hstack((b, B))
        return pk % self.q

    def secret_key_gen(self):
        t = np.random.randint(0,self.q,size=self.n, dtype=np.int64)
        sk = np.concatenate((np.array([1]), -t))
        return t,sk
