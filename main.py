from machine import ADC, Pin, PWM
import time
import math
import utime

red = Pin(20, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)
micpin = ADC(Pin(26))
pwmred = PWM(red)
pwmyellow = PWM(yellow)
pwmgreen = PWM(green)
pwmred.freq(1000)
pwmyellow.freq(1000)
pwmgreen.freq(1000)
scaling = 65535
button1 = Pin(13, Pin.IN, Pin.PULL_UP)

def led(color):
    color.value(1)
    
def ledoff(color):
    color.value(0)

def mic():
    prevb = 0
    prevs = 1000000
    for i in range(100):
        value = micpin.read_u16()
        if value > prevb:
            prevb = value
        if value < prevs:
            prevs = value
    return prevb - prevs

def twosecsample():
    start_time = time.ticks_ms()
    samples = ""
    elapsed_time = 0
    while elapsed_time < 2000:
        elapsed_time = time.ticks_diff(time.ticks_ms(), start_time)
        samples.join(micpin.read_u16())
        time.sleep_us(144)
    return samples
        
    
    #micvalue = int(mic())
    #print(micvalue)
    #pwmred.duty_u16(max(0,65535-5*abs(micvalue-40000)))
    #pwmyellow.duty_u16(max(0,65535-5*abs(micvalue-30000)))
    #pwmgreen.duty_u16(max(0,65535-5*abs(micvalue-20000)))
    #time.sleep_ms(100)
def button_press(button):
    if not button.value():  # Button pressed (value is low)
        return True
    else:
        return False
    utime.sleep_ms(0.1)

while True:
    if button_press(button1):
        audiosample = twosecsample()
        print(audiosample)
    else:
        pass