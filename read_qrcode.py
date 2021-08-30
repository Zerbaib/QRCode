import cv2

d = cv2.QRCodeDetector()

print("ou se trouve le QRCode (met le chemin ici)")
chemin = input()

val, points, qrcode, = d.detectAndDecode(cv2.imread(chemin))

print("Voila ce que contient le qrcode: ")
print(val)
input()