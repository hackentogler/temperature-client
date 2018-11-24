from __future__ import division
import requests

# Enter path to sensor, will appear once you start the service in starttempdriver.sh
tfile = open("/sys/bus/w1/devices/28-000004a78d56/w1_slave")
text = tfile.read()
tfile.close()
secondline = text.split("\n")[1]
temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:])
temperature /= 1000

# Convert to Fahrenheit
temperature = (temperature * 1.8) + 32
unit = "F"

print str(temperature) + " " + unit

print "Logging to web service..."

url = 'https://hackentogler.com/templog/temperature.php'
data = '{"currTemp": "' + str(temperature) + '","unit": "' + unit + '"}'
response = requests.get(url, data=data)
print response.text

print "Done."
