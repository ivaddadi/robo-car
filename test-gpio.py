import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.output(21,True)
GPIO.output(22,False)
GPIO.output(23,True)
GPIO.output(24,False)
