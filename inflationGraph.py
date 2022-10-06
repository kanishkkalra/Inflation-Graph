# Name - Kanishk Kalra
# C# - C0832722

import numpy as np
import csv  
import matplotlib.pyplot as plt
from numpy import random
from matplotlib.animation import FuncAnimation

#Setting the per page year display to 30
limit = 30

# Declaring lists to to used to display data
x_data = []
y_data = []

# Declaring lists to store data to be diaplyed
x = []
y = []

# Generating random data and storing in x and y lists
for i in range(1900,2023):
    x.append(i)
    y.append(str(round(random.uniform(-0.36,13.55),1)))

# Writing the x and y lists to inflation.csv file
with open('inflation.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # Looping through x and y list
    for i in range(len(y)):
        text = x[i],y[i] # Appending each value of x and y with a comma in between
        writer.writerow(text) # Writing each appended value to file

# Clearing teh data from x and y lists after written in file
x.clear()
y.clear()

# Reading data from inflation.csv file
with open('inflation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # Setting delimiter as a comma
    for row in csv_reader:
        # Reading add data in 1st column (year) to list x and 2nd column (inflation rate) to list y
        x.append(int(row[0])) # Data is returned in string and converted to int for x list and float for y string
        y.append(float(row[1]))

fig,ax = plt.subplots()
# Setting x axis and y axis limits
ax.set_xlim(1900,1930)
ax.set_ylim(-2,16)
# Setting title of the plot
ax.set_title('Inflation rate from the year 1900 to 2022')
# Setting labels of the axis and displayin max and min value from the list
plt.xlabel("Year - From 1900 to 1930")
plt.ylabel("Infaltion Rate\nMaximum - "+str(max(y))+" | Minimum - "+str(min(y)))

line, = ax.plot(0,0)


# Animation frame method to be called from funcAnimation method
def animation_frame(i):
    global limit # Setting limit method as global

    # Called when the entire x list has been iterated i.e the year has been reached to 2022
    if(i == len(x)-1) :
        
        limit=30 # limit se set back to 30
        ax.set_xlim(1900,1930) # Axis limits are reset i.e set to 1900 to 1930
        plt.xlabel("Year - From 1900 to 1930") # Label is reset
        # Appending data to x_data and y_data list from x and y list
        x_data.append(x[i])
        y_data.append(float(y[i]))
        # Shwoing line on graph
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        # Clearing the lists
        x_data.clear()
        y_data.clear()
    
    # Called when limit has been reached
    elif(i == limit):
        # Data is appended to list
        x_data.append(x[i])
        y_data.append(float(y[i]))
        # Showing data on line
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        # Setting axis limits to the current year and current year + 30 year
        ax.set_xlim(x[i],x[i]+30)
        # Updating the label of x axis to show the year range being shown
        plt.xlabel("Year - From "+str(x[i])+" to "+str(x[i]+30))
        # Increasing the limit to do 30 more years
        limit = limit+30
        # Clearing the lists
        x_data.clear()
        y_data.clear()
        # Adding new data to lists after being cleared
        x_data.append(x[i])
        y_data.append(float(y[i]))
        # Showing the data from teh lists
        line.set_xdata(x_data)
        line.set_ydata(y_data)
    
    else :
        # Adding data to the list
        x_data.append(x[i])
        y_data.append(float(y[i]))
        # Showing the lines on the graph
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        # Returning line
    return line,

# Calling the funcAnimation method with the arguments:
# figure, 
# animation frame method that is called repeatedly, 
# arange method from numpy sets the range of i in animation_frame method from 0 to 123 with an gap of 1 
# Setting time interval to 150 miliseconds
animation = FuncAnimation(fig, func=animation_frame,frames=np.arange(0,123,1), interval=150)
# SUMMARIZING FUNCANIMATION METHOD
# The above method calls animation_frame method after every 150 miliseconds interval
# and the i in animation_frame is added by 1 on each interval starting from 0 till 123(123 not included)

# Showing the plot
plt.show()