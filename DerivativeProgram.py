#Matthew Siegel
#DerivitveProgram.py



terms = int(input('How many terms do you have?'))
data = {}
for i in range(1,terms+1):
    data['coefficient',i] = float(input('Enter the coefficient'))
    data['exponent',i] = float(input('Enter the exponent'))

lowerRange = float(input('Enter the lower limit'))
upperRange = float(input('Enter the upper range'))
interval = float(input('Enter the interval'))
lowerRangeValue = 0
def getValue(x):
    y = 0
    for i in range(1,terms+1):
        y += (data['coefficient',i])*((x)**data['exponent',i])
    return y



