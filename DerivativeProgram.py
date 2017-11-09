#Matthew Siegel
#DerivitveProgram.py


print(.001//1)
localMaxes = 0
localMins = 0
precision = 0.000001
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

    
#Getting the values for the first derivitive
def getFirstDerivite(x):
    firstDerivitive = (getValue(x+precision)-getValue(x-precision))/(2*precision)
    return firstDerivitive


#Getting the values for second derivitive
def getSecondDerivitive(x):
    secondDerivitive = (getFirstDerivite(x+precision)-getFirstDerivite(x-precision))/(2*precision)
    return secondDerivitive




def getExtrema():
    b = lowerRange
    while b<=upperRange:
        if getFirstDerivite(b) > 0 and getFirstDerivite(b+step)<0:
            print('There is an upper extrema at',b)
            localMaxes +=1
            data['upperMax', localMaxes] = b
        if getFirstDerivite(b) < 0 and getFirstDerivite(b+step)>0:
            print('There is a lower extrema at',b)
            localMins +=1
            data['lowerMin', localMins] = b

            
        b+=step
getExtrema()

def increasing():
    if getFirstDerivite(lowerRange) > 0:
        if upperMaxes > 0:
            print('Increasing',lowerRange,'to', data['upperMax',1])
    if getFirstDerivite(lowerRange) < 0:
        if lowerMins > 0:
            print('Decreasing',lowerRange,'to', data['lowerMin',1])
increasing()

def getPOI():
    b = lowerRange
    while b<=upperRange:
        if getSecondDerivitive(b) > 0 and getSecondDerivitive(b+step)<0:
            print('There is a POI at',b)
        if getSecondDerivitive(b) < 0 and getSecondDerivitive(b+step)>0:
            print('There is a POI at', b)
            
            
        b+=step
getPOI()







