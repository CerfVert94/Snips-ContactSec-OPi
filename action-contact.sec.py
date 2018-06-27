#!/usr/bin/env python2
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def gpio_export(gpio_pin_num) :
	gpio_pin = open("/sys/class/gpio/export","w")
	gpio_pin.write(str(gpio_pin_num))
	gpio_pin.close()
	gpio_pin = open("/sys/class/gpio/gpio"+ str(gpio_pin_num) +"/direction","w")
	gpio_pin.write('out')
	gpio_pin.close()
	
def gpio_unexport(gpio_pin_num) : 
	gpio_pin = open("/sys/class/gpio/unexport", "w")
	gpio_pin.write(str(gpio_pin_num))
	gpio_pin.close()
	
def gpio_on(gpio_pin_num) :
	gpio_export(gpio_pin_num)
	gpio_pin = open("/sys/class/gpio/gpio"+ str(gpio_pin_num) +"/value","w")
	gpio_pin.write(str(1))
	gpio_pin.close()
	gpio_unexport(gpio_pin_num)
	
def gpio_off(gpio_pin_num) :
	gpio_export(gpio_pin_num)
	gpio_pin = open("/sys/class/gpio/gpio"+ str(gpio_pin_num) +"/value","w")
	gpio_pin.write(str(0))
	gpio_pin.close()
	gpio_unexport(gpio_pin_num)
def intent_received(hermes, intent_message):
	test(); 
	probability = intent_message.intent.probability
	intentName = intent_message.intent.intent_name	

	
	if intentName == 'Roqyun:Allumage' :
		if probability > 0.9 :
			sentence = "J allume la lumiere"
		else :
			sentence = " Je n'ai pas compris"
	elif intentName == 'Roqyun:Extinction' :
		if probability > 0.9 :
			sentence = "Je eteins la lumiere"
		else :
			sentence = " Je n'ai pas compris"
			
			

	hermes.publish_end_session(intent_message.session_id, sentence)
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()