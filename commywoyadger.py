#!/usr/bin/env python
#coding=utf8
import matplotlib.pyplot as plt
def mnkLIN(x,y):                             
              a=round((len(x)*sum([x[i]*y[i] for i in range(0,len(x))])-sum(x)*sum(y))/(len(x)*sum([x[i]**2 for i in range(0,len(x))])-sum(x)**2),3)
              b=round((sum(y)-a*sum(x))/len(x) ,3)
              y1=[round(a*w+b ,3) for w in x]         
              s=[round((y1[i]-y[i])**2,3) for i in range(0,len(x))]                          
              sko=round((sum(s)/(len(x)-1))**0.5,3)
              p=(sko*len(x)*100)/sum(y1)
              plt.title('Аппроксимация методом наименьших \n квадратов Y=%s*x+%s с погрешностью  -%i -проц.'%(str(a),str(b),int(p)), size=14)
              plt.xlabel('Количество  городов', size=14)
              plt.ylabel('Длина маршрутов', size=14)
              plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Данные метода ближайшего соседа')
              plt.plot(x, y1, color='b',linewidth=1, label='Аппроксимирующая прямая')
              plt.legend(loc='best')
              plt.grid(True)
              plt.show()
y=[933.516, 1282.842, 1590.256, 1767.327 ,1949.975, 2212.668, 2433.955, 2491.954, 2549.579, 2748.672]
x=[100,200,300,400,500,600,	700,800, 900,1000] 