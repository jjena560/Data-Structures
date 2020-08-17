class Tay():
    s = 1
    def taylor(self, x, n):
        if n==0:
            return self.s
        self.s = 1+self.s*x/n
        self.taylor(self,x, n-1)
        
obj = Tay()
print(obj.taylor(4,2))