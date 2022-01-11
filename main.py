"""!
@file main.py
This file contains all the funcitons for dimming an LED
using a PWM wave 
@author Lucas Sandsor
@author Jack Barone
@author Jackson Myers
@date 04-Jan-2022 
"""
import motorDriver
import encoderDriver
import time

def led_setup():
    """!
    Sets pin A0 on the Nucleo board to an active output pin.
    It then sets the timer pin A0 uses to a frequnecy
    of 2000Hz. We then enable the channel for pin A0 to use
    PWM and invert it so that the brightness is max at duty
    @returns The channel to use for brightness    
    """
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=2000)
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    return ch1

def led_brightness(ch1, bright):
    """!
    Changes the duty cycle (brightness) of the PWM wave.
    @param ch1    The correct channel
    @param bright    The duty cycle (brightness) of the PWM wave
    """
    ch1.pulse_width_percent (bright)
    
if __name__ == "__main__":
    '''#An infinite loop
    while(1):
        #A cycle of decreasing brightness
        brightness = 0
        for brightness in range(100):
            led_brightness(led_setup(), brightness)
            #A delay of 50 to make the loop take 5 seconds
            pyb.delay(50)'''
    moe = motorDriver.MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    enc = encoderDriver.EncoderDriver(pyb.Pin.board.PB6,pyb.Pin.board.PB7, 4)
    while(1):
        moe.set_duty_cycle(-25)
        pyb.delay(100)
        moe.set_duty_cycle(0)
        enc.read()
        pyb.delay(50)        


