from picamera2 import Picamera2, Preview
from libcamera import Transform
from datetime import datetime
picam2 = Picamera2()
#picam2.start_preview(Preview.QTGL, x=100, y=200, width=800, height=600, transform=Transform(hflip=1)) # Om du ønsker å speilvende biletet, kan du legge til transform=Transform(hflip=1)
#picam2.start_preview(Preview.NULL)
filnavn = str(datetime.now()) + ".jpg"
picam2.start_and_capture_file(filnavn)