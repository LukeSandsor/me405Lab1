"""!
@file encoder.py
This file contains all driver functions for the encoder by scanning

@author Lucas Sandsor
@author Jack Barone
@author Jackson Myers
@date 10-Jan-2022 
"""
import pyb
class EncoderDriver:
    '''!
    This class impliments and encoder for ME405
    '''
    def __init__(self, in1pin, in2pin, timer):
        '''!
        Creates an encoder driver by initializing GPIO
        pins and reading signal output from two channels and comparing
        them to see what the direction of movement is
        @param in1pin    The input pin for one for one of the scanners
        on the encoder measuring ticks
        @param in2pin    The input pin for a different scanner seperated
        by a half cycle from the other encoder 
        @param timer     The timer on the STM32 that works in counter
        mode that allows us to track ticks for the encoder
        '''
        print("Creating an encoder driver")
        self.period = 4000 - 1
        self.pinIN1 = pyb.Pin (in1pin, pyb.Pin.IN)        
        self.pinIN2 = pyb.Pin (in2pin, pyb.Pin.IN)
        #must declare pyb.Pin.board.en_pin in main
        self.tim = pyb.Timer (timer, prescaler=0, freq=20000)
        self.ch1 = self.tim.channel (1, pyb.Timer.ENC_A, pin=self.pinIN1)
        self.ch2 = self.tim.channel (2, pyb.Timer.ENC_B, pin=self.pinIN2)
        self.count = 0
        self.lastCount = 0
        self.position = 0
        self.delta = 0

    def update(self):
        '''!
        Handles overflow for the counter by creating a differential
        between the last counted number and the counted number at
        run time. If there is overflow, the differential will be
        greater or less than the period (-self.period/2 to self.period/2
        is equals to one period) and the code will adjust the number
        '''
        self.count = self.tim.counter()
        self.delta = self.count - self.lastCount
        if self.delta > self.period/2:
            self.delta -= self.period
        elif self.delta < -self.period/2:
            self.delta += self.period
        else:
            pass
        self.position += self.delta
        self.lastCount = self.count
            
        
    def read(self):
        '''!
        Reads the current position of the motor using the
        past update function and then priting the value of the
        encoder to the user
        '''
        self.update()
        print("Printing Encoder Position: ", end="")
        print(self.position)
    
    def zero(self):
        '''!
        Resets the position of the encoder to zero
        '''
        print("Encoder Position reset to zero!")
        self.position = 0
        return 0
        

        