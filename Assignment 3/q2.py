# Class for differentiation
# 2*x^3+3*x^2+5*x+1 = 6*x^2+6*x+5

class Differential:
    def __init__(self, polynomial=''):
        self.polynomial = polynomial

    def splitPolynomial(self):
        diff = self.polynomial
        diff = diff.replace('-', '+') # Changes all operators to positive to make polynomial easier to split
        diff = diff.split('+')        # Splits polynomial at the operator
        return diff

    def getOperators(self):
        polynomial = self.polynomial
        polySlice = []
        operatorList = []
        polySlice[:0] = polynomial # Slicing the polynomial into individual characters
        for i in range(len(polySlice)):
            if polySlice[i] == '+' or polySlice == '-':
                operatorList.append(polySlice[i])
        return operatorList

    def separateValues(self, diff, var='x'):
        separated = []
        differentiated = []
        for i in range(len(diff)):
            if '*' in (diff[i]): # If there is both a coefficient and an exponent -> 6*x^2
                coefficient = diff[i].split('*')[0]
                if '^' in (diff[i]):
                    variableExponent = diff[i].split('*')[1]
                else: # If there is a coefficient but no exponent -> 6*x
                    variableExponent = ''.join((var,'^1'))
            elif diff[i] == var: # If there is no coefficient or exponent
                coefficient = '1'
                variableExponent = ''.join((var,'^1'))
            elif var in (diff[i]): # If there is an exponent but no coefficient
                coefficient = '1'
                variableExponent = ''.join(var,diff[i].split(var)[0])
            separated.append ((coefficient, variableExponent))
        return (separated)
    
    def differentiate(self, equation):
        coefficient = int(equation[0])
        variableExponent = equation[1]
        variable = str(variableExponent.split('^')[0])
        exponent = int(variableExponent.split('^')[1])
        newCoefficient = str(exponent * coefficient)
        newExponent = str(exponent - 1)
        if int(newExponent) > 1 and int(newCoefficient) == 1: # e.g -> x^2
            differential = ''.join([variable,'^',newExponent])
        elif int(newExponent) == 1 and int(newCoefficient) == 1: # e.g. -> x
            differential = ''.join([variable])
        elif int(newExponent) == 0 and int(newCoefficient) > 0: # e.g. -> 1
            differential = ''.join([newCoefficient])
        elif int(newExponent) == 1 and int(newCoefficient) > 1: # e.g. -> 3*x
            differential = ''.join([newCoefficient,'*', variable]) 
        elif int(newExponent) > 1 and int(newCoefficient) > 1:
            differential = ''.join([newCoefficient,'*',variable,'^',newExponent]) # e.g. -> 3*x^2
        return (differential)

    def getDifferential(self):
        differential = []
        operators = self.getOperators()
        splitPolynomial = self.splitPolynomial()
        differentiables = (self.separateValues(splitPolynomial))
        for i in range(len(differentiables)):
            returnedDiff = (self.differentiate((differentiables)[i]))
            differential.append(returnedDiff)
            try:
                differential.append(operators[i])
            except:
                continue
        print(differential)

equation = Differential('2*x^3+3*x^2+5*x+1')
equation.getDifferential()
