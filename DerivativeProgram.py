#Matthew Siegel Frans Luttmer
#DerivitveProgram.py

from math import sin,cos, tan, acos, asin, asin
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2


precision = 0.000001
data = {}
function = input('Enter a function')


lowerRange = float(input('Enter the lower limit'))
upperRange = float(input('Enter the upper limit'))
step = float(input('Enter the step'))
lowerRangeValue = 0
#Getting the y-values of the original function


#This function gets the y-values of the function that the user had inputed for any given value of x. The function 'eval' will find the solution to the mathmatic problem in it, and replace the variable 'x' with the x value that was used for the GetValue function.
def getValue(x):
    Locfunction = function.lower()
    y = eval(Locfunction)

    return y
#This will get all zeros of the function. It looks for points of the function where the y-value either equals zero or crosses over the x axis.
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

    
#Getting the values for the first derivitive. It does this by using the symetric difference stratagy. It finds the slope at the point by using the two points that either a little bit higher or a little bit lower, and finding the slope between those points.
def getFirstDerivite(x):
    firstDerivitive = (getValue(x+precision)-getValue(x-precision))/(2*precision)
    return firstDerivitive


#Getting the values for second derivitive. This also uses the symetric difference quotient. The only difference instead, is that the being used to find the derivitive is the first derivitive of the function, not the original function.
def getSecondDerivitive(x):
    secondDerivitive = (getFirstDerivite(x+precision)-getFirstDerivite(x-precision))/(2*precision)
    return secondDerivitive


#This is the function that finds all of the upper or lower extrema of the function. It searches for points where the first derivitive is changing signs. If the slope of the graph is going from positive to negative, or negative to positive, then that means that the point in between is an extrema.
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
        if getFirstDerivite(c) < avg and getFirstDerivite(c+step) > avg:
            print('The average slope is equal to the tangent line slope at',c)
        if getFirstDerivite(c) > avg and getFirstDerivite(c+step) < avg:
            print('The average slope is equal to the tangent line slope at',c)
        if getFirstDerivite(c) == avg:
            print('The average slope is equal to the tangent line slope at',c)
        c+=step
meanValue()
    







