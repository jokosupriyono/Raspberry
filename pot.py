from gpiozero import MCP3008
from time import sleep

pot1 = MCP3008(0)
pot2 = MCP3008(1)
pot3 = MCP3008(2)
pot4 = MCP3008(3)

while True:
    print("Pot1:{:.2f} Pot2:{:.2f} Pot3:{:.2f} Pot4:{:.2f}".format(pot1.value,pot2.value,pot3.value,pot4.value))
    sleep(1.0)
        
