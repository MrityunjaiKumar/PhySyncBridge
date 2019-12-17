#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Creates a scrolling data display


class RealtimePlotWindow:

    def __init__(self):
        # create a plot window
        self.fig, self.ax = plt.subplots(figsize=(9, 5))
        self.fig.canvas.set_window_title('Using Steinhart Hart equation, to get temperature from resistance of thermistor (mapped to adc value).')
        self.fig.subplots_adjust(bottom=0.2) 
        # that's our plotbuffer
        self.plotbuffer = np.zeros(500)
        # create an empty line
        self.line, = self.ax.plot(self.plotbuffer,color='orange')
        # axis
        self.ax.set_ylim(0, 50)
        # That's our ringbuffer which accumluates the samples
        # It's emptied every time when the plot window below
        # does a repaint
        self.ringbuffer = []
        # start the animation
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100)
        self.ann1=plt.annotate("maximum", xy=(0, 0))
        self.ann2=plt.annotate("maximum", xy=(1, 0))
        self.ann3=plt.annotate("Maximum value", xy=(0, 0))
        self.ann4=plt.annotate("Minimum value", xy=(1, 0))
        self.lastest_raw_value=0
        self.proccesed_value=0
        self.max_value=0
        self.min_value=1000

    # updates the plot
    def update(self, data):
        # add new data to the buffer
        self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
        # only keep the 500 newest ones and discard the old ones
        self.plotbuffer = self.plotbuffer[-500:]
        self.ringbuffer = []
        # set the new 500 points of channel 9
        self.line.set_ydata(self.plotbuffer)
        
        self.ann1.remove()
        self.ann1=plt.annotate("Current adc data    = "+str(self.lastest_raw_value), xy=(250, 45))
        
        self.ann2.remove()
        self.ann2=plt.annotate("Current temperature = "+str('%.3f'%self.proccesed_value)+" ℃", xy=(250, 42),color='orange')
        # print("self.plotbuffer[499]\t"+str(self.plotbuffer[499])+"\t\t\tself.lastest_data\t"+str(self.lastest_raw_value))
        self.ann3.remove()
        self.ann3=plt.annotate("Maximum value = "+str('%.3f'%self.max_value)+" ℃", xy=(0, 45),color='red')
        
        self.ann4.remove()
        self.ann4=plt.annotate("Minimum value = "+str('%.3f'%self.min_value)+" ℃", xy=(0, 42),color='blue')
        return self.line

    # appends data to the ringbuffer
    def addData(self, raw_value, proccesed_value):
        self.ringbuffer.append(proccesed_value)
        self.lastest_raw_value=raw_value
        self.proccesed_value=proccesed_value
        if(proccesed_value<self.min_value):
            self.min_value=proccesed_value
        if(proccesed_value>self.max_value):
            self.max_value=proccesed_value
        

    def show(self):
        # show the plot and start the animation
        plt.xlabel('Real time samples \n\n Using Steinhart Hart equation, to get temperature from resistance of thermistor (mapped to adc value).')
        plt.ylabel('Temperature')
        plt.grid()
        plt.show()

    def getFigure(self):
        return self.fig

    def getAx(self):
        return self.ax
