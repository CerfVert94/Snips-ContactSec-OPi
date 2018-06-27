#!/bin/sh
echo "Hello world"
echo '12' | sudo tee /sys/class/gpio/export
echo 'out' | sudo tee /sys/class/gpio/gpio12/directoin
echo '1' | sudo tee /sys/class/gpio/gpio12/value
echo '12' | sudo tee /sys/class/gpio/unexport