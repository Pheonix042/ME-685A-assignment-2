import numpy as np
from math import sqrt
x=[1,1,1]
F=[0,0,0]
F[0]=lambda x,y,z: 16*x**4 + 16*y**4 + z**4 -15
F[1]=lambda x,y,z: x**2+y**2+z**2-3
F[2]=lambda x,y,z: x**3-y
j=[[0 for col in range(3)] for row in range(3)]
j[0][0]=lambda x,y,z:64*x**3
j[0][1]=lambda x,y,z:64*y**3
j[0][2]=lambda x,y,z:2*z
j[1][0]=lambda x,y,z:2*x
j[1][1]=lambda x,y,z:2*y
j[1][2]=lambda x,y,z:2*z
j[2][0]=lambda x,y,z:3*x**2
j[2][1]=lambda x,y,z:-1
j[2][2]=lambda x,y,z:0
ca_a=[0,0,0]
ca_b=[[0 for col in range(3)] for row in range(3)]
norm=sqrt(3)
while norm>(1e-5):
    print(x)
    for num1 in range(3):
        a=F[num1]
        ca_a[num1]=a(x[0],x[1],x[2])
        for num2 in range(3):
            b=j[num1][num2]
            ca_b[num1][num2]=b(x[0],x[1],x[2])
    j_in=np.linalg.inv(ca_b)
    sub_t=np.matmul(j_in,ca_a)
    x_old=x
    for num3 in range(3):
        x[num3]-=sub_t[num3]
    norm=sqrt((x[0]-x_old[0])**2+(x[1]-x_old[1])**2+(x[2]-x_old[2])**2)
print('Result is:',x)
