from math import sqrt
x=[0,0]
x[0]=float(input('Enter x1:'))
x[1]=float(input('Enter x2:'))
g1=lambda x,y: 4*x-4*x**3+x**5+y-2*max(0,4*x-12)
g2=lambda x,y: x+y
g=[g1(x[0],x[1]),g2(x[0],x[1])]
f1=g1(x[0],x[1])
f2=g2(x[0],x[1])
################
#norm=sqrt(f1**2+f2**2)
#while norm>(1e-5):
#    d=[-f1/norm,-f2/norm]
#    alp=((x[0]+x[1])*norm)/(f1+f2)
#    x[0]=x[0]-(alp*d[0])
#    x[1]=x[1]-(alp*d[1])
#    if (2*x[0]**2-12*x[0]-x[1]+23)<=0:
#        pass
#    else:
#        x[1]=2*x[0]**2-12*x[0]+23
#    f1=g1(x[0],x[1])
#    f2=g2(x[0],x[1])
#    norm=sqrt(f1**2+f2**2)
#    print(x)
#########################
h1=lambda x:5*x**4-12*x**2-4
H=[[h1(x[0]),1],[1,1]]
import numpy as np
in_h=np.linalg.inv(H)
fun=lambda x,y:2*x**2-x**4+(x**6/6)+x*y+(y**2/2)
nor=fun(x[0],x[1])
k=0
while nor>1e-5 and k<=100:
    x=x-(np.matmul(in_h,g))
    g=[g1(x[0],x[1]),g2(x[0],x[1])]
    H=[[h1(x[0]),1],[1,1]]
    in_h=np.linalg.inv(H)
    nor=fun(x[0],x[1])
    k+=1
    print(x)
