import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_list = (16, 18, 22)
motor = pin_list
for pin in pin_list:
    GPIO.setup(pin, GPIO.OUT)

print 'Going forwards'
GPIO.output(motor[0], GPIO.HIGH)
GPIO.output(motor[1], GPIO.LOW)
GPIO.output(motor[2], GPIO.HIGH)

sleep(2)

print 'Going backwards'
GPIO.output(motor[0], GPIO.LOW)
GPIO.output(motor[1], GPIO.HIGH)
GPIO.output(motor[2], GPIO.HIGH)

sleep(2)

print 'Now stop'

GPIO.output(motor[2], GPIO.LOW)

GPIO.cleanup()
