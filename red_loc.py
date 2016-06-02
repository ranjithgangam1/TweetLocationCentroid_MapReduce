#!/usr/bin/env python

import sys

summation1 = 0;
summation2 = 0;
count1 = 0;
count2 = 0;
for line in sys.stdin: 
  (key,val) = line.split('\t')
  if eval(val):
    #loc = eval(line[1]
    val = eval(val)
    summation1 += float(val[0])
    summation2 += float(val[1])
    count1 +=1 
  else:
    count2 +=1

centroid = (summation1/count1,summation2/count1)
proportion = (float(count1)/float(count2))*100;
print 'centroid',centroid
print 'proportion%',proportion
