import multiprocessing
import RPi.GPIO as GPIO
import time
import helmet
import joystick
import motor
import tts
import cv2
import deletefile
import sys
import signal
import motor
import blackbox
import handle
import loadcell
time.sleep(1)

# GPIO 핀 번호 설정
GPIO.setmode(GPIO.BCM)

led_leftpin = 12
led_rightpin = 6

# 버튼과 LED의 핀 번호 설정
leftbutton = 18

rightbutton = 23

bothbutton=24

start_button=27

detect_left = False
detect_right = False
detect_both = False
start=False



# 버튼 핀의 입력 설정
GPIO.setup(leftbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bothbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(start_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# LED 핀의 출력 설정
GPIO.setup(led_leftpin, GPIO.OUT)
GPIO.setup(led_rightpin, GPIO.OUT)

# 버튼 인터럽트 처리 함수
def button_left_callback(channel):
    global detect_left
    detect_left = not detect_left

def button_right_callback(channel):
    global detect_right
    detect_right = not detect_right 

def button_both_callback(channel):
    global detect_both
    detect_both = not detect_both

def button_start_callback(channel):
    global start
    start = not start
    
# 이벤트 감지 등록
GPIO.add_event_detect(leftbutton, GPIO.FALLING, callback=button_left_callback, bouncetime=100)
GPIO.add_event_detect(start_button, GPIO.FALLING, callback=button_left_callback, bouncetime=100)
GPIO.add_event_detect(bothbutton, GPIO.FALLING, callback=button_both_callback, bouncetime=100)


GPIO.add_event_detect(rightbutton, GPIO.FALLING, callback=button_right_callback, bouncetime=100)


#if not start:
#    while True:
#        if start:
#            break
#        pass


def main():
    global detect_right
    global detect_left
    multi=multiprocessing.Process(target=blackbox.cctv)
    multi.start()
    while True:
        motor.motor_control()
        if detect_both == True:
            GPIO.output(led_leftpin, GPIO.HIGH)
            GPIO.output(led_rightpin, GPIO.HIGH)
            print("비상 깜빡이")
            time.sleep(0.5)
            GPIO.output(led_leftpin, GPIO.LOW)
            GPIO.output(led_rightpin, GPIO.LOW)
            time.sleep(0.5) 
            
        if detect_left == True:
            GPIO.output(led_leftpin, GPIO.HIGH)
            print("좌측 깜빡이")
            GPIO.output(led_leftpin, GPIO.LOW)
            if handle.steer()<380:
                detect_left= not detect_left
            time.sleep(0.5)
 
        if detect_right == True:
            GPIO.output(led_rightpin, GPIO.HIGH)
            print("우측 깜빡이")
            time.sleep(0.5)
            GPIO.output(led_rightpin, GPIO.LOW)
            time.sleep(0.5)
            if handle.steer()>480:
                detect_right= not detect_right
        if start_button == False: 
            GPIO.clean()
            motor.pwm1.stop()
            motor.pwm2.stop()
            multi.join()
            time.sleep(0.5)
            sys.exit()


if __name__ == "__main__":
    main()
