import RPi.GPIO as GPIO
import time
from datetime import datetime
from enum import Enum

class Mode(Enum):
    ERROR="ERROR"
    DEBUG="DEBUG"
    INFO="INFO"

def Log(content: str,mode: Mode):
    filename = "run.log"
    content_to_append = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"{mode.value}:{content_to_append}:{content}\n"
    # open the file in append mode, creates if it dosen't exist
    with open(filename, 'a') as file:
        file.write(formatted_text)


GPIO.setmode(GPIO.BCM)
pin=3
ontime=120
offtime=60

GPIO.setup(pin,GPIO.OUT)

try:
    while True:
        GPIO.output(pin,GPIO.LOW)
        Log("Relay on",Mode.INFO)
        

        time.sleep(ontime)

        GPIO.output(pin,GPIO.HIGH)
        Log("Relay off",Mode.INFO)

        time.sleep(offtime)

except KeyboardInterrupt:
    GPIO.cleanup()
