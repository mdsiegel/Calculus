#Matthew Siegel Frans Luttmer
#DerivitveProgram.py

from math import sin,cos, tan, acos, asin, asin
from math import exp, expm1, e
from math import log, log10, sqrt, log2


precision = 0.000001
data = {}
function = input('Enter a function')


lowerRange = float(input('Enter the lower limit'))
upperRange = float(input('Enter the upper limit'))
step = float(input('Enter the step'))
lowerRangeValue = 0
#Getting the y-values of the original function



def getValue(x):
    Locfunction = function.lower()
    y = eval(Locfunction)

    return y
def getZeros():
    l = lowerRange
    while l<=upperRange:
        if getValue(l) > 0 and getValue(l+step) < 0:
            print('There is a zero at',l)
        if getValue(l) < 0 and getValue(l+step) > 0:
            print('There is a zero at',l)
        if getValue(l) == 0:
           print('There is a zero at',l)
        l+=step
getZeros()

    
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
    localMaxes = 0
    localMins = 0
    while b<=upperRange:
        if getFirstDerivite(b) > 0 and getFirstDerivite(b+step)<0:
            print('There is an upper extrema at',b)
            localMaxes +=1
            data['upperMax', localMaxes] = b
            if localMins>0:
                print('Increasing from',data['lowerMin',localMins],'to',b)
        if getFirstDerivite(b) < 0 and getFirstDerivite(b+step)>0:
            print('There is a lower extrema at',b)
            localMins +=1
            data['lowerMin', localMins] = b
            if localMaxes>0:
                print('Decreasing from',data['upperMax',localMaxes],'to',b)
        if getFirstDerivite(b) == 0:
            if getFirstDerivite(b) > 0 and getFirstDerivite(b+step)<0:
                print('There is an upper extrema at',b)
                localMaxes +=1
                data['upperMax', localMaxes] = b
                if localMins>0:
                    print('Increasing from',data['lowerMin',localMins],'to',b)
            if getFirstDerivite(b) < 0 and getFirstDerivite(b+step)>0:
                print('There is a lower extrema at',b)
                localMins +=1
                data['lowerMin', localMins] = b
                if localMaxes>0:
                    print('Decreasing from',data['upperMax',localMaxes],'to',b)
            
            
        
            
        b+=step
    #increasing/decreasing
    if getFirstDerivite(lowerRange) > 0:
        if localMaxes > 0:
            print('Increasing',lowerRange,'to', data['upperMax',1])
        else:
            print('Increasing',lowerRange,'to', upperRange)
    if getFirstDerivite(lowerRange) < 0:
        if localMins > 0:
            print('Decreasing',lowerRange,'to', data['lowerMin',1])
        
        else:
            print('Decreasing',lowerRange,'to', upperRange)
    if getFirstDerivite(upperRange)>0:
        if localMins>0:
            print('Increasing from',data['lowerMin',localMins],'to',upperRange)
    if getFirstDerivite(upperRange)<0:
        if localMaxes>0:
            print('Decreasing from',data['upperMax',localMaxes],'to',upperRange)

getExtrema()



def getPOI():
    b = lowerRange
    POItoUp=0
    POItoDown = 0
    while b<=upperRange:
        if getSecondDerivitive(b) > 0 and getSecondDerivitive(b+step)<0:
            print('There is a POI at',b)
            POItoDown+=1
            data['POIDown', POItoDown] = b
            if POItoUp>0:
                print('Concave Up from',data['POIUp',POItoUp],'to',b)
            
            
        if getSecondDerivitive(b) < 0 and getSecondDerivitive(b+step)>0:
            print('There is a POI at', b)
            POItoUp += 1
            data['POIUp', POItoUp] = b
            if POItoDown>0:
                print('Concave Down from',data['POIDown',POItoDown],'to',b)
        if getSecondDerivitive(b) == 0:
            if getSecondDerivitive(b-step) > 0 and getSecondDerivitive(b+step)<0:
                print('There is a POI at',b)
                POItoDown+=1
                data['POIDown', POItoDown] = b
                if POItoUp>0:
                    print('Concave Up from',data['POIUp',POItoUp],'to',b)
                
            
            if getSecondDerivitive(b-step) < 0 and getSecondDerivitive(b+step)>0:
                print('There is a POI at', b)
                POItoUp += 1
                data['POIUp', POItoUp] = b
                if POItoDown>0:
                    print('Concave Down from',data['POIDown',POItoDown],'to',b)
        
            
            
            
        b+=step
    if getSecondDerivitive(lowerRange) > 0:
        if POItoDown > 0:
            print('Concave Up',lowerRange,'to', data['POIDown',1])
        else:
            print('Concave Up',lowerRange,'to', upperRange)
    if getSecondDerivitive(lowerRange) < 0:
        if POItoUp > 0:
            print('Concave Down',lowerRange,'to', data['POIUp',1])
        
        else:
            print('Concave down',lowerRange,'to', upperRange)
    if getSecondDerivitive(upperRange)>0:
        if POItoUp>0:
            print('Concave up from',data['POIUp',POItoUp],'to',upperRange)
    if getSecondDerivitive(upperRange)<0:
        if POItoDown>0:
            print('Concave down from',data['POIDown',POItoDown],'to',upperRange)

getPOI()

def meanValue():
    avg = (getValue(lowerRange)-getValue(upperRange))/(lowerRange-upperRange)
    print('The average slope is',avg)
    c = lowerRange
    while c<=upperRange:
        if round(getFirstDerivite(c),1) == round(avg,1):
            print('The average slope is equal to the tangent line slope at',c)
        c+=step
meanValue()
    







