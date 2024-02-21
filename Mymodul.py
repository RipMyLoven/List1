#def Summa(arv1:int,arv2:int,arv3=0)->int:
#    """ Funktsioon tagastab kolme arvu summa
#        Summa(arv1,arv2,arv3)

#    :param int arv1: Arv1 sisestab kasutaja
#    :param int arv2: Arv2 sisestab kasutaja
#    :param int arv3: Vaikimisi arv3 võrdub nulliga
#    :rtype: int
#    """
#    s=arv1+arv2+arv3 
#    return s

#def IntKontroll(x):
#    try:
#        x = int(x)
#        return "int"
#    except:
#        try:
#            x = float(x)
#            return "float"
#        except:
#            return "str"

def arithmetic(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Nulliga jagamine pole võimalik"
    else:
        return "Tundmatu tegevus"

