#!/bin/sh
echo '12' | sudo tee /sys/class/gpio/export
echo 'out' | sudo tee /sys/class/gpio/gpio12/direction
echo '1' | sudo tee /sys/class/gpio/gpio12/value
echo '12' | sudo tee /sys/class/gpio/unexport
