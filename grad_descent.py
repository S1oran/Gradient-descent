import math
from sympy.utilities.lambdify import lambdify
from sympy import symbols


point = []
print("Enter a starting point")
for i in range(2):
    point.append(int(input()))


def gradient_of_function():
    """Find a gradient of function"""
    x1 = symbols('x1')
    x2 = symbols('x2')
    func = 5 * (x1 - 3) ** 2 + 10 * (x2 - 7) ** 2 + 98
    f1 = func.diff(x1)
    f2 = func.diff(x2)
    grad = [f1, f2]
    return grad


def gradient_in_point(gradient, start_point):
    """Find a gradient value in point"""
    x1 = symbols('x1')
    x2 = symbols('x2')
    d1 = lambdify(x1, gradient[0])
    d12 = lambdify(x2, gradient[1])
    global point
    point = [d1(start_point[0]), d12(start_point[1])]
    return point


def descent(t, grad_in_p, tochki):
    """The iterative formula; find x[k+1]"""
    rez = [tochki[0]-t*grad_in_p[0], tochki[1]-t*grad_in_p[1]]
    new_point = [rez[0], rez[1]]
    return new_point


print("Enter step size")
step_size = float(input())
print("Enter epsilon")
epsilon = float(input())
first_point = point
gr = gradient_of_function()
value_in_gradient = gradient_in_point(gr, point)
i = 0
while math.sqrt(point[0]**2+point[1]**2 > epsilon):
    xk = descent(step_size, value_in_gradient, first_point)
    value_in_gradient = gradient_in_point(gr, xk)
    first_point = descent(step_size, value_in_gradient, first_point)
    print(xk)
    i = i+1
print("Number of iterations: ", i)








