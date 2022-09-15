#Code by Meer Tabres Ali (works on termux)
#To find the angles and sides of the trapezium
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import sys     #for path to external scripts

def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB


sys.path.insert(0,'/home/CoordGeo')
#local imports

#if using termux
import subprocess
import shlex
#end if

#Input parameters
A = np.array(([-2, 2]))
B = np.array(([ 2, 2]))
C = np.array(([ 4, 0]))
D = np.array(([-4, 0]))

a = np.linalg.norm(A-B)
print("length of side AB")
print(a)

b = np.linalg.norm(B-C)
print("length of side BC")
print(b)

c = np.linalg.norm(C-D)
print("length of side CD")
print(c)

d = np.linalg.norm(D-A)
print("length of side DA")
print(d)
print("---------------------")
print("Solution of Q12.1")
angleBAD =np.arccos(np.dot (A-B, A-D)/((np.linalg.norm(A-B)) * np.linalg.norm(A-D)))*57.296
print("Angle BAD")
print(angleBAD)

angleABC =np.arccos(np.dot (B-A, B-C)/((np.linalg.norm(B-A)) * np.linalg.norm(B-C)))*57.296
print("Angle ABC")
print(angleABC)
print("Angle BAD = Angle ABC = 135")
print("---------------------")
print("Solution of Q12.2")
angleADC =np.arccos(np.dot (D-A, D-C)/((np.linalg.norm(D-A)) * np.linalg.norm(D-C)))*57.296
print("Angle ADC")
print(angleADC)

angleBCD =np.arccos(np.dot (C-B, C-D)/((np.linalg.norm(C-B)) * np.linalg.norm(C-D)))*57.296
print("Angle BCD")
print(angleBCD)
print("Angle ADC = Angle BCD = 45")
print("---------------------")
print("Solution of Q12.3")
print("Sides and Angles of Triangle ABC, BAD")
print("All the sides and angles of Triangle ABC , Triangle BAD are similar")
print("Triangle ABC = Triangle BAD")
print("---------------------")
print("Solution of Q12.4")
e = np.linalg.norm(A-C)
print("length of Diogonal AC")
print(e)

f = np.linalg.norm(B-D)
print("length of Diagonal BD")
print(f)

if e == f:
    print("Digonal AC is equal to Diagonal BD")  
print("---------------------")
  
  
  
  
  
#Given points
A = np.array(([-2,2]))
B = np.array(([ 2,2]))
C = np.array(([ 4,0]))
D = np.array(([-4,0]))


x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_AC = line_gen(A,C)
x_AD = line_gen(A,D)
x_BD = line_gen(B,D)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')


#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x_axis$')
plt.ylabel('$y_axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('trapezium')
#if using termux
#plt.savefig('/home/par.pdf')  
plt.show()
