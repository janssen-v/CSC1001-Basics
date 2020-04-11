# Class for differentiation
# 2*x^3+3*x^2+5*x+1 = 6*x^2+6*x+5

class Differential:
    def __init__(self, polynomial=''):
        self.polynomial = polynomial
        
    def differentiables(self):
        diff = self.polynomial.split('+')
        return diff

    def differentiate(self):
        differentiables = self.differentiables()
        for i in range(len(differentiables)):
            if '*' in (differentiables[i]):
                if '^' in (differentiables[i]):
                    base     = differentiables[i].split('^')[0]
                    exponent = differentiables[i].split('^')[1]
                    print(base)
                    print(exponent)
                else:
                    return differentiables[i].split('*')[1]

equation = Differential('2*x^3+3*x^2+5*x+1')
print(equation.differentiables())
print(equation.differentiate())