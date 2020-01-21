import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#def my_func(t):
 #   if t< 4:
  #      return 1
 #   return 0
#print(my_func(3))

#def my_func(var1, var2)
#ef morpho_func(t):
#res = 1
#if t>4:
#res=0
#return res
from scipy.misc import derivative


def morpho_func(t):
    res = 1
    if t>4:
        res=0
    return res

Xs = np.linspace(0,10,100)
Ys = [morpho_func(x) for x in Xs]
fig,ax = plt.subplots()
ax.plot(Xs,Ys)
#fig.savefig("figures/exercise1.svg")
plt.show()

def derivative(P,t,r,n,P0):
    M= morpho_func(t)
    res= M + r* (P**n )/ (P**n + P_0**n)-P
    return res

r=2
n=5
P_0=1
P=0
times =[P]
list1=[0]
dtau=0.1
for t in np.arange(0,10,dtau):
 P = P +dtau*(derivative(P,t,r,n,P_0))
 list1.append(P)
 times.append(t)

fig,ax = plt.subplots()
ax.plot(times,list1)
ax.set_xlabel("t")
ax.set_ylabel("P")
plt.show()