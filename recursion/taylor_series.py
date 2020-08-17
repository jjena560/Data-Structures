class Taylor:
    p=1
    f=1
    def taylor(self, x, n):
        if n==0:
            return 1

        r = self.taylor(x, n - 1)
        Taylor.p = Taylor.p * x
        Taylor.f = Taylor.f * n
        return r+(Taylor.p/Taylor.f)

obj = Taylor()
print(obj.taylor(4,2))

