import re


expr1 = r'(1+00*1)+(1+00*1)(0+10*1)*(0+10*1)'
expr2 = r'0*1(0+10*1)*'


def verifica_egalitatea(expr1, expr2):
 
    test_strings = ['0', '1', '00', '01', '10', '11', '000', '001', '010', '011', '100', '101', '110', '111']
    
    for s in test_strings:
        match1 = re.fullmatch(expr1, s)
        match2 = re.fullmatch(expr2, s)
        
        if (match1 is not None) != (match2 is not None):
            return False
    
    return True


if verifica_egalitatea(expr1, expr2):
    print("sunt egale")
else:
    print("nu sunt egale")