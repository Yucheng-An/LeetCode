
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
    for i in range(2,len(subExpr)):
        
        