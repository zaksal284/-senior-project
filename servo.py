import RPi.GPIO as GPIO
import time

# GPIO Servo모터 제어

servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50) # 50Hz( 서보모터 PWM 동작을 위한 주파수 )
pwm.start(0) # 서보모터의 0도 위치( 0.6ms ) 이동: 값 3.0은 pwm 주기인 20ms 의 3% 를 의미

def serct():
    pwm.ChangeDutyCycle(3.0) # 0도
    time.sleep(0.5)
    pwm.stop()
    
def serct2():
    pwm.ChangeDutyCycle(7.5) # 90도
    time.sleep(0.5)
    
