import numpy
import numpy as np
# Write a python procedure segment(pt1, pt2) that, given points represented as
# 2-element lists, returns a list of a hundred points spaced evenly along the line segment whose
# endpoints are the two points
# Plot the hundred points resulting when pt1 = [3.5, 3] and pt2 = [0.5, 1]
def segment(pt1, pt2):
   segment_params =  [[x,y] for x,y in zip(np.arange(0,1,.01), list(reversed(np.arange(0,1,.01))))]
   for x in segment_params:
      print(x[0]*pt1[0]+x[1]*pt2[0],x[0]*pt1[1]+x[1]*pt2[1])

a = [3,5]
b = [0.5, 1]
print([[x,y] for x,y in zip(np.arange(0,1,.01), list(reversed(np.arange(0,1,.01))))])
print(segment(a, b))
