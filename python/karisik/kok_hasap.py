# -*- coding: cp1254 -*-
from math import*
def kok_hesapLa(a,b,c):
    
    if b**2-(4*a*c)<0:
        print " denklemin ger�el k�k� bulunmamaktad�r."
    else:
        w1=(-b+(b**2-4*a*c)**0.5)/(2*a)
        print "Denklemin birinci k�k�:",w1
        w2=(-b-(b**2-4*a*c)**0.5)/(2*a)
        print "Denklemin ikinci k�k�:",w2
