import qrcode
from PIL import Image

link = input("Enter data to be added (URL,text,numbers,anything):")

qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(link)
qr.make()
image=qr.make_image(fill_color='black',back_colour='white')
image.save("YourQRCode.png") #saves image to current directory as "YourQRCode"

print("Image saved successfully")

(Image.open("YourQRCode.png")).show() #displays the qr code


