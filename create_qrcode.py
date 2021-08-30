import qrcode
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=3,
    error_correction=ERROR_CORRECT_H,
    box_size=3,
    border=5
)

print("Que va contenir le QRCode")
qrcode = input()

qr.add_data(qrcode)
qr.make(fit=True)

img = qr.make_image(fill_color="black", black_color="white")
img.save("qrcode.png")

print("QRCode générer")
input()
