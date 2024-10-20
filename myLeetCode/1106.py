from tomlkit.exceptions import MixedArrayTypesError

testStr = "|(f,f,f,t)"


def parseBoolExpr(expression):
    calculation = []
    boolValue = []
    for i in expression:
        if i == 'f' or i == 't':
            boolValue.append(i)
        elif i =='|' or i == '&':
            calculation.append(i)
    for i in boolValue:
        
def subExp(subExpr):
    boolValue = set()
    for i in range(2,len(subExpr)-1):
        if subExpr[i] == 't': 
            boolValue.add('t')
        elif subExpr[i] == 'f':
            boolValue.add('f')
    allTrue = None
    allFalse = None
    mixed= None
    
    if len(boolValue) ==  2:
        mixed = True
    else: 
        for 
    if subExpr[0]:
        
        