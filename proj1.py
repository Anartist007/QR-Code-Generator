#below is the code for creating basic QR code
import qrcode as qr
img=qr.make("https://youtu.be/gPpQNzQP6gE?si=iiaZIXk5Zm7m3Dzj")
img.save("checkitout.jpg")
#below is the code for generating a QR code with taking into consideration the error correction
import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)
qr.add_data("https://1drv.ms/i/c/4597b7f1e6c72500/Ee_GFz68M_NCoAd85AMUWgkB6UqHQ5c-JBfbbOKySlselg?e=7149yl")
qr.make(fit=True)
img = qr.make_image(fill_color="RED", back_color="white")
img.save("Hi.jpg")
