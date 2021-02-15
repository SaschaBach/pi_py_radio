#Kommentar 1
test=5
test2=7
print(test)
test3=test+test2
print(test3)
print("Test via SSH")

from radiosender import Radiosender
from radiosenderSwitch import RadiosenderSwitch
import time

#radioBob=Radiosender('http://streams.radiobob.de/bob-live/mp3-192/mediaplayer','RadioBob')
#radioBob.play()
#time.sleep(10)
#radioBob.stop
#time.sleep(10)
radiosenderSwitch = RadiosenderSwitch()
#radiosender = radiosenderSwitch.get_radiosender('RadioBob') 
#radiosender.play()
#time.sleep(10)
#radiosender.stop()
#time.sleep(10)
radiosender2 = radiosenderSwitch.get_radiosender(radiosenderSwitch.radioBob) 
radiosender2.play()
time.sleep(20)
radiosender2.stop()
time.sleep(20)