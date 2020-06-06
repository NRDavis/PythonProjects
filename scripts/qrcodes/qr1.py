import qrcode
img = qrcode.make('Some data here')     # This works for generating a relevant QR Code
img.show()
img.save("qrimage.png")


'''
import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
    )


data = "The Data that you need to store in the QR Code"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()       # create an image from the QR Code instance

img.save("image.jpg")   # supports .png, .bmp, .jpeg, etc

https://ourcodeworld.com/articles/read/554/how-to-create-a-qr-code-image-or-svg-in-python

'''