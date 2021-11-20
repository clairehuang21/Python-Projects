import qrcode

link = qrcode.make("https://www.google.com/")
link.save("QRCode.jpg")