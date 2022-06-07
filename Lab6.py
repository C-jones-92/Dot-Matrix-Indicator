import RPi.GPIO as GPIO 
import ADC0832_dualChan as ADC
import time
C5 = 37
C3 = 35
C2 = 33
C8 = 16
C7 = 18
C1 = 22
C6 = 32
C4 = 36
CSpin   = 11
DIDOpin = 12
CLKpin  = 13
BTN = 40
DHT11pin = 38
mode = 0
MotorPin_A = 29
MotorPin_B = 31
g_sta =  1
g_dir =  1
speed = 50
pwm_B = 0

def motorStop():
    global MotorPin_A, MotorPin_B, pwm_B
    GPIO.output(MotorPin_A, GPIO.LOW)
    GPIO.output(MotorPin_B, GPIO.LOW)
    pwm_B.stop()

def motor(status, direction, speed):
    global pwm_B
    if status == 1:  # run
        if direction == 1:
            GPIO.output(MotorPin_A, GPIO.HIGH)
            pwm_B.start(100)
            pwm_B.ChangeDutyCycle(100-speed)
        else:
            GPIO.output(MotorPin_A, GPIO.LOW)
            pwm_B.start(0)
            pwm_B.ChangeDutyCycle(speed)
    else:  # stop
        motorStop()
def ButtonPush():
    if(GPIO.input(BTN) == GPIO.LOW)
        time.sleep(1)
        if(GPIO.input(BTN) == GPIO.LOW)
            mode = mode + 1
            Print("Button Pressed. Mode =" mode)
            if(mode == 5)  
                mode = 0

def Voltmeter():
    Rbottom = 10000  #resistor connected below the photoresistor 
    Vcc
    ADC.setup(cs=CSpin,clk=CLKpin,dido=DIDOpin)
    GPIO.setup(C1, GPIO.OUT)
    GPIO.setup(C2, GPIO.OUT)
    GPIO.setup(C3, GPIO.OUT)
    GPIO.setup(C4, GPIO.OUT)
    GPIO.setup(C5, GPIO.OUT)
    GPIO.setup(C6, GPIO.OUT)
    GPIO.setup(C7, GPIO.OUT)
    GPIO.setup(C8, GPIO.OUT)
    GPIO.output(C1, GPIO.HIGH)
    GPIO.output(C2, GPIO.HIGH)
    GPIO.output(C3, GPIO.HIGH)
    GPIO.output(C4, GPIO.HIGH)
    GPIO.output(C5, GPIO.HIGH)
    GPIO.output(C6, GPIO.HIGH)
    GPIO.output(C7, GPIO.HIGH)
    GPIO.output(C8, GPIO.HIGH)
        while True:
            ADCch0 = ADC.getResult(0)
            V0=round(ADCch0 * (Vcc / 255), 2)
            print("ADC Chan0=%03d (%3.2f V)     " % (ADCch0, V0), end='')
            print(63*'\b', end='')
            if(V0 <= 0.625):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.HIGH)
                GPIO.output(C3, GPIO.HIGH)
                GPIO.output(C4, GPIO.HIGH)
                GPIO.output(C5, GPIO.HIGH)
                GPIO.output(C6, GPIO.HIGH)
                GPIO.output(C7, GPIO.HIGH)
                GPIO.output(C8, GPIO.HIGH)
            elif(V0 <= 1.25):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.LOW)
                GPIO.output(C3, GPIO.HIGH)
                GPIO.output(C4, GPIO.HIGH)
                GPIO.output(C5, GPIO.HIGH)
                GPIO.output(C6, GPIO.HIGH)
                GPIO.output(C7, GPIO.HIGH)
                GPIO.output(C8, GPIO.HIGH)
            elif(V0 <= 1.875):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.LOW)
                GPIO.output(C3, GPIO.LOW)
                GPIO.output(C4, GPIO.HIGH)
                GPIO.output(C5, GPIO.HIGH)
                GPIO.output(C6, GPIO.HIGH)
                GPIO.output(C7, GPIO.HIGH)
                GPIO.output(C8, GPIO.HIGH)
            elif(V0 <= 2.5):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.LOW)
                GPIO.output(C3, GPIO.LOW)
                GPIO.output(C4, GPIO.LOW)
                GPIO.output(C5, GPIO.HIGH)
                GPIO.output(C6, GPIO.HIGH)
                GPIO.output(C7, GPIO.HIGH)
                GPIO.output(C8, GPIO.HIGH)
            elif(V0 <= 3.125):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.LOW)
                GPIO.output(C3, GPIO.LOW)
                GPIO.output(C4, GPIO.LOW)
                GPIO.output(C5, GPIO.LOW)
                GPIO.output(C6, GPIO.HIGH)
                GPIO.output(C7, GPIO.HIGH)
                GPIO.output(C8, GPIO.HIGH)
            elif(V0 <= 3.75):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.LOW)
                GPIO.output(C3, GPIO.LOW)
                GPIO.output(C4, GPIO.LOW)
                GPIO.output(C5, GPIO.LOW)
                GPIO.output(C6, GPIO.LOW)
                GPIO.output(C7, GPIO.HIGH)
                GPIO.output(C8, GPIO.HIGH)
            elif(V0 <= 4.375):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.LOW)
                GPIO.output(C3, GPIO.LOW)
                GPIO.output(C4, GPIO.LOW)
                GPIO.output(C5, GPIO.LOW)
                GPIO.output(C6, GPIO.LOW)
                GPIO.output(C7, GPIO.LOW)
                GPIO.output(C8, GPIO.HIGH)
            elif(V0 <= 5):
                GPIO.output(C1, GPIO.LOW)
                GPIO.output(C2, GPIO.LOW)
                GPIO.output(C3, GPIO.LOW)
                GPIO.output(C4, GPIO.LOW)
                GPIO.output(C5, GPIO.LOW)
                GPIO.output(C6, GPIO.LOW)
                GPIO.output(C7, GPIO.LOW)
                GPIO.output(C8, GPIO.LOW)       
            time.sleep(0.1)

def Temperature():
    while True:
        time.sleep(1)  # we cannot read the DHT11 faster than 1 per second
        GPIO.setup(DHT11pin, GPIO.OUT)   # send a pulse to DHT11
        GPIO.output(DHT11pin, GPIO.LOW)
        time.sleep(0.02)
        GPIO.output(DHT11pin, GPIO.HIGH)  # 20ms pulse to request a reading
        GPIO.setup(DHT11pin, GPIO.IN)     # start listening to the sensor
        while GPIO.input(DHT11pin) == GPIO.LOW:
            continue
        while GPIO.input(DHT11pin) == GPIO.HIGH:
            continue
        j=0
        SensorReading=[]  # this will contain the bits read
        while j < 40:
            k = 0
            while GPIO.input(DHT11pin) == GPIO.LOW:
                continue
            while GPIO.input(DHT11pin) == GPIO.HIGH:
                k += 1
                if k > 100:
                    break
            if k < 8:
                SensorReading.append(0)
            else:
                SensorReading.append(1)
            j += 1
        print(f"Raw sensor reading bits ={SensorReading} ...",end='')
        print("  I am parsing these bits now...")
        # parse 5 bytes: temperature, temp frac, humidity, humid frac, checksum
        HumidityDecimalBits        = SensorReading[0:8]
        HumidityFractionalBits     = SensorReading[8:16]
        TemperatureDecimalBits     = SensorReading[16:24]
        TemperatureFractionalBits  = SensorReading[24:32]
        ErrorCheckBits             = SensorReading[32:40]

        HumidDec  = 0
        HumidFrac = 0
        TempDec   = 0
        TempFrac  = 0
        checksum = 0
        for i in range(8):
            HumidDec  += HumidityDecimalBits[i] * (2 ** (7 - i))
            HumidFrac += HumidityFractionalBits[i] * (2 ** (7 - i))
            TempDec   += TemperatureDecimalBits[i] * (2 ** (7 - i))
            TempFrac  += TemperatureFractionalBits[i] * (2 ** (7 - i))
            checksum  += ErrorCheckBits[i] * (2 ** (7 - i))
        chk = HumidDec + HumidFrac + TempDec + TempFrac
        TempC=TempDec+TempFrac/100.00
        TempF=round(TempC*1.8+32.0,2)
        if chk != checksum:
            print(f".....Checksum Error!!!    checksum={checksum}")
        else:
            print(f"    Temperature = {TempC}\u00b0C   =  {TempF}\u00b0F")
            print(f"    Humidity    = {HumidDec}.{HumidFrac} %")    
        print()
        time.sleep(2) # this is just to avoid flooding the screen with readings

def Tachometer():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(MotorPin_A, GPIO.OUT)
    GPIO.setup(MotorPin_B, GPIO.OUT)
    pwm_B = GPIO.PWM(MotorPin_B, 2000)        # create PWM with f=2kHz
    motorStop()
    
    while True:
        SP=int(input("Enter speed (0=stop, -100..-1=reverse and +1..+100=forward): "))
        if(SP==0):
            g_sta=0
        else:
            g_sta=1
        if(SP<0):
            g_dir=1
        else:
            g_dir=0
        if(SP<-100):
            SP = -100
        elif (SP>100):
            SP = +100
        speed=abs(SP)
        motor(g_sta, g_dir, speed)


try:  
    while True:
    
        ButtonPush()
        
        if(mode == 1)
            print("You are now in Voltmeter mode")
            Voltmeter()
            time.sleep(1)
     
        elif(mode == 2)
            print("You are now in Temperature mode")
            Temperature()
            time.sleep(1)
            
        elif(mode == 3)
            print("You are now in Humidty mode")
            Temperature()
            time.sleep(1)
            
        elif(mode == 4)
            print("You are now in Tachometer mode")
            Tachometer()
            time.sleep(1)
        
    
        

except KeyboardInterrupt:
    print("\nLab 6 is done. BYE.")
    GPIO.cleanup()
