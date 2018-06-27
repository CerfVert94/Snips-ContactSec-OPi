#!/usr/bin/env python2
import os
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):

	probability = intent_message.intent.probability
	intentName = intent_message.intent.intent_name	
	os.popen("echo '12' | sudo tee /sys/class/gpio/export", 'w')
	os.popen("echo 'out' | sudo tee /sys/class/gpio/gpio12/direction", 'w')
	
	
	if intentName == 'Roqyun:Allumage' :
		if probability > 0.9 :
			os.popen("echo '1' | sudo tee /sys/class/gpio/gpio12/value", 'w')
			sentence = "J allume la lumiere"
		else :
			sentence = " Je n'ai pas compris"
	elif 	intentName == 'Roqyun:Extinction' :
		if probability > 0.9 :
			os.popen("echo '0' | sudo tee /sys/class/gpio/gpio12/value", 'w')
			sentence = "Je eteins la lumiere"
		else :
			sentence = " Je n'ai pas compris"		
	else :
		sentence = " Je n'ai pas compris"
	#os.popen("echo '12' | sudo tee /sys/class/gpio/unexport", 'w')


	hermes.publish_end_session(intent_message.session_id, sentence)
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()