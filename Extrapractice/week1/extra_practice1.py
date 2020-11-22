#################################################
# ep1.py
#################################################

import cs112_f20_week1_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# functions (for you to write)
#################################################

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    sum_of_radii = r1 + r2
    return (distance(x1, y1, x2, y2) <= sum_of_radii )

def getInRange(x, bound1, bound2):
    upper_bound = max(bound1, bound2)
    lower_bound = min(bound1, bound2)
    if x < lower_bound:
        return lower_bound
    elif x > upper_bound: 
        return upper_bound
    else:
        return x

def isFactor(f, n):
    if n == 0:
        return True
    elif f == 0 :
        return False
    return n % f == 0

def fabricYards(inches):
    return math.ceil(inches / 36) 
 
def fabricExcess(inches):
    return fabricYards(inches) * 36 - inches

def isMultiple(m, n):
    return isFactor(n, m)

def isLegalTriangle(s1,s2,s3):
    if s1 > 0 and s2 > 0 and s3 > 0:
        return s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1
    return False    

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x3, y3, x1, y1)
    
    if isLegalTriangle(s1,s2,s3):
        result =  almostEqual((s1**2 + s2**2), s3**2)
        result = result or almostEqual((s2**2 + s3**2), s1**2)
        result = result or  almostEqual((s1**2 + s3**2), s2**2)
        return result
    else:
        return False

def isEvenPositiveInt(x):
    return type(x) == int and x > 0 and x % 2 == 0

def nthFibonacciNumber(n):
    if n <=1 :
        return 1
    # elif n == 2:
    #     return 2
    return roundHalfUp(((1+5**0.5)**(n+1)-(1-5**0.5)**(n+1))/(2**(n+1)*5**0.5))

def isFactorish(n):
    if type(n) == int :
        n = abs(n)
        ones = n % 10
        tens = n // 10 % 10
        hundreds = n // 100 % 10
        if n // 1000 % 10 :
            return False
        zero = ones and tens and hundreds
        same = (ones!=tens and ones!=hundreds and tens!=hundreds)  
        result = zero and same     
        return result
    return False

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed.')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed.')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed.')

def testIsFactor():
    print('Testing isFactor()... ', end='')
    assert(isFactor(1,1) == True)
    assert(isFactor(2,10) == True)
    assert(isFactor(-5,25) == True)
    assert(isFactor(5,0) == True)
    assert(isFactor(0,0) == True)
    assert(isFactor(2,11) == False)
    assert(isFactor(10,2) == False)
    assert(isFactor(0,5) == False)
    print('Passed.')

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print('Passed.')

def testIsMultiple():
    print('Testing isMultiple()... ', end='')
    assert(isMultiple(1,1) == True)
    assert(isMultiple(2,10) == False)
    assert(isMultiple(-5,25) == False)
    assert(isMultiple(5,0) == False)
    assert(isMultiple(0,0) == True)
    assert(isMultiple(2,11) == False)
    assert(isMultiple(10,2) == True)
    assert(isMultiple(0,5) == True)
    assert(isMultiple(25,-5) == True)
    print('Passed.')

def testIsLegalTriangle():
    print('Testing isLegalTriangle()... ', end='')
    assert(isLegalTriangle(3, 4, 5) == True)
    assert(isLegalTriangle(5, 4, 3) == True)
    assert(isLegalTriangle(3, 5, 4) == True)
    assert(isLegalTriangle(0.3, 0.4, 0.5) == True)
    assert(isLegalTriangle(3, 4, 7) == False)
    assert(isLegalTriangle(7, 4, 3) == False)
    assert(isLegalTriangle(3, 7, 4) == False)
    assert(isLegalTriangle(5, -3, 1) == False)
    assert(isLegalTriangle(-3, -4, -5) == False)
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testIsEvenPositiveInt():
    print('Testing isEvenPositiveInt()... ', end='')
    assert(isEvenPositiveInt(809) == False)
    assert(isEvenPositiveInt(810) == True)
    assert(isEvenPositiveInt(2389238001) == False)
    assert(isEvenPositiveInt(2389238000) == True)
    assert(isEvenPositiveInt(-2389238000) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt('do not crash here!') == False)
    print('Passed.')

def testNthFibonacciNumber():
    print('Testing nthFibonacciNumber()... ', end='')
    assert(nthFibonacciNumber(0) == 1)
    assert(nthFibonacciNumber(1) == 1)
    assert(nthFibonacciNumber(2) == 2)
    assert(nthFibonacciNumber(3) == 3)
    assert(nthFibonacciNumber(4) == 5)
    assert(nthFibonacciNumber(5) == 8)
    assert(nthFibonacciNumber(6) == 13)
    print('Passed.')

def testIsFactorish():
    print('Testing isFactorish()...', end='')
    assert(isFactorish(412) == True)      # 4, 1, and 2 are all factors of 412
    assert(isFactorish(-412) == True)     # Must work for negative numbers!
    assert(isFactorish(4128) == False)    # has more than 3 digits
    assert(isFactorish(112) == False)     # has duplicates digits (two 1's)
    assert(isFactorish(420) == False)     # has a 0 (no 0's allowed)
    assert(isFactorish(42) == False)      # has a leading 0 (no 0's allowed)
    assert(isFactorish(1.0) == False)     # floats are not factorish
    assert(isFactorish('nope!') == False) # don't crash on strings
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testIsFactor()
    testFabricYards()
    testFabricExcess()
    testIsMultiple()
    testIsLegalTriangle()
    testIsRightTriangle()
    testIsEvenPositiveInt()
    testNthFibonacciNumber()
    testIsFactorish()

def main():
    cs112_f20_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
