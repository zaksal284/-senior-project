import serial
import tts
import hx711

def read_serial_data():
    ser = serial.Serial()
    ser.port = '/dev/ttyACM0'  # 실제 시리얼 포트에 맞게 수정
    ser.baudrate = 9600
    ser.timeout = 1
    ser.open()  # 시리얼 포트 열기

    while True:
        if ser.isOpen() and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if line.strip():
                try:
                    val = float(line)
                    print(val)
                    if val > 100:
                        tts.twopeople()
                except ValueError:
                    print("유효하지 않은 값입니다.")

    ser.close()

read_serial_data()
