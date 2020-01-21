# -*- coding: utf-8 -*-
"""
Spyder Edit
This is a temporary script file.
"""# Function definition is here
#from scipy.integrate import odeint

import matplotlib.pyplot as plt

N=1000
Net=0
umE=0.2
Ke=150

def incumbent():
    global N
    eggArr=[]
    for time in range(0,74):
        N=N*(1-umE)+Ke
        eggArr.append(N) # fills the array eggArr=[]
        print N
        print(time)        
    return eggArr
#   "This prints a passed info into this function"
#   print "Name: ", name
#   print "Age ", age
#   return;
def plotEggs(eggArr):
    plt.figure(1)
    plt.plot(xrange(0,74),eggArr)
    plt.ylabel('eggs')
    #plt.savefig('eggs.png')
        

# Now you can call printinfo function
#printinfo( age=50, name="miki" )
#def printme( str ):
#   "This prints a passed string into this function"
#  print str
#  return

e=incumbent()
plotEggs(e)
plt.savefig('destination_path.png', format='png', dpi=50)