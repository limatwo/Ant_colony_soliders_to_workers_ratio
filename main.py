import numpy as np
import matplotlib.pyplot as plt


#initial count of eggs on day 0
N_egg = 1000
#mortality percentage of eggs
U_egg = 0.006
#mortality of soldiers
U_soldiers = 0.006

New_s_t = 0

New_w_t = 0
'''
 (count of eggs generated in a day or
put another way number of eggs produced per day )
'''
K_egg = 3

# run simulation for these number of days
days=1000

# intial count of workers
N_workers = 300
# intial count of soldiers
N_soldiers = 200

# intial no. of new soldiers on day zero calculated from intial no of soldiers and workers N_soldiers/N_workers
ks = N_soldiers / ( N_soldiers + N_workers )


# calculates the number of eggs over the length of the simulation in days.
def incumbent():
    global N_egg
    #array to hold the count of eggs on each day
    eggArr = []
    #run the model for 1000 days
    for time in range(0, days):
        N_egg = N_egg * (1 - U_egg) + K_egg
        eggArr.append(N_egg)  # fills the array eggArr=[]
       # print "Eggs after day "+ str(time)+ " : "+str(N_egg)+"\n"
    return eggArr



def plotEggs(eggArr):
    plt.figure(1)
    plt.plot(xrange(0, days), eggArr)
    plt.ylabel('eggs')
    plt.xlabel('days')
    # plt.savefig('eggs.png')


# calculates the  intial percentage of soldiers at the start of the simulation
def intialize_soldier ():
    global N_workers
    global N_soldiers
    N_soldiers = N_soldiers / ((N_soldiers+N_workers)* 100 )
    print " starting % of soldiers : "+str(N_soldiers)
    return N_soldiers

# calculates the  intial percentage of workers at the start of the simulation
def intialize_worker ():
    global N_workers
    global N_soldiers
    N_worker = N_workers / ((N_soldiers+N_workers)* 100 )
    print " starting % of soldiers"
    return N_worker

# looks up the number of soldiers after 75 days with the intial input number of soldiers on day 1 ( saturation function)
def lookup_soldiers ():
    global N_soldiers
    if  N_soldiers < 20 :
        soldier_inc = 5
    elif  N_soldiers > 20 &  N_soldiers < 50 :
        soldier_inc = 2.5
    print "soldier inc : "+str(soldier_inc) # shows the soldier increase on the console.
    return soldier_inc

# looks up the number of workers after 75 days with the intial input number of workers on day 1 ( saturation function)
def lookup_workers ():
    if  N_workers < 20 :
        worker_inc = 5
    elif  N_workers > 20 &  N_workers < 50 :
        worker_inc = 2.5
    return worker_inc

# produces the percentage of soldiers that will hatch once multiplied by the number of  eggs
def newsoldiers_Req_ks ():
    global soldier_inc
    global N_egg
    ks =  (soldier_inc * (New_s_t + New_w_t)- N_soldiers)/ N_egg
    print "new soldiers required"
    return ks

# produces the number of soldiers after subtracting mortality
def newsoldiers ():
    global N_soldiers
    global ks
    soldierArr = []
    for time in range(0, days):
        N_soldiers = N_soldiers*( 1 - U_soldiers ) + ks *(N_egg)
        soldierArr.append(N_soldiers)
        #print "new soldiers"
    return soldierArr

# produces the percentage of workers that will hatch once multiplied by the number of  eggs

def newworkers_Req_Kw ():
    global worker_inc
    k_w =  ( worker_inc * (New_s_t + New_w_t)- New_w_t)/ N_egg
    print "new soldiers required"
    return

# plots the number of soldiers against days

plt.savefig('destination_path.png', format='png', dpi=200)
def plotsoldiers(N_soldiers):
    plt.figure(2)
    plt.plot(xrange(0, days), N_soldiers )
    plt.ylabel('soldiers')
    plt.xlabel('days')

soldierArr=newsoldiers()
plotsoldiers(soldierArr)
plt.savefig('soldier_path.png', format='png', dpi=200)

eggArr = incumbent()
plotEggs(eggArr)
plt.savefig('destination_path.png', format='png', dpi=200)

# calling of functions
intialize_soldier()
lookup_soldiers()