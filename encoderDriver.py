import pyb
class EncoderDriver:
    '''!
    This class impliments and encoder for ME405
    '''
    def __init__(self, in1pin, in2pin, timer):
        '''!
        Creates an encoder driver by initializing GPIO
        pins and reading signal
        @param (doLater)
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
        Handles overflow for the counter
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
        Reads the current position of the motor
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
        

        