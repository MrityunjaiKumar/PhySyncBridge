from phySyncFirmata.phyCom.peripherals import Version1_pinouts as pins
from graphWindow import RealtimePlotWindow

from phySyncFirmata import ArduinoNano
import math
'''This function will print all the peripheral pinouts'''
#pins.print_pinouts()

'''Get the pin number for respective peripherals'''
#print(pins.Ac_relay)


def steinhart_temperature_C(r, Ro=10000.0, To=25.0, beta=3950.0):
    import math
    steinhart = math.log(r / Ro) / beta      # log(R/Ro) / beta
    steinhart += 1.0 / (To + 273.15)         # log(R/Ro) / beta + 1/To
    steinhart = (1.0 / steinhart) - 273.15   # Invert, convert to C
    return steinhart


board = ArduinoNano('COM5')

# Create an instance of an animated scrolling window
# To plot more channels just create more instances and add callback handlers below
realtimePlotWindow = RealtimePlotWindow()

# sampling rate: 1000Hz
samplingRate = 20

# called for every new sample which has arrived from the Arduino
def callBack(data):
    # send the sample to the plotwindow
    R = 10000 / (1.0/data - 1)
    # print(steinhart_temperature_C(R))

    realtimePlotWindow.addData(data,steinhart_temperature_C(R))

# Set the sampling rate in the Arduino
board.samplingOn(1000 / samplingRate)

# Register the callback which adds the data to the animated plot
board.analog[pins.Thermistor_1].register_callback(callBack)

# Enable the callback
board.analog[pins.Thermistor_1].enable_reporting()
realtimePlotWindow.show()
