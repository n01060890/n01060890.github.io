#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import Adafruit_DHT
from subprocess import call

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin1 = 19
temp = 0
hum = 0
temp_list = []
hum_list = []
fail = 0

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity1, temperature1 = Adafruit_DHT.read_retry(sensor, pin1)
humidity2, temperature2 = Adafruit_DHT.read_retry(sensor, pin2)
humidity3, temperature3 = Adafruit_DHT.read_retry(sensor, pin3)
humidity4, temperature4 = Adafruit_DHT.read_retry(sensor, pin4)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity1 is not None and temperature1 is not None:
    #print('1st: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature1, humidity1))
    temp_list.append(temperature1)
    hum_list.append(humidity1)
else:
    #print('Failed to get first readings. Try again!')
    fail = 1
if humidity2 is not None and temperature2 is not None:
    #print('2nd: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature2, humidity2))
    temp_list.append(temperature2)
    hum_list.append(humidity2)
else:
    #print('Failed to get second readings. Try again!')
    fail = 1

if humidity3 is not None and temperature3 is not None:
    #print('3rd: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature3, humidity3))
    temp_list.append(temperature3)
    hum_list.append(humidity3)
else:
    #print('Failed to get third readings. Try again!')
    fail = 1

if humidity4 is not None and temperature4 is not None:
    #print('4th: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature4, humidity4))
    temp_list.append(temperature4)
    hum_list.append(humidity4)
else:
    #print('Failed to get fourth readings. Try again!')
    fail = 1

if fail != 1:
    temp = (temp_list[0] + temp_list[1] + temp_list[2] + temp_list[3])/4
    hum = (hum_list[0] + hum_list[1] + hum_list[2] + hum_list[3])/4
    print('{0:0.1f},{1:0.1f}'.format(temp, hum))
    
    


    
    
