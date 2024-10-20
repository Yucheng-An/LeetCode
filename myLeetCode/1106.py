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
    global mixed,allTrue,allFalse
    boolValue = set()
    for i in range(2,len(subExpr)-1):
        if subExpr[i] == 't': 
            boolValue.add('t')
        elif subExpr[i] == 'f':
            boolValue.add('f')
    
    if len(boolValue) ==  0:
        return None
    elif len(boolValue) ==  2:
        mixed = True
    elif boolValue[0] == 't':
        allTrue = True
    else: 
        allFalse = True
        
    if subExpr[0] == '|':
        if mixed:
            return 't'
        elif allTrue:
            return 't'
        elif allFalse:
            return 'f'
    elif subExpr[0] == '&':
        
        
        