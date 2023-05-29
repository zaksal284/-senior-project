import spidev

spi=spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz=1000000
def read_adc(vol):
        adc=spi.xfer2([1,(8+vol)<<4,0])
        data=((adc[1]&3)<<8)+adc[2]
        return data
