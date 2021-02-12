#Kommentar 1
test=5
test2=7
print(test)
test3=test+test2
print(test3)
print("Test")

from radiosender import Radiosender

radioBob=Radiosender('http://streams.radio.de/bob-live/mp3-192/mediaplayer','RadioBob')
radioBob.play()