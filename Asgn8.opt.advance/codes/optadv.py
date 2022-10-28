import numpy as np
import matplotlib.pyplot as plt
import cvxpy  as cp
from math import log
import sys, os
#sys.path.insert(0,'/sdcard/Download/tabrez7/CoordGeo')

#if using termux
import subprocess
import shlex
#Defining f(x)


#Input parameters

#from given function f(x)=(1/8)lnx-bx+x^2,following constants are imagined

a = (1/8) #co-efficient of "lnx"
c=1 	  #co-efficient of "x^2"
b = 7	  # Given that b>0, so "b" assumed equal to 7
def f(x,a,b,c):
	z=log(x) 			#log(x)=lnx
	vector=np.vectorize(float)
	z=vector(z)			# z=log(x)
	return a * z - b * x + c*x**2 	#Given function f(x)=(1/8)lnx-bx+x^2
#Defining derivative of f(x)
df = lambda x: a*(1/x) - b + 2*c*x            

print("--------------------------------------------------------------------")
#For Maxima using gradient ascent
cur_x1=0.5
previous_step_size1=1
iters1=0
precision=0.000000001
alpha=0.0001
max_iters=100000000
while (previous_step_size1>precision)&(iters1<max_iters):
	prev_x=cur_x1
	cur_x1+=alpha*df(prev_x)
	previous_step_size1=abs(cur_x1-prev_x)
	iters1+=1
max_val = f(cur_x1,a,b,c)
print('Maximum value of x is',max_val,"at","x=",cur_x1)
print("--------------------------------------------------------------------")
#For Minima using gradient ascent
cur_x2=1.5
previous_step_size2=1
iters2=0
while (previous_step_size2>precision)&(iters2<max_iters):
	prev_x=cur_x2
	cur_x2-=alpha*df(prev_x)
	previous_step_size2=abs(cur_x2-prev_x)
	iters2+=1
min_val = f(cur_x2,a,b,c)
print('Minimum value of x is',min_val,"at","x=",cur_x2)
print("--------------------------------------------------------------------")



#Plotting the given function f(x)=(1/8)lnx-bx+x^2
xdata = np.arange(0.000001,8, 0.001)
ydata = a*(np.log(xdata)) - b*xdata + xdata**2
plt.plot(xdata, ydata, 'r', label='$f(x)=(1/8)lnx-bx+x^2$')

# Settng title for the plot in blue color
plt.title('Graph of the function: $f(x)=(1/8)lnx-bx+x^2$', color='b')
plt.grid()

# Highlighting axis at x=0 and y=0
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

Max=np.array(([cur_x1, max_val])) #Maximum value including its location
Min=np.array(([cur_x2, min_val])) #Minimum value including its location

#labelling the curve and points
tri_coords = np.vstack((Max,Min)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['Max=(0.01, -0.62)','Min=(3.48, -12.09)']
for i, txt in enumerate(vert_labels):
        plt.annotate(txt, # this is the text
                (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(-14,-11), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center
        plt.xlabel('$x-axis$')
        plt.ylabel('$y-axis$')
        plt.legend(loc='best')
        plt.grid()
        plt.axis('equal')
# Finally displaying the plot
plt.savefig('/home/administrator/Assignment8/optadvfig.pdf')  
plt.show()

