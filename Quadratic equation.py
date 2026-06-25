
#calculation of qudratic equation using python

#(z = a*x**2 + b*x + c)


a = int(input("enter value of a: "))


b = int(input("enter value of b: "))


c = int(input("enter value of c: "))



print("the root value of quadratic eqn is", (-b-(b**2-4*a*c)**0.5)/(2*a))


print("the root value of quadratic eqn is", (-b+(b**2-4*a*c)**0.5)/(2*a))