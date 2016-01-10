import os
import time
import picamera
import RPi.GPIO
import requests
from your_info import ngrok_url

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2, RPi.GPIO.IN,
    pull_up_down=RPi.GPIO.PUD_UP)
camera = picamera.PiCamera()
camera.resolution=(320, 240)
FILE_DIR = '/home/pi/projects/doorbell/static/'

def send_file(filename):
    saved_file = open(FILE_DIR + filename, 'r')
    r = requests.post(ngrok_url + '/incoming', files={filename: saved_file})
    print('sending file: ' + filename)

def Ring():
    filename="Ring_%s.jpg"%time.strftime("%Y%m%d-%H%M%S")
    camera.capture(
        os.path.join(FILE_DIR, 
        filename
        )
    )
    os.system("mpg321 ring.mp3")
    print('ringing...')
    send_file(filename)
    while RPi.GPIO.input(2) == RPi.GPIO.LOW:
        pass

while True:
    if RPi.GPIO.input(2) == RPi.GPIO.LOW:
        Ring()
