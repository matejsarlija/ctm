from random import randint
import math

x = 3
y = math.sqrt(x)
z = pow(y, 2)
print(z)
#print("Square root of -1 is ", math.sqrt(-1))
print("The cosine of pi is ", math.cos(math.pi))
print("In python .math, e is ", math.e)
print("the log of e is", math.log(math.e))

def movie_review(str_movie):
    print('Regarding %s - %s'
          %(str_movie, {x:y for (x,y) in enumerate(["See it!", "A gem!", "Ideological claptrap!"])}[randint(0,2)],))


movie_review("Matrix")

def quadratic(a,b,c):
    discriminant = math.sqrt(b*b - 4*a*c)
    return ((-b + discriminant)/(2*a), (-b -discriminant)/(2*a))

f = open("input2.txt")
lines = list(f)
print(lines)