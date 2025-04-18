# remote sensor
from microbit import *
import radio
radio.config(group=23)
radio.on()


while True:
    if button_a.was_pressed():    
 #      while True
        for x in range(5):
            display.clear()
            C = temperature()
            F = 32 + 9/5*C
            msg = str(C)
            radio.send(msg)
            display.scroll(msg)
            sleep(5)
    if button_b.was_pressed():  
        msg = ""
        radio.send(msg)