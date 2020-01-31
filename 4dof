import I2C_LCD_driver
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from time import sleep

mylcd = I2C_LCD_driver.lcd()

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

try:
  while True:
    adcPot = mcp.read_adc(0)
    voltage = adcPot * 0.00322
    mylcd.lcd_display_string("Pot:%.2fV " % voltage, 1)
    
    adcLm35 = mcp.read_adc(1)
    celsius = adcLm35 * 0.322
    mylcd.lcd_display_string("LM35:%.2f%sC" % (celsius, chr(223)), 2)
    
    sleep(0.5)


except KeyboardInterrupt:
    mylcd.lcd_clear()
