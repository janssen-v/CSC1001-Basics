# Class for differentiation
# 2*x^3+3*x^2+5*x+1 = 6*x^2+6*x+5

class Differential:
    def __init__(self, polynomial=''):
        self.polynomial = polynomial

    def splitPolynomial(self):
        diff = self.polynomial.split('+')
        return diff

    def separateValues(self, diff):
        separated = []
        differentiated = []
        for i in range(len(diff)):
            if '*' in (diff[i]):
                if '^' in (diff[i]):
                    base     = diff[i].split('^')[0]
                    exponent = diff[i].split('^')[1]
                    separated.append ((base, exponent))
                else:
                    differentiated.append ((diff[i].split('*')[0]))
        return (separated, differentiated)
    
    def differentiate(self, equation):
        print(equation)
        base = equation[0]
        conjugate = int(base.split('*')[0])
        variable = (base.split('*')[1])
        exponent = int(equation[1])
        newConjugate = str(conjugate * exponent)
        newExponent = str(exponent - 1)
        if int(newExponent) > 1:
            differential = ''.join([newConjugate,'*',variable,'^',newExponent])
        else:
            differential = ''.join([newConjugate,'*',variable])
        print (differential)
        return (differential)

    def getDifferential(self):
        differential = []
        splitPolynomial = self.splitPolynomial()
        differentiables = (self.separateValues(splitPolynomial))[0]
        for i in range(len(differentiables)):
            returnedDiff = (self.differentiate((differentiables)[i]))
            differential.append(returnedDiff)
        differential.append((self.separateValues(splitPolynomial))[1])
        return ''.join(differential)


equation = Differential('2*x^3+3*x^2+5*x+1')
equation.getDifferential()