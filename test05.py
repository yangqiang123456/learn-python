# -*- coding:utf-8 -*-
#########学生基本信息############
#姓名:杨强
#学号:1403050125
#班级：通风14-1班
##############题目###############
#N次多项式
############代码#################
a0,a1,a2,a3,a4,a5,a6,a7=4,5,7,1,21,4,6
x=input('请输入x:')
#计算f(1,x)
f1=a0+a1*x
print 'n=1','x=',x,'f1=',f1
#计算f(2,x)
f2=a0+a1*x+a2*x**2
print 'n=2','x=',x,'f2=',f2
#计算f(5,x)
f5=a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5
print 'n=5','x=',x,'f5=',f5
#计算f(7,x)
f7=a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5+a6*x**6+a7*x**7
print 'n=7','x=',x,'f7=',f7