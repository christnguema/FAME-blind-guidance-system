import pyb
import time

from pyb import LED

class LEDManager():
    def __init__(self):
        self.led1 = pyb.LED(1)
        self.led2 = pyb.LED(2)
        self.led3 = pyb.LED(3)
    
    def set_led_blue_on(self):
        self.led1.on()
    
    def set_led_blue_off(self):
        self.led1.off()
        
    def toggle_led_blue(self):
        self.led1.toggle()
    
    def set_led_green_on(self):
        self.led2.on()
        
    def set_led_green_off(self):
        self.led2.off()

    def toggle_led_green(self):
        self.led2.toggle()
        
    def set_led_red_on(self):
        self.led3.on()
        
    def set_led_red_off(self):
        self.led3.off()
        
    def toggle_led_red(self):
        self.led3.toggle()
        
    
    def chenillard(self) :

        self.led1.on()
        self.led2.off()
        self.led3.off()
        time.sleep(0.4)
        
        self.led1.off()
        self.led2.on()
        self.led3.off()
        time.sleep(0.4)
        
        self.led1.off()
        self.led2.off()
        self.led3.on()
        time.sleep(0.4)
        
        self.led3.off()

    def led_blink(self, freq_hz=4) :
        sleep_period = 1 / freq_hz
        # extinction de toutes les LEDs ---
        self.led1.off()
        self.led2.off()
        self.led3.off()
        time.sleep(0.1)
        # ---------------------------------
        
        # premiere allumage ---
        self.led1.on()
        self.led2.on()
        self.led3.on()
        time.sleep(sleep_period)
        self.led1.off()
        self.led2.off()
        self.led3.off()
        time.sleep(0.1)
        # --------------------
        
        # second allumage ---
        self.led1.on()
        self.led2.on()
        self.led3.on()
        time.sleep(sleep_period)
        self.led1.off()
        self.led2.off()
        self.led3.off()
        time.sleep(0.1)
        # --------------------
        
        # troisieme allumage ---
        self.led1.on()
        self.led2.on()
        self.led3.on()
        time.sleep(sleep_period)
        self.led1.off()
        self.led2.off()
        self.led3.off()
        # --------------------

        