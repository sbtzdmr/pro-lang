# -*- coding: cp1254 -*-
def bmi_hesapla(agirlik,boy):
    bmi=agirlik/boy**2
    if bmi<18.5:
        print ("zay�fs�n�z")
    elif bmi>=18.5 and bmi<25:
        print ("normalsiniz")
    else:
        print ("�i�mans�n�z")
