def checkEven(No):
    if No % 2 == 0:
        return True
    else:
        return false

def CheckEvenX(No):
    return (No % 2 == 0)

Ret = CheckEvenX(12)

if(Ret == True):
    print("Its even")
else:
    print("Its odd")