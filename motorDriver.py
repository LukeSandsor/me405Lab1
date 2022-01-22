import pyb
class MotorDriver:
    '''!
    This class impliments a motor driver for ME405
    '''
    def __init__ (self, en_pin, in1pin, in2pin, timer):
        '''!
        Creates a motor driver by initializing GPIO
        pins and turning motor off
        @param en_pin    The enable pin for driving the motor
        @param in1pin    The input pin for the motor to spin forwards
        @param in2pin    The input pin for the motor to spin backwards
        @param timer    The timer whose channels we use for controlling the motor
        '''
        print("Creating a motor driver")
        self.pinEN = pyb.Pin (en_pin, pyb.Pin.OUT_PP)
        self.pinIN1 = pyb.Pin (in1pin, pyb.Pin.OUT_PP)
        self.pinIN2 = pyb.Pin (in2pin, pyb.Pin.OUT_PP)
        #must declare pyb.Pin.board.en_pin in main
        self.tim = pyb.Timer (timer, freq=20000)
        self.ch1 = self.tim.channel (1, pyb.Timer.PWM, pin=self.pinIN1)
        self.ch2 = self.tim.channel (2, pyb.Timer.PWM, pin=self.pinIN2)
        
        
    def set_duty_cycle(self, level):
        '''!
        This method sets duty cycle of motor to a certain
        level. Positive cuase torque in one direction and
        negative causes torque in another
        If the duty cycle is out of the acceptable range, it
        will prin
        @param level    This is the duty cycle/speed on the motor
        '''
        if(abs(level) > 100):
            print('Invalid duty cycle')
            self.ch2.pulse_width_percent (0)
            self.ch1.pulse_width_percent (0)
        else:
            print ('Setting duty cycle to ' + str (level))
            self.pinEN.value(255)
            if(level > 0):
                self.ch2.pulse_width_percent (0)
                self.ch1.pulse_width_percent (abs(level))
            else:
                self.ch1.pulse_width_percent (0)
                self.ch2.pulse_width_percent (abs(level))

            