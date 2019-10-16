#  MBTechWorks.com 2016
#  Pulse Width Modulation (PWM) demo to cycle brightness of an LED

import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use 
                          # Broadcom SOC channel names.

ledPin = 37
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, GPIO.HIGH)
GPIO.setup(32, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(32, 10000)   # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(19, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm1 = GPIO.PWM(19, 10000) 

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=25                               # set dc variable to 0 for 0%
pwm.start(20)                      # Start PWM with 0% duty cycle
pwm1.start(75) 
time.sleep(2)                     # Start PWM with 0% duty cycle
pwm1.ChangeDutyCycle(20)                      # Start PWM with 0% duty cycle
pwm.ChangeDutyCycle(75)                      # 

try:
    
              # wait .05 seconds at current LED brightness
    while True:
      time.sleep(2)

      pwm.ChangeDutyCycle(20)                      # Start PWM with 0% duty cycle
      pwm1.ChangeDutyCycle(75)                      # Start PWM with 0% duty cycle
      time.sleep(2)
      pwm.ChangeDutyCycle(75)
      pwm1.ChangeDutyCycle(20)
    
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")
  
                      # 
pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode

