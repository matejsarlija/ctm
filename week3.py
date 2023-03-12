import numpy
import numpy as np
from matplotlib import pyplot as plt
from vec import Vec


# Write a python procedure segment(pt1, pt2) that, given points represented as
# 2-element lists, returns a list of a hundred points spaced evenly along the line segment whose
# endpoints are the two points
# Plot the hundred points resulting when pt1 = [3.5, 3] and pt2 = [0.5, 1]
def segment(pt1, pt2):
    segment_params = [[x, y] for x, y in zip(np.arange(0, 1, .01), list(reversed(np.arange(0, 1, .01))))]

    points = []

    for x in segment_params:
        point = [x[0] * pt1[0] + x[1] * pt2[0], x[0] * pt1[1] + x[1] * pt2[1]]
        points.append(point)

    return points

# Quiz 2.7.1: Write a procedure zero_vec(D) with the following spec:
# • input: a set D
# • output: an instance of Vec representing a D-vector all of whose entries have value zero
def zero_vec(D):
    return Vec(D, {x:0 for x in D})

def getitem(v, d):
    return v.f[d] if d in v.f else 0

def setitem(v, d, val):
    v.f[d] = val

# Quiz 2.7.3: Write a procedure scalar_mul(v, alpha) with the following spec:
# • input: an instance of Vec and a scalar alpha
# • output: a new instance of Vec that represents the scalar-vector product alpha times v.
def scalar_mul(v, alpha):
    return Vec(v.D, {x:y*alpha for (x,y) in v.f.items()})

# Quiz 2.7.4: Write a procedure add(u, v) with the following spec:
# • input: instances u and v of Vec
# • output: an instance of Vec that is the vector sum of u and v
def add(u, v):
    return Vec(u.D, {x:getitem(u, x) + getitem(v, x) for x in v.D})


v = Vec({'A','B','C'}, {'A':1, 'B':2})
u = Vec(v.D, {'A':5., 'C':10.})
z = Vec({'Z'}, {'Z':1})
x = getitem(v, 'A')
#print((scalar_mul(v, 3)).f)
print((add(z, v)).f)

#print(x)
