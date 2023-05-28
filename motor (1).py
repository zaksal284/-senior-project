import RPi.GPIO as GPIO
import time
import joystick
#import distance
#뫁머 작동
ENA = 13
ENB = 21
IN1 = 19
IN2 = 26
IN3 = 16
IN4 = 20
#모터l

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

# PWM 주파수 설정
pwm_freq = 1000
pwm1=GPIO.PWM(ENA,pwm_freq)
pwm2=GPIO.PWM(ENB,pwm_freq)
pwm2.start(0)
def motor_control():
        
        speed=joystick.joytick_read()
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
        pwm1.ChangeDutyCycle(speed)
        pwm2.ChangeDutyCycle(speed)
