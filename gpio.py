def gpio_export(gpio_pin_num) :
	gpio = open("/sys/class/gpio/export","w")
	gpio.write(str(gpio_pin_num))
	gpio.close()
	gpio = open("/sys/class/gpio/gpio"+ str(gpio_pin_num) +"/direction","w")
	gpio.write('out')
	gpio.close()
	
def gpio_unexport(gpio_pin_num) : 
	gpio = open("/sys/class/gpio/unexport", "w")
	gpio.write(str(gpio_pin_num))
	gpio.close()
	
def gpio_on(gpio_pin_num) :
	gpio_export(gpio_pin_num)
	gpio = open("/sys/class/gpio/gpio"+ str(gpio_pin_num) +"/value","w")
	gpio.write(str(1))
	gpio.close()
	gpio_unexport(gpio_pin_num)
	
def gpio_off(gpio_pin_num) :
	gpio_export(gpio_pin_num)
	gpio = open("/sys/class/gpio/gpio"+ str(gpio_pin_num) +"/value","w")
	gpio.write(str(0))
	gpio.close()
	gpio_unexport(gpio_pin_num)