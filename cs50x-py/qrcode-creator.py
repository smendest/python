# QR-code creator
import os
import qrcode
from sys import argv

if len(argv) == 2:
    img = qrcode.make(argv[1])
    img.save("qr.png", "PNG")
else:
    print("Error: must add the url as the only argument")

# Static example:
# img = qrcode.make("https://cs50.harvard.edu/x/2025/weeks/6/")
