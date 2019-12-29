"""
oscilloscope
==================================

This oscilloscope example code grabs data from PhyCom and plot it in realTime

"""

from phySyncFirmata.phyCom.peripherals import Version1_pinouts as pins
from phySyncFirmata.phyCom.common_Utility import RealtimePlotWindow

from phySyncFirmata import ArduinoNano

'''This function will print all the peripheral pinouts'''
#pins.print_pinouts()

'''Get the pin number for respective peripherals'''
#print(pins.Ac_relay)

board = ArduinoNano('COM8')

# Create an instance of an animated scrolling window
# To plot more channels just create more instances and add callback handlers below
realtimePlotWindow = RealtimePlotWindow()

# sampling rate: 1000Hz
samplingRate = 100

# called for every new sample which has arrived from the Arduino
def callBack(data):
    # send the sample to the plotwindow
    realtimePlotWindow.addData(data)

# Set the sampling rate in the Arduino
board.samplingOn(1000 / samplingRate)

# Register the callback which adds the data to the animated plot
board.analog[pins.Pot_1].register_callback(callBack)

# Enable the callback
board.analog[pins.Pot_1].enable_reporting()
realtimePlotWindow.show()
