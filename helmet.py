import time
import spidev
import signal
import sys
import control



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
        '''
        if data >=100:
            break
        if count==20:
            sys.exit()
        if count>=10:
            control.helmet()
        count+=1
        '''
        print(data)
        time.sleep(1)
        

#헬멧착용
def continuation(vol):
	adc=spi.xfer2([1,(8+vol)<<4,0])
	data=((adc[1]&3)<<8)+adc[2]
	while True:
		if data >=1000:
			break
		if count==20:
			sys.exit()
		if count>=10:
			control.helmet()
		count+=1
  
		time.sleep(1)
