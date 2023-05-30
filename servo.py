import RPi.GPIO as GPIO
import time

servo_pin=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm=GPIO.PWM(servo_pin,50)
pwm.start(3.0)

time.sleep(0.2)
pwm.ChangeDutyCycle(7.5)

#pwm.stop()
#GPIO.celanup()
