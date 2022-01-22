"""!
@file main.py
This file contains all the funcitons for controlling
motor speed and couting revolutions via an encoder
attatched to the motor
@author Lucas Sandsor
@author Jack Barone
@author Jackson Myers
@date 10-Jan-2022 
"""
import motorDriver
import encoderDriver
import pyb
import time

   
if __name__ == "__main__":
    '''!
    
    '''
    moe = motorDriver.MotorDriver(pyb.Pin.board.PA10,
        pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    '''To get the motor to start to move the minumum duty cycle is 25 in either
    direction but to keep it moving once started, the minimum duty cycle is
    18'''
    enc = encoderDriver.EncoderDriver(pyb.Pin.board.PB6,pyb.Pin.board.PB7, 4)
    while(1):
        #An infinite loop to see it go back and forth for testing
        moe.set_duty_cycle(-25)
        pyb.delay(1000)
        moe.set_duty_cycle(25)
        pyb.delay(1000)
        moe.set_duty_cycle(0)
        enc.read()     


