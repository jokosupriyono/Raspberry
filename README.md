# Raspberry
Robot 4 DOF

import RPi.GPIO as GPIO
import time
GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  input_value = GPIO.input(17)
  if input_value == False:
    print ("tombol ditekan")
    time.sleep(2)
   elif input_value == True:
    print ("tombol tidak ditekan")
    time.sleep(2)
    
 GPIO.cleanup()
