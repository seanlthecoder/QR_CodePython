import qrcode

# this is a comment

data = 'Don\'t forget to subscribe'


qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = 'red', back_color = 'white')


img.save('C:/Users/Sean Lester Durham/Desktop/QRCodeFiles/sean\'sQRCode1.png')