x_axi=[]
y=[]
for num in range(4):
    print('Enter x',num+1)
    in1=float(input('Value:'))
    print('Enter y',num+1)
    in2=float(input('Value:'))
    x_axi.append(in1)
    y.append(in2)
Y=y[:]
from romil import newton_p,mono,lagra
mee=newton_p(x_axi,Y)
print(mee)
ne1=lambda x: mee[0]+mee[1]*(x-x_axi[0])+mee[2]*(x-x_axi[1])*(x-x_axi[0])+mee[3]*(x-x_axi[2])*(x-x_axi[1])*(x-x_axi[0])
moo=mono(x_axi,y)
print(moo)
ne2=lambda x:moo[0]+moo[1]*x+moo[2]*x**2+moo[3]*x**3
la,numera=lagra(x_axi,Y)
print(la)
print(numera)
l1=lambda x:((x+la[0][0])*(x+la[0][1])*(x+la[0][2]))/numera[0]
l2=lambda x:((x+la[1][0])*(x+la[1][1])*(x+la[1][2]))/numera[1]
l3=lambda x:((x+la[2][0])*(x+la[2][1])*(x+la[2][2]))/numera[2]
l4=lambda x:((x+la[3][0])*(x+la[3][1])*(x+la[3][2]))/numera[3]
ne3=lambda x:Y[0]*l1(x)+Y[1]*l2(x)+Y[2]*l3(x)+Y[3]*l4(x)
yo1=[]
yo2=[]
yo3=[]
from pylab import *
import matplotlib.pyplot as plt
zox=linspace(x_axi[0],x_axi[3],100)
for num in range(100):
    xx=zox[num]
    y1=ne1(xx)
    y2=ne2(xx)
    y3=ne3(xx)
    yo3.append(y3)
    yo2.append(y2)
    yo1.append(y1)
plt.plot(zox,yo1,'bo')
plt.plot(zox,yo2,'r*')
plt.plot(zox,yo3,'g')
plt.show()
