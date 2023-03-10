import matplotlib.pyplot as plt

def my_filter(L, num):
    new_list = []
    for x in L:
        if x != num:
            new_list.append(x)
    return new_list


our_list = [1,2,4,5,7]
number = 2

print(my_filter(our_list, number))

# Problem 1.7.2: my lists(L)
# input: list L of non-negative integers.
# output: a list of lists: for every element x in L create a list containing 1, 2, . . . , x.
# example: given [1,2,4] return [[1],[1,2],[1,2,3,4]]. example: given [0] return [[]]
def my_lists(L):
    return [[x for x in range(1, x+1, 1)] for x in L]


# my function composition(f,g)
# input: two functions f and g, represented as dictionaries, such that g ◦ f exists.
# output: dictionary that represents the function g ◦ f .
# example: given f = {0:’a’, 1:’b’} and g = {’a’:’apple’, ’b’:’banana’}, return {0:’apple’, 1:’banana’}
def my_function_composition(f, g):
    return {a:d for (a,b),(c,d) in zip(f.items(), g.items())}


# Problem 1.7.4: mySum(L)
# Input: list of numbers
# Output: sum of numbers in the list
def mySum(L):
    current = 0
    for x in L:
        current += x
    return current

# Problem 1.7.5: Product(L)
# input: list of numbers
# output: product of numbers in the list
def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return current


# Problem 1.7.6: myMin(L)
# input: list of numbers
# output: minimum number in the list
def myMin(L):
    current = 0
    for x in L:
        if x < current:
            current = x
    return current


# Problem 1.7.7: myConcat(L)
# input: list of strings
# output: concatenation of all the strings in L
def myConcat(L):
    current = ""
    for x in L:
        current += x
    return current


# Problem 1.7.8: myUnion(L)
# input: list of sets
# output: the union of all sets in L.
def myUnion(L):
    current = []
    for x in L:
        current.append(x)
    return current


# Problem 1.7.12: Write a procedure transform(a,b, L) with the following spec:
# • input: complex numbers a and b, and a list L of complex numbers
# • output: the list of complex numbers obtained by applying f (z) = az + b to each complex
# number in L
def transform(a, b, L):
    output = map(lambda x: a*x + b, L)
    return set(output)


S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

#plt.scatter([pt.real for pt in S], [pt.imag for pt in S])
#plt.show()

new_set = transform(2j, 1+1j, S)
plt.scatter([pt.real for pt in new_set], [pt.imag for pt in new_set])
plt.show()

