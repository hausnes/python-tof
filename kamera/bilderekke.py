from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

for x in range(1,4): # Dette blir altså køyrt 3 stk. gonger (1, 2 og 3)
    filnavn = str(x) + ".jpg"
    picam2.start_and_capture_file("/home/pi/hausnes/" + filnavn)
    time.sleep(2)