def matrii(x,y):
    mat=[]
    for num1 in range(4):
        row=[]
        for num2 in range(4):
            r=(x[num1])**(num2)
            row.append(r)
        mat.append(row)
    b=y
    return mat,b
def matrii1(x,y):
    mat=[]
    for num1 in range(9):
        row=[]
        for num2 in range(9):
            r=(x[num1])**(num2)
            row.append(r)
        mat.append(row)
    b=y
    return mat,b
def check(A):
    for n in range(4):
        rep=0
        for m in range(4):
            if A[m][n]==0:
                rep+=1
            else:
                pass
        if rep==4:
            break
        else:
            pass
    if rep==4:
        return False
    else:
        return True
def interchange(A,b,num7):
    for num9 in range(num7+1,4):
        pii=A[num9][num7]
        for num10 in range(4):
            A[num9][num10]=A[num9][num10]-(pii*A[num7][num10]/A[num7][num7])
            if abs(A[num9][num10])<(1e-4):
                A[num9][num10]=0
        b[num9]=b[num9]-(b[num7]*pii/A[num7][num7])
        if abs(b[num9])<(1e-4):
            b[num9]=0
    return A,b
def replacement(A,b):
    for num7 in range(4):
        pip=abs(A[num7][num7])
        pivot=num7
        if num7!=(3):
            for num8 in range(num7,4):
                if abs(A[num8][num7])>pip:
                    pivot=num8
                    pip=A[num8][num7]
            A[pivot],A[num7]=A[num7],A[pivot]
            b[pivot],b[num7]=b[num7],b[pivot]
            A,b=interchange(A,b,num7)
        else:
            pass
    return A,b
def replacement_gen(A,rr,b):
    for num7 in range(rr):
        pip=abs(A[num7][num7])
        pivot=num7
        if num7!=(rr-1):
            for num8 in range(num7,rr):
                if abs(A[num8][num7])>pip:
                    pivot=num8
                    pip=A[num8][num7]
            A[pivot],A[num7]=A[num7],A[pivot]
            b[pivot],b[num7]=b[num7],b[pivot]
            A,b=interchange(A,b,num7)
        else:
            pass
    return A,b
def sol_check(A,b):
    if A[3][3]==0:
        if b[3]==0:
            a= 'infinite possible polynomial'
        else:
            a= 'no solution possible'
        return False,a
    else:
        a='Unique polynomial exist'
        return True,a
def back_sub(A,b,X):
    for num12 in range(4,0,-1):
        aa=0
        for num13 in range(num12,4):
            aa=aa-X[num13]*A[num12-1][num13]
        X[num12-1]=(b[num12-1]+aa)/A[num12-1][num12-1]
    return X
def back_sub1(A,b,row,X):
    for num12 in range(row,0,-1):
        aa=0
        for num13 in range(num12,row):
            aa=aa-X[num13]*A[num12-1][num13]
        X[num12-1]=(b[num12-1]+aa)/A[num12-1][num12-1]
    return X
def mono(x,y):
    X=[0]*4
    mat,b=matrii(x,y)
    mat,b=replacement(mat,b)
    xX=back_sub(mat,b,X)
    return xX
def monoo(x,y):
    X=[0]*9
    mat,b=matrii1(x,y)
    mat,b=replacement_gen(mat,9,b)
    xX=back_sub1(mat,b,9,X)
    return xX        
def lagra(x,y):
    numera=[]
    rop=[]
    for num4 in range(4):
        pro=1
        for num5 in range(4):
            if num4!=num5:
                pro=pro*(x[num4]-x[num5])
            else:
                pass
        numera.append(pro)
    for num6 in range(4):
        rp=[]
        for num7 in range(4):
            if num7!=num6:
                subb=-1*x[num7]
                if subb==-0.0:
                    rp.append(0)
                else:
                    rp.append(subb)
            else:
                pass
        rop.append(rp)
    return rop,numera
def newton_p(x,y):
    mat=[[0 for col in range(4)] for row in range(4)]
    for num19 in range(4):
        mat[num19][0]=1
    mat[1][1]=(x[1]-x[0])
    mat[2][1]=(x[2]-x[0])
    mat[3][1]=(x[3]-x[0])
    mat[2][2]=(x[2]-x[1])*(x[2]-x[0])
    mat[3][2]=(x[3]-x[1])*(x[3]-x[0])
    mat[3][3]=(x[3]-x[2])*(x[3]-x[1])*(x[3]-x[0])
    xx=for_sub(mat,y)
    return xx
def for_sub(mat,y):
    x=[0,0,0,0]
    for num17 in range(4):
        if num17==0:
            x[0]=y[0]
        else:
            a=y[num17]
            for num16 in range(num17):
                a=a-(mat[num17][num16]*x[num16])
            x[num17]=a/mat[num17][num17]
    return x
import numpy as nup
from math import sqrt,sin,e,exp,sinh,cos,cosh,tan,tanh,pi,log,log10,log2,factorial,acos,asin,acosh,asinh,atan,atanh
def richar(a,x):
    h=0.005
    al=0.5
    F1=dif(a,x,h)
    F2=dif(a,x,(h/al))
    F3=dif(a,x,(h/al**2))
    F4=deri_dif(F1,F2,2)
    F5=deri_dif(F2,F3,2)
    F6=deri_dif(F5,F4,4)
    return F6
def deri_dif(F1,F2,po):
    F=(F1-(0.5)**po*F2)/(1-(0.5)**po)
    return F
def dif(a,x,h):
    x=x+h
    f1=eval(a)
    x=x-h
    f2=eval(a)
    df=(f1-f2)/(2*h)
    return df
def matri(h,inter):
    mat=[[0 for col in range(inter+1)] for row in range(inter+1)]
    mat[0][0]=1
    mat[inter][inter]=1
    for num1 in range(1,inter):
        mat[num1][num1-1]=h
        mat[num1][num1]=4*h
        mat[num1][num1+1]=h
    return mat
def fv(st,h,inter,fun):
    x=st
    f_val=[]
    for num in range(inter+1):
        f=eval(fun)
        x+=h
        f_val.append(f)
    return f_val
def b_rhs(f,h,inter):
    b=[0]*(inter+1)
    for num in range(1,inter):
        b[num]=3*(f[num+1]-2*f[num]+f[num-1])/h
    return b
def coef(f,X,h,inter):
    bi=[]
    di=[]
    for num in range(inter):
        d=(X[num+1]-X[num])/h
        b=((f[num+1]-f[num])/h)-(h*(2*X[num]+X[num+1])/3)
        bi.append(b)
        di.append(d)
    return bi,di
def f2val(fun,st,stop):
    h=(stop-st)/8
    x=st
    ff=[]
    zo=[]
    for num in range(9):
        zo.append(round(x,7))
        f=eval(fun)
        x=round(x+h,6)
        ff.append(f)
    return zo,ff
def regula(fun,a,b):
    while abs(b-a)>(1e-5):
        #print('A=',a,'B=',b)
        x=a
        f1=eval(fun)
        x=b
        f2=eval(fun)
        c=b-((b-a)*f2/(f2-f1))
        x=c
        f3=eval(fun)
        if f1*f3<0:
            a,b=a,c
        else:
            a,b=c,b
    return c
def diff(fun,st):
    x=st+0.01
    f1=eval(fun)
    x=st-0.01
    f2=eval(fun)
    de=(f1-f2)/(2*0.01)
    return de
def nr(fun,st):
    x=st
    while abs(eval(fun))>1e-5:
        print(x)
        nx=x-(eval(fun)/diff(fun,x))
        x=nx
    return x
