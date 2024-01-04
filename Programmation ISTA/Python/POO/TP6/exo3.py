class Point:
    def __init__(self,x=int(),y=int()):
        self.__abscisse=x
        self.__ordonnee=y

    @property
    def X(self):
        return self.__abscisse
    @X.setter
    def X(self,M):
        self.__abscisse=M

    @property
    def Y(self):
        return self.__ordonnee
    @Y.setter
    def Y(self,M):
        self.__ordonnee=M
    
    def Deplacer(self,nx=int(input("Entrez New Abscisse: ")),ny=int(input("Entrez New Ordonnee: "))):
        self.X=nx
        self.Y=ny
    
    def Distance(self,B):
        import math as mt
        AB=mt.sqrt(((B.X)-(self.X))**2+((B.Y)-(self.Y))**2)
        return AB


A=Point(1,2)
B=Point(3,5)

A.Deplacer()
print((A.X,A.Y))


print(A.Distance(B)) 