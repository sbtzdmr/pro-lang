# -*- coding: cp1254 -*-
import math
def daire_fonk(yari_cap):
    if yari_cap<0:
        print "yar� �ap s�f�rdan k���k olamaz."
    else:
        c=math.pi*2*yari_cap
        a=math.pi*yari_cap**2
        print "dairenin �evresi:",c
        print "dairenin alan�:",a
