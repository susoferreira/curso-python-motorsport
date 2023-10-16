
class Triangle:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        print("getter")
        return self._base
        
    @base.setter
    def base(self,n):
        print("setter")
        assert n > 0
        self._base=n
    @property
    def altura(self):
        print("getter")
        return self._altura

    @altura.setter
    def altura(self,n):
        print("setter")
        assert n > 0
        self._altura=n



    def area(self):
        return 0.5 * self.base * self.altura


triangle = Triangle(10, 5)
print(triangle.area())