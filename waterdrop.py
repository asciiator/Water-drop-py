import sys
import RPi.GPIO as GPIO
import os, time
if (sys.version_info > (3, 0)):
	import urllib.request as ulib
else:
	import urllib2 as ulib
import netifaces as ni

k=float(input("Enter the time between detection and taking the shot"))
RECEIVER_PIN = 23

def callback_func(channel):
    if GPIO.input(channel):
        print("Detection happened!")
	take_photo(k, ipaddresse)

def take_photo(k, ipaddresse):
	#take a picture
        url2="http://"+ipaddresse+"/cam.cgi?mode=camcmd&value=capture"
        print(url2)
        time.sleep(k)
        foto=ulib.urlopen(url2)
        html2=foto.read()
        
def switch_on_the_camera():
	#get ip address of cam
        #it is the the same ip as your wlan iface except the last section is a 1
        ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        listip=ip.split(".")
        listip[3]="1"
        ipaddresse= ".".join(listip)
        #start cam
        url="http://"+ipaddresse+"/cam.cgi?mode=camcmd&value=recmode"
        print(url)
        response1 = ulib.urlopen(url)
        html=response1.read()
	return ipaddresse

if __name__ == '__main__':
	ipaddresse = switch_on_the_camera()
	GPIO.setmode(GPIO.BCM)
    	GPIO.setwarnings(False)
   	GPIO.setup(RECEIVER_PIN, GPIO.IN)
   	GPIO.add_event_detect(RECEIVER_PIN, GPIO.BOTH, callback=callback_func, bouncetime=200)

    	try:
        	while True:
            		time.sleep(0.05)
    	except:
        	# delete event via:
        	GPIO.remove_event_detect(RECEIVER_PIN)
