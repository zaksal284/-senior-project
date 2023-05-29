import time
import spidev
import sys
import tts


count =0
#헬멧 및 조이스틱 초기설정 
spi=spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz=1000000

def ReadVol(vol):
    global count
    while True:
        adc=spi.xfer2([1,(8+vol)<<4,0])
        data=((adc[1]&3)<<8)+adc[2]
        if data >=100:
            break
        if count==20:
            sys.exit()
        if count>=10:
            tts.helmet()
        time.sleep(1)
        count+=1

