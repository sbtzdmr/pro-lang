# -*- coding: cp1254 -*-
def ters_fark(sayi):
    a=sayi
    d=""
    while sayi:
        basamak=sayi%10
        sayi=sayi/10
        d+=str(basamak)
    print "say�n�n tersi:",d,"aradaki fark:",a-int(d)
    
