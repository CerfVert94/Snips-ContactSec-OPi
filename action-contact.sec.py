#!/usr/bin/env python2
import OPiGPIO
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
	"""
	Executes the action prompted by a vocal command.
	The vocal command is analysed and passed as an argument (intent_message)
	
	"""
	# intentName : the name of "intention" supposedly meant by vocal command (chosen by NLU)
	intentName = intent_message.intent.intent_name
	# Probability : the match in percentage between the vocal command and the "intention" chosen by NLU.
	probability = intent_message.intent.probability

	gpio_pin_num = 12
	OPiGPIO.gpio_config(gpio_pin_num)

	# Probability thresold should reach 0.9. Otherwise, it's an unknown command
	if intentName == 'Roqyun:Allumage' :
		if probability > 0.9 :
			OPiGPIO.gpio_on(gpio_pin_num)
			sentence = "J allume la lumiere"
		else :
			sentence = " Je n'ai pas compris"
	elif intentName == 'Roqyun:Extinction' :
		# Probability thresold should reach 0.9. Otherwise, it's an unknown command
		if probability > 0.9 :
			OPiGPIO.gpio_off(gpio_pin_num)
			sentence = "Je eteins la lumiere"
		else :
			sentence = " Je n'ai pas compris"
	else :
		sentence = " Je n'ai pas compris"
	OPiGPIO.gpio_unexport(gpio_pin_num)
	hermes.publish_end_session(intent_message.session_id, sentence)
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
