import matplotlib.pyplot as plt
import random

# run simulation for these number of days
days=367
# season time span
season_timespan_eggs=92
season_timespan_workers=92
season_timespan_soldiers=92 # to eqaute the number of seasons make them all equal to 92 days

# all about eggs
# initial count of eggs on day 0
N_egg = 120
# mortality percentage of eggs per day
#U_egg = 0.02
#U_egg = [[0.02,0.07],[0.06,0.09],[0.04,0.07],[0.05,0.06],[0.02,0.08]]
#U_egg = [[0.001,0.03],[0.001,0.03],[0.001,0.01],[0.001,0.03]]
U_egg = [[0.03,0.03]]
# number of eggs produced per day
K_egg = 10
# Array that stores egg status
eggArr = []


# all about soldiers
# initial count of soldiers
N_soldiers = 50
# mortality of soldiers per day
#U_soldiers = 0.01
U_soldiers = [[0.025,0.025]]
#U_soldiers = [[0.010,0.025],[0.07,0.015],[0.06,0.010],[0.07,0.015]]

# Array that stores the soldiers status
soldierArr = []
# Array that stores the soldier percentages
soldierPercArr= []


# all about workers
# initial count of workers
N_workers = 600
# mortality of workers per day
#U_workers= [0,0.2]
#U_workers=[[0.3,0.5],[0.5,0.6],[0.5,0.6],[0.3,0.5]]
U_workers=[[0.3,0.3]]
# Array that stores the worker status
workerArr = []


# function to plot eggs
def plot_elements(arr, name, num, clr):
    plt.figure(num)
    plt.plot(xrange(0, days), arr, color=clr)
    plt.ylabel(name)
    plt.xlabel('days')



# perform saturation graph lookup
def getPercFromSaturation(soldiers_perc):
    if soldiers_perc<0.05:
        output_perc = (soldiers_perc*(0.03-0.04)/0.05)+0.04
    elif soldiers_perc < 0.10:
        output_perc = ((soldiers_perc-(0.05))*(0.05-0.03)/0.05)+0.03
    elif soldiers_perc < 0.20:
        output_perc = 0.05
    elif soldiers_perc < 0.50:
        output_perc = ((soldiers_perc-(0.20))*(0.02-0.05)/0.30)+0.05
    else:
        output_perc = ((soldiers_perc - (0.50)) * (0.01 - 0.02) / 0.50) + 0.02
    return output_perc+0.15


# function to compute Ks
def computeKs(N_soldiers,N_workers,N_egg):

    soldiers_perc = N_soldiers/(N_soldiers+N_workers)
    future_soldiers_perc = getPercFromSaturation(soldiers_perc)

    soldiers_req = (future_soldiers_perc*(N_soldiers+N_workers))-N_soldiers

    if soldiers_req <0:
        return 0;
    if soldiers_req <= N_egg:
        return soldiers_req/N_egg
    else:
        return 1


# calculates the number of eggs over the length of the simulation in days.
def incumbent():

    global N_egg
    global N_workers
    global N_soldiers
    global eggArr
    global soldierArr
    global workerArr
    global soldierPercArr


    # run the model for 1000 days
    for time in range(0, days):

        # computes Ks and Kw
        # Ks is the percentage of eggs that are converted to soldiers
        Ks = computeKs(N_soldiers,N_workers,N_egg)
        # Kw is the percentage of eggs that are converted to workers
        Kw = 1-Ks

        # worker update
        idx=(time/season_timespan_workers)%len(U_workers)
        N_workers = N_workers * (1.0 - random.uniform(U_workers[idx][0], U_workers[idx][1])) + Kw * N_egg
        #N_workers = N_workers * (1.0 - (U_workers[idx], U_workers[idx])) + Kw * N_egg

        workerArr.append(N_workers)

        # soldier update
        idx=(time/season_timespan_soldiers)%len(U_soldiers)
        N_soldiers = N_soldiers * (1.0 - random.uniform(U_soldiers[idx][0],U_soldiers[idx][1])) + Ks * N_egg
        soldierArr.append(N_soldiers)

        soldierPercArr.append((N_soldiers/(N_soldiers+N_workers))*100)

        # egg update
        idx=(time/season_timespan_eggs)%len(U_egg)
        N_egg = N_egg * (1.0 - random.uniform(U_egg[idx][0],U_egg[idx][1])) + K_egg
        eggArr.append(N_egg)  # fills the array eggArr=[]
    return


incumbent()

plot_elements(eggArr, "eggs",1, 'y' )
plt.savefig('eggs_plot.png', format='png', dpi=400,)

plot_elements(soldierArr, "soldiers",2,'r')
plt.savefig('soldiers_plot.png', format='png', dpi=400)

plot_elements(workerArr, "workers",3,'b')
plt.savefig('workers_plot.png', format='png', dpi=400)

plot_elements(soldierPercArr,"soldier_percentage",4,'g')
plt.savefig('soldier_perc_plot.png', format='png', dpi=400)

plt.show()