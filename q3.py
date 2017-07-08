fun='cos(10*acos(x)+(pi/6))+log(2*x+5)'#str(input('Enter the function:'))
st=-0.3#float(input('Enter the start of interval:'))
stop=0.8#float(input('Enter stop of interval:'))
inter=int(input('Enter number of interval'))
h=(stop-st)/inter
from romil import matri,fv,b_rhs,replacement_gen,back_sub1,coef,f2val,monoo
f_val=fv(st,h,inter,fun)
A=matri(h,inter)
b=b_rhs(f_val,h,inter)
X=[0]*(inter+1)
mat,b=replacement_gen(A,(inter+1),b)
X=back_sub1(mat,b,(inter+1),X)
bi,di=coef(f_val,X,h,inter)
v=st
pol=[]
for num in range(inter):
    sa=lambda x: f_val[num]+bi[num]*(x-v)+X[num]*(x-v)**2+di[num]*(x-v)**3
    v=st+h
    pol.append(sa)
x_val,f2_val=f2val(fun,st,stop)
interpol=monoo(x_val,f2_val)
mono_pol=lambda x: interpol[0]+interpol[1]*x+interpol[1]*x**2+interpol[1]*x**3+interpol[1]*x**4+interpol[1]*x**5+interpol[1]*x**6+interpol[1]*x**7+interpol[1]*x**8
mono_y=[]
from pylab import *
import matplotlib.pyplot as plt
pol_x=linspace(st,stop,50)
for num1 in range(len(pol_x)):
    x=round(pol_x[num1],6)
    y=mono_pol(x)
    mono_y.append(y)
yy=[]
for num3 in range(inter):
    a=pol[num3]
    y1=[]
    for num2 in range(len(pol_x)):
        y=a(num2)
        y1.append(y)
    yy.append(y1)
plt.plot(pol_x,mono_y,'g')
star=st
stp=(st+h)
for num4 in range(inter):
    xx=linspace(star,stp,50)
    plt.plot(xx,yy[num4],'r')
    star=stp
    stp+=+h
plt.show()
