import spidev

spi=spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz=1000000
def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def read_adc(vol):
    adc = spi.xfer2([1, (8 + vol) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    pwmdata = map_range(data, 325, 0, 0, 100)
    pwmdata = max(0, min(100, pwmdata))  # 값의 범위를 0과 100 사이로 제한
    return pwmdata
