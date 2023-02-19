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


a = [3, 5]
b = [0.5, 1]
# print([[x, y] for x, y in zip(np.arange(0, 1, .01), list(reversed(np.arange(0, 1, .01))))])

# points = segment(a, b)
# print(points)
#
# x_coords, y_coords = zip(*points)
# plt.plot(x_coords, y_coords, 'o')
# plt.show()


# Quiz 2.7.1: Write a procedure zero_vec(D) with the following spec:
# • input: a set D
# • output: an instance of Vec representing a D-vector all of whose entries have value zero
def zero_vec(D):
    return Vec(D, {x:0 for x in D})
