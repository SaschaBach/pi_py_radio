from spidev import SpiDev
from myLogger import MyLogger

class MCP3008Controller(object):
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()
        self.spi.max_speed_hz = 1000000 # 1MHz
        self.myLogger = MyLogger(self.__class__.__name__)
        self.myLogger.info('Init MCP3008')
 
    def open(self):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 1000000 # 1MHz
    
    def read(self, channel = 7):
        cmd1 = 4 | 2 | (( channel & 4) >> 2)
        cmd2 = (channel & 3) << 6
 
        adc = self.spi.xfer2([cmd1, cmd2, 0])
        self.myLogger.debug("Read SPI: %s" % adc)

        data = ((adc[1] & 15) << 8) + adc[2]
        return data
            
    def close(self):
        self.spi.close()