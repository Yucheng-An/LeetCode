
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
    boolValue = []
    for i in range(2,len(subExpr)-1):
        if subExpr[i] == 't': 
            boolValue.append('t')
        elif subExpr[i] == 'f':
            boolValue.append('f')
    allTrue = None
    all
    
    for i in boolValue:
        
    if subExpr[0]:
        
        