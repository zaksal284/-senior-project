import spidev
import signal
import sys
import time
import numpy as np
#헬멧 및 조이스틱 초기설정 
spi=spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz=1000000

def map_range(x, in_min, in_max, out_min, out_max):
    return np.interp(x, (in_min, in_max), (out_min, out_max))
                     
def read_adc(vol):
        adc=spi.xfer2([1,(8+vol)<<4,0])
        data=((adc[1]&3)<<8)+adc[2]
        pwmdata=map_range(data,512,1024,0,100)
        return pwmdata

def joytick_read():
        y = read_adc(7)
        print(y)
        return y