#!/usr/bin/env python2
import os, time
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

gpio_path = "/sys/class/gpio"

def gpio_config(gpio_pin_num) :
	if os.access(gpio_path + "/export", os.W_OK):
		gpio_pin = os.open(gpio_path + "/export", os.O_WRONLY)
		os.write(gpio_pin, str(gpio_pin_num))
		os.close(gpio_pin)
	time.sleep(0.05)
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/direction", os.W_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/direction",os.O_WRONLY)
		os.write(gpio_pin, 'out')
		os.close(gpio_pin)
def gpio_unexport(gpio_pin_num) : 
	if os.access(gpio_path + "/unexport", os.W_OK):
		gpio_pin = os.open(gpio_path + "/unexport", os.O_WRONLY)
		os.write(gpio_pin, str(gpio_pin_num))
		os.close(gpio_pin)

def gpio_on(gpio_pin_num) :
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/value", os.W_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/value",os.O_WRONLY)
		os.write(gpio_pin, '1')
		os.close(gpio_pin)

def gpio_off(gpio_pin_num) :
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/value", os.W_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/value",os.O_WRONLY)
		os.write(gpio_pin, '0')
		os.close(gpio_pin)

def intent_received(hermes, intent_message):

	probability = intent_message.intent.probability
	intentName = intent_message.intent.intent_name

	gpio_pin_num = 12
	gpio_config(12)

	if intentName == 'Roqyun:Allumage' :
		if probability > 0.9 :
			gpio_on(12)
			sentence = "J allume la lumiere"
		else :
			sentence = " Je n'ai pas compris"
	elif 	intentName == 'Roqyun:Extinction' :
		if probability > 0.9 :
			gpio_off(12)
			sentence = "Je eteins la lumiere"
		else :
			sentence = " Je n'ai pas compris"
	else :
		sentence = " Je n'ai pas compris"
	gpio_unexport(12)
	hermes.publish_end_session(intent_message.session_id, sentence)
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
