import math
# receive values
a = float(input("Enter 'a' value:"))
b = float(input("Enter 'b' value:"))
c = float(input("Enter 'c' value:"))

# calculate delta
delta = (b**2)-(4*a*c)

# calculate square roots
if delta == 0:
    sqrt1 = (-b + math.sqrt(delta))/(2*a)
    print("the solution for this equation is", sqrt1)
else:
    if delta < 0:
        print("this equation has an imaginary root")
    else:  
            sqrt1 = (-b + math.sqrt(delta))/(2*a)
            sqrt2 = (-b - math.sqrt(delta))/(2*a)
            if sqrt1<sqrt2:   
                print(f"the roots for this equation are {sqrt1} and {sqrt2}")
            else:
                print(f"the roots for this equation are {sqrt2} and {sqrt1}")   



