# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 

selectURL = input("pleas enter the url: ")
  
# String which represent the QR code 
s = selectURL
  
# Generate QR code 
url = pyqrcode.create(s) 
 
url.svg("QRcodder.svg", scale = 8)
print("Your URL is https://"+selectURL);
print("Pleas check the ' QRcodder.svg ' file")
