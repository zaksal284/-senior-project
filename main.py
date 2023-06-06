import multiprocessing
import RPi.GPIO as GPIO
import time
import helmet
import joystick
import motor
import cv2
import deletefile
import sys
import signal
import motor
import blackbox
import handle
import loadcell
import servo
time.sleep(1)

# GPIO 핀 번호 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

reader = loadcell.SerialReader()
reader.set_serial()

led_leftpin = 12
led_rightpin = 6

# 버튼과 LED의 핀 번호 설정
leftbutton = 18

rightbutton = 23

bothbutton=24

start_button=22

detect_left = False
detect_right = False
detect_both = False
start= multiprocessing.Value("b",False)


GPIO.remove_event_detect(leftbutton)  # 기존 이벤트 감지 제거
GPIO.remove_event_detect(bothbutton)  # 기존 이벤트 감지 제거
GPIO.remove_event_detect(rightbutton)  # 기존 이벤트 감지 제거
GPIO.remove_event_detect(start_button) 
# 버튼 핀의 입력 설정
GPIO.setup(leftbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bothbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(start_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
    start.value = not start.value

    

GPIO.add_event_detect(leftbutton, GPIO.FALLING, callback=button_left_callback, bouncetime=100)
GPIO.add_event_detect(start_button, GPIO.FALLING, callback=button_start_callback, bouncetime=200)
GPIO.add_event_detect(bothbutton, GPIO.FALLING, callback=button_both_callback, bouncetime=100)
GPIO.add_event_detect(rightbutton, GPIO.FALLING, callback=button_right_callback, bouncetime=100)



while True:
    print("시작")
    if start.value:
        break
    pass

helmet.ReadVol(0)

reader.read_serial_data()

servo.serct2()

time.sleep(1)

def main(start):
    global detect_left
    global detect_both
    global detect_right
    while True:
        motor.motor_control()
        if detect_both == True:
            GPIO.output(led_leftpin, GPIO.HIGH)
            GPIO.output(led_rightpin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_leftpin, GPIO.LOW)
            GPIO.output(led_rightpin, GPIO.LOW)
            time.sleep(0.5)
            
        if detect_left == True:
            GPIO.output(led_leftpin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_leftpin, GPIO.LOW)
            time.sleep(0.5)
            if handle.read_adc(3)>650:  #값변경 필요
                detect_left= not detect_left
 
        if detect_right == True:
            GPIO.output(led_rightpin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_rightpin, GPIO.LOW)
            time.sleep(0.5)
            if handle.read_adc(3)<410:   #값변경 필요
                detect_right= not detect_right
                
        if start.value == False:
            servo.serct()
            motor.pwm1.stop()
            motor.pwm2.stop()
            GPIO.cleanup()
            multi.join()
            sys.exit()
 

          



if __name__ == "__main__":
    multi = multiprocessing.Process(target=blackbox.cctv, args=(start,))
    multi.start()
    main(start)
