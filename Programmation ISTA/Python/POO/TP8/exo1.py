class Point:
    __cpt=0
    #constructeur
    def __init__(self,x=float,y=float):
        Point.__cpt+=1
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
    
    def Deplacer(self,nx,ny):
        # nx=int(input("Entrez New Abscisse: "))
        # ny=int(input("Entrez New Ordonnee: "))
        self.X=nx
        self.Y=ny
    
    def Distance(self,B):
        import math as mt
        AB=mt.sqrt(((B.X)-(self.X))**2+((B.Y)-(self.Y))**2)
        return AB

    def calculermilieu(self,B):
        if isinstance(B,Point):

            xM=(self.__abscisse+B.X)/2
            yM=(self.__ordonnee+B.Y)/2
            M=Point(xM,yM)
            return M
    
    @classmethod
    def NbrPt(cls):
        return cls.__cpt
    

    #destructeur
    def __del__(self):
        Point.__cpt-=1

    # def __str__(self):
    #     return f"abscisse:{self.__abscisse}\nordonnee:{self.__ordonnee}"

class TroisPoints:
    
    #constructeur
    def __init__(self,pt1=Point(),pt2=Point(float(),float()),pt3=Point(float(),float())):
        print(pt2)
        self.__point1=pt1
        self.__point2=pt2
        self.__point3=pt3
    
    def __str__(self):
        return f"Triganle de:\nPoint A:{(self.__point1)}\nPoint B:{self.__point2}\nPoint C:{self.__point3}"
    #getters
    def Getpoint1(self):
        return self.__point1
    def Getpoint2(self):
        return self.__point2
    def Getpoint(self):
        return self.__point3
    
    #setters
    def Setpoint1(self,m):
        self.__point1=m
    def SetPoint2(self,m):
        self.__point2=m
    def Setpoint3(self,m):
        self.__point3=m
    #distances:
    
    def sontalignes(self,B,C):
        if (Point.Distance(self,B)==Point.Distance(self,C)+Point.Distance(B,C)):
            return True
        else:
            return False
    
    def estisocele(self):
        AC=self.__point1.Distance(self.__point3)
        AB=self.__point1.Distance(self.__point2)
        BC=self.__point2.Distance(self.__point3)
        if ((AC==AB+BC)):
            return print("un triangle isocèle")
        else: 
            return print("un triangle n'est pas isocèle")
    
    @staticmethod
    def Millieu2(self,B):
        return Point.calculermilieu(self,B)
    def distance2(self,B):
        return Point.Distance(self,B)