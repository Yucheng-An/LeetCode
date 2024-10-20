
testStr = "|(f,f,f,t)"


def parseBoolExpr(expression):
    calculation = []
    boolValue = []
    for i in expression:
        if i == ''