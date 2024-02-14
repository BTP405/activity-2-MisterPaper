import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

def graphSnowfall(t):
    values = [0, 0, 0, 0, 0]
    file = open (t, "r")
    content = file.readline()
    while(content):
        if(int(content) <= 10):
            values[0]+=1
        elif(int(content) <= 20):
            values[1]+=1
        elif(int(content) <= 30):
            values[2]+=1
        elif(int(content) <= 40):
            values[3]+=1
        else:
            values[4]+=1
        content = file.readline()
    return values

plt.style.use('_mpl-gallery')

# make data:
x = 0.5 + np.arange(5)
y = graphSnowfall("python.txt")

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 5), xticks=np.arange(1, 5),
       ylim=(0, 5), yticks=np.arange(1, 5))

plt.show()
