# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:16:10 2020

@author: Alex
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:39:49 2020

@author: Alex
"""

class American:
    
    def __init__(self, u, R, N, S0, K, Type):
        self.R = R
        self.N = N
        self.S0 = S0
        self.K = K
        self.Type = Type
        
        if Type.lower()[0] == "c":
            self.Value_func = lambda x : max([x-K, 0])
            
        elif Type.lower()[0] == "p":
            self.Value_func = lambda x : max([K-x, 0])
        
        self.fill_prices(u, 1/u, N, S0)
        self.fill_values(u, 1/u, R, N, K)
        self.Option_Price = round(self.Values[0][0],2)
        
        
        
    def fill_prices(self, u, d, N, S0):
        self.Prices = []
        for i in range(0, N+1):
            self.Prices.append([])
            for j in range(0, i+1):
                self.Prices[i].append(u**(i-j)*d**j*S0)
                        
    def fill_values(self, u , d, R, N, K):
        q = (R-d)/(u-d)
        self.Values = [[]]
         
        for i in range (0, N+1):
            self.Values[0].append(self.Value_func(self.Prices[N][i]))
                                             
        for j in range(N-1,-1,-1):
            self.Values.append([])
            
            for k in range(0, j+1):
                self.Values[N-j].append( max([self.Value_func(self.Prices[j][k]) , 
                             (q*self.Values[N-1-j][k]+(1-q)*self.Values[N-1-j][k+1])/R]) )
            
        self.Values = self.Values[::-1]
    
    def output(self):
        print(f"At a strike of {self.K}$ and RFR of {self.R}, the american {self.Type} price in the {self.N} period model is {self.Option_Price}$\n")
        
       
class European:
    
    def __init__(self, u, R, N, S0, K, Type):
        self.R = R
        self.N = N
        self.S0 = S0
        self.K = K
        self.Type = Type
        
        if Type.lower()[0] == "c":
            self.Value_func = lambda x : max([x-K, 0])
            
        elif Type.lower()[0] == "p":
            self.Value_func = lambda x : max([K-x, 0])
        
        self.fill_prices(u, 1/u, N, S0)
        self.fill_values(u, 1/u, R, N, K)
        self.Option_Price = round(self.Values[0][0],2)
        
    def fill_prices(self, u, d, N, S0):
        self.Prices = []
        for i in range(0, N+1):
            self.Prices.append([])
            for j in range(0, i+1):
                self.Prices[i].append(u**(i-j)*d**j*S0)
                        
    def fill_values(self, u , d, R, N, K):
        q = (R-d)/(u-d)
        self.Values = [[]]
         
        for i in range (0, N+1):
            self.Values[0].append(self.Value_func(self.Prices[N][i]))
                                             
        for j in range(N-1,-1,-1):
            self.Values.append([])
            
            for k in range(0, j+1):
                self.Values[N-j].append( (q*self.Values[N-1-j][k]+(1-q)*self.Values[N-1-j][k+1])/R )
            
        self.Values = self.Values[::-1]

    def output(self):
        print(f"At a strike of {self.K}$ and RFR of {self.R}, the american {self.Type} price in the {self.N} period model is {self.Option_Price}$\n")
      

        
        