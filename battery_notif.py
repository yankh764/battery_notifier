#!/usr/bin/python
import psutil 
import time
from plyer import notification 

def get_battery_status():
	"""The function will gett the bettery percent, and power status"""
	battery = psutil.sensors_battery()
	#Power status
	power_status = battery.power_plugged
	#Battery percent
	percent = int(battery.percent)
	return power_status, percent


def send_battery_notifications():
	"""
	The function will send a system notification whenever the
	battery is below on 20% or 10% and unplugged from charger.
	"""
	while True:
		power_status, percent = get_battery_status()	
		if power_status == True:
			#Wait 30 min
			time.sleep(60*30)
			continue
		if percent > 40:
			#Wait 20 min 
			time.sleep(60*20)
			continue
		elif percent <= 40 and percent >= 30:
    			#Wait 5 min 
			time.sleep(60*5)
			continue
		elif percent < 30 and percent > 20:
			#Wait 2 min 
			time.sleep(60*2) 
		elif percent == 20:
			notification.notify( 
    				title="Warning:", 
    				message="20% battery remaining.", 
    				timeout=10
    				)
			#Wait 3 min 
			time.sleep(60*3)
			continue
		elif percent < 20 and percent > 10:
			#Wait 2 min 
			time.sleep(60*2)
			continue  
		elif percent == 10:
			notification.notify(
				title="Warning:",
				message="10% battery remaining.",
				timeout=10
				)
			#Wait 5 min 
			time.sleep(60*3)

send_battery_notifications()
