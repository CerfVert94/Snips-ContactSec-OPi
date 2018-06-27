#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from pyA20.gpio import gpio
from pyA20.gpio import port

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):

	probability = intent_message.intent.probability
	intentName = intent_message.intent.intent_name	
	
	gpio.init()
	gpio.setcfg(port.PA12, gpio.OUTPUT)

	
	gpio_pin = os.open("/home/pi/log.txt",os.O_WRONLY)
	if intentName == 'Roqyun:Allumage' :
		if probability > 0.9 :
			gpio.output(port.PA12, gpio.HIGH)
			sentence = "J allume la lumiere"
		else :
			sentence = " Je n'ai pas compris"
	elif 	intentName == 'Roqyun:Extinction' :
		if probability > 0.9 :
			gpio.output(port.PA12, gpio.LOW)
			sentence = "Je eteins la lumiere"
		else :
			sentence = " Je n'ai pas compris"		
	else :
		sentence = " Je n'ai pas compris"
			

	hermes.publish_end_session(intent_message.session_id, sentence)
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()