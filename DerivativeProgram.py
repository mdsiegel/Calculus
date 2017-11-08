#Matthew Siegel
#DerivitveProgram.py



terms = int(input('How many terms do you have?'))
data = {}
for i in range(1,terms+1):
    data['coefficient',i] = float(input('Enter the coefficient'))
    data['exponent',i] = float(input('Enter the exponent'))

lowerRange = float(input('Enter the lower limit'))
upperRange = float(input('Enter the upper limit'))
step = float(input('Enter the step'))
lowerRangeValue = 0
def getValue(x):
    y = 0
    for i in range(1,terms+1):
        y += (data['coefficient',i])*((x)**data['exponent',i])
    return y
u = lowerRange
while u<=upperRange:
    data['y-value',u] = getValue(u)
    u+= step
    

def getFirstDerivite(x):
    firstDerivitive = (getValue(x+0.001)-getValue(x-0.001))/(2*0.001)
    return firstDerivitive

o = lowerRange
while o<=upperRange:
    data['1Der',o] = getFirstDerivite(o)
    o+= step

def getSecondDerivitive(x):
    secondDerivitive = (getFirstDerivite(x+0.001)-getFirstDerivite(x-.001))/(2*0.001)
    return secondDerivitive
    
print(getSecondDerivitive(2))
