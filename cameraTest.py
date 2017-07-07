import picamera
import os
import os.path
import time
from datetime import datetime

imgFile = "snap.jpg"
camera = picamera.PiCamera()
camera.capture(imgFile)
camera.close()
