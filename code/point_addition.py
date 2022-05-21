# Point addition in the group E(\Q)
import math

def _reduce(a, b):
    if a < 0 and b < 0:
        a *= -1
        b *= -1
    
    g = math.gcd(int(a), int(b))
    if g == 1:
        return int(a), int(b)
    return _reduce(int(a / g), int(b / g))

def duplication_formula(a, b, c, x, denom):
    numerator =  x ** 4  -  denom ** 2 * 2 * b * x ** 2   -  denom ** 3 * 8 * c * x   +  denom ** 4 * (b ** 2 - 4 * a * c)
    denominator = denom * 4 * x ** 3  +  denom ** 2 * 4 * a * x ** 2  +  denom ** 3 * 4 * b * x  +  denom ** 4 * 4 * c 
    return _reduce(numerator, denominator)

def tangent(a, b, c, x_num, x_denom, y_num, y_denom):
    numerator = y_denom * (3 * x_num ** 2 + 2 * a * x_num * x_denom + b * x_denom ** 2)
    denominator = 2 * y_num * x_denom ** 2
    return _reduce(numerator, denominator)

while True:
    coefficients_entered = False

    while not coefficients_entered:
        coefficients = input('Enter the coefficients of the equation of the elliptic curve in Weierstrass form separated by spaces.\n').split()

        if len(coefficients) != 3:
            print('Please input three values for the coefficients.')
            continue

        coefficients_entered = True 

        for i in range(3):
            try: 
                coefficients[i] = float(coefficients[i])
            except:
                print('Please ensure you enter numbers for the coefficients.')
                coefficients_entered = False
                break

        if coefficients_entered:
            a, b, c = coefficients
            if -4 * a ** 3 * c + a ** 2 * b ** 2 + 18 * a * b * c - 4 * b ** 3 - 27 * c ** 2 == 0:
                print('Please ensure the elliptic curve is not singular.')
                coefficients_entered = False
                break
                

    point_entered = False

    while not point_entered:
        point_1 = input('Enter the components of the first point on the elliptic curve separated by spaces.\n').split()

        if len(point_1) != 2:
            print('Please input two values for the point.')
            continue

        point_entered = True 

        for i in range(2):
            try: 
                point_1[i] = float(point_1[i])
            except:
                print('Please ensure you enter numbers for the components.')
                coefficients_entered = False
                break

        if point_entered:
            if point_1[1] ** 2 != point_1[0] ** 3 + coefficients[0] * point_1[0] ** 2 + coefficients[1] * point_1[0] + coefficients[2]:
                print('Please ensure your point is on the elliptic curve.')
                point_entered = False

    point_entered = False

    while not point_entered:
        point_2 = input('Enter the components of the second point on the elliptic curve separated by spaces.\n').split()

        if len(point_2) != 2:
            print('Please input two values for the point.')
            continue

        point_entered = True 

        for i in range(2):
            try: 
                point_2[i] = float(point_2[i])
            except:
                print('Please ensure you enter numbers for the components.')
                point_entered = False
                break

        if point_entered:
            if point_2[1] ** 2 != point_2[0] ** 3 + coefficients[0] * point_2[0] ** 2 + coefficients[1] * point_2[0] + coefficients[2]:
                print('Please ensure your point is on the elliptic curve.')
                point_entered = False

    try:
        if point_1 == point_2:  
            x = duplication_formula(*coefficients, point_1[0], 1)
            y = []
            slope = tangent(*coefficients, point_1[0], 1, point_1[1], 1)
            y.append(slope[0] * (x[1] * point_1[0] - x[0]) - point_1[1] * slope[1] * x[1])
            y.append(slope[1] * x[1])
            y = _reduce(*y)

        elif point_1[1] != point_2[1]:
            slope = _reduce(point_2[1] - point_1[1], point_2[0] - point_1[0])
            constant = _reduce(point_1[1] * slope[1] - slope[0] * point_1[0], slope[1])
            slope_squared = [i ** 2 for i in slope]
            x = _reduce(slope_squared[0] - slope_squared[1] * (coefficients[0] + point_1[0] + point_2[0]), slope_squared[1])
            y = _reduce(-1 * (slope[0] * x[0] * constant[1] + constant[0] * slope[1] * x[1]), slope[1] * x[1] * constant[1])

        if x[1] != 1:
            x_0 = str(x[0]) + ' / ' + str(x[1])
        else:
            x_0 = str(x[0])

        if y[1] != 1:
            y_0 = str(y[0]) + ' / ' + str(y[1])
        else:
            y_0 = str(y[0])

        again = 'y' in input(f'({x_0}, {y_0})\nWould you like to double this point on the curve? (y/n) ')

        while again:
            slope = tangent(*coefficients, *x, *y)
            x_temp = duplication_formula(*coefficients, *x)
            y_temp = []
            y_temp.append(y[1] * slope[0] * (x_temp[1] * x[0] - x_temp[0] * x[1]) - y[0] * slope[1] * x_temp[1] * x[1])
            y_temp.append(slope[1] * x_temp[1] * y[1] * x[1])
            x = x_temp
            y = _reduce(*y_temp)

            if x[1] != 1:
                x_0 = str(x[0]) + ' / ' + str(x[1])
            else:
                x_0 = str(x[0])

            if y[1] != 1:
                y_0 = str(y[0]) + ' / ' + str(y[1])
            else:
                y_0 = str(y[0])
            again = 'y' in input(f'({x_0}, {y_0})\n({x[0] / x[1]}, {y[0]/y[1]})\nWould you like to double this point on the curve? (y/n) ')

    except ZeroDivisionError:
        print('point at infinity\n')

    except Exception as e:
        print(e)