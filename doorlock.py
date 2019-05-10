#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

redled = 7
greenled = 8

GPIO.setup(redled,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(greenled,GPIO.OUT,initial=GPIO.LOW)

reader = SimpleMFRC522()

while True:
    id, text= reader.read()
    print("id: " + str(id))
    print("Text: "+ text)
    if id==108374469526:
        print("Acces Granted")
#        GPIO.output(greenled,GPIO.HIGH)
    else:
        print("sorry ask the owner for the correct card")
#        GPIO.output(redled,GPIO.HIGH)

    sleep(3)
    GPIO.output(greenled,GPIO.LOW)
    GPIO.output(redled,GPIO.LOW)
