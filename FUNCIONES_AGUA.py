import re

def ValidaModelo(model1,model2,model3,model4,model5,model6,model7,model8):

    exreg = '\d'
    p = re.compile(exreg)
    m = p.search(model1)
    m2 = p.search(model2)
    m3 = p.search(model3)
    m4 = p.search(model4)
    m5 = p.search(model5)
    m6 = p.search(model6)
    m7 = p.search(model7)
    m8 = p.search(model8)

    if (m) and (m2) and (m3) and (m4) and (m5) and (m6) and (m7) and (m8):
        return  True
    else:
        return  False

def unafuncion (model1,model2,model3,model4):

    exreg = '\d'
    p = re.compile(exreg)
    m1 = p.search(model1)
    m2 = p.search(model2)
    m3 = p.search(model3)
    m4 = p.search(model4)


    if (m1) and (m2) and (m3) and (m4):
        return True
    else:
        return False


def segundafuncion(model5,model6,model7,model8):
    exreg = '\d'
    p = re.compile(exreg)
    m5 = p.search(model5)
    m6 = p.search(model6)
    m7 = p.search(model7)
    m8 = p.search(model8)

    if (m5) and (m6) and (m7) and (m8):
        return True
    else:
        return False