"""
Lab 1 Example 2
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#1: Define Variables

s = 8 						#number of students
hw = np.array( [10.,10.,8.,9.5,3.,9.,0.,6.])    #homework grades
mt = np.array([10.,10.,10.,10.,8.,5.,10.,7.])   #midterm grades
fp = np.array([9.,10.,10.,6.,10.,6.,8.,9.])     #final project grades

#2: Find Final Grades

fg = hw * 0.4 + mt * 0.2 + fp * 0.4

#3: Write grades to file

F = open("grades.txt","w")
fgs = np.array(fg).astype('str')

i = 0
for i in range(s):
	F.write(fgs[i])
	F.write("\n")
	i+=1

F.close

#4: Print failed, outstanding students to screen

fail = 0
outstanding = 0
j = 0

for j in range(s):			#check grade in range of students
	if (fg[j]<6.):
		fail+=1
		j+=1
	elif (fg[j]>9.5):
		outstanding+=1
		j+=1
	else:
		j+=1

if (fail == 1):					#dealing with pluralities
	print '1 student failed the course.'
else:
	print fail,'students failed the course.'

print outstanding,'out of',s,'students were outstanding.'

#5: Plot the historgram

plt.figure()

fgp = fg * 10					#grade in %
num_bins = 10

n, bins, patches = plt.hist(fgp, num_bins)
#n, bins, patches = plt.hist(fgp, num_bins)
plt.xlim(0.,100.)
plt.ylim(0.,2.)
plt.xlabel('Grade [%]')
plt.ylabel('Number of Students')
plt.show()
plt.savefig('GradeHistogram.png',format='png')
