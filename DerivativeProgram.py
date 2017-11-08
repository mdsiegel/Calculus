#Matthew Siegel
#DerivitveProgram.py


precision = 0.00001
terms = int(input('How many terms do you have?'))
data = {}
for i in range(1,terms+1):
    data['coefficient',i] = float(input('Enter the coefficient'))
    data['exponent',i] = float(input('Enter the exponent'))

lowerRange = float(input('Enter the lower limit'))
upperRange = float(input('Enter the upper limit'))
step = float(input('Enter the step'))
lowerRangeValue = 0
#Getting the y-values of the original function
def getValue(x):
    y = 0
    for i in range(1,terms+1):
        y += (data['coefficient',i])*((x)**data['exponent',i])
    return y
u = lowerRange
while u<=upperRange:
    data['y-value',u] = getValue(u)
    u+= step
    
#Getting the values for the first derivitive
def getFirstDerivite(x):
    firstDerivitive = (getValue(x+precision)-getValue(x-precision))/(2*precision)
    return firstDerivitive

o = lowerRange
while o<=upperRange:
    data['1Der',o] = getFirstDerivite(o)
    o+= step
#Getting the values for second derivitive
def getSecondDerivitive(x):
    secondDerivitive = (getFirstDerivite(x+precision)-getFirstDerivite(x-precision))/(2*precision)
    return secondDerivitive

q = lowerRange
while q<=upperRange:
    data['2Der',q] = getSecondDerivitive(q)
    q+= step
    
def getExtrema():
    b = lowerRange
    while b<=upperRange:
        if getFirstDerivite(b) > 0 and getFirstDerivite(b+step)<0:
            print('There is an upper extrema at',b)
        if getFirstDerivite(b) < 0 and getFirstDerivite(b+step)>0:
            print('There is a lower extrema at',b)
        b+=step
getExtrema()




