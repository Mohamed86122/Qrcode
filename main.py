import qrcode


img = qrcode.make("https://github.com/Mohamed86122")

img.save("myQr.jpg")

