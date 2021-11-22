# import qrcode
# from qrcode.image.styledpil import StyledPilImage
# from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
# from qrcode.image.styles.colormasks import RadialGradiantColorMask
#
# #link = qrcode.make("https://www.google.com/")
# #link.save("QRCode.jpg")
#
# qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
# qr.add_data('Some data')
#
# img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
# img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
# img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="C:/Users/Images/purdue.png")
# img_1.save("Image.jpg")
# img_2.save("Image2.jpg")
# img_3.save("Image3.jpg")

cdict2 = {'red':   [(0.0,  1.0, 1.0),
                    (1.0,  1.0, 1.0),
                    (1.0,  1.0, 1.0)],
         'green': [(0.0,  1.0, 1.0),
                   (1.0, 0.0, 0.0),
                   (1.0,  0.0, 0.0)],
     'blue':  [(0.0,  1.0, 1.0),
               (1.0,  0.0, 0.0),
               (1.0,  0.0, 0.0)]}

# import modules
import qrcode
from PIL import Image

# taking image which user wants
# in the QR code center
#linkOfImage = input("What's the link of the image?")
Logo_link = "C:/Users/Images/bobabears2.png"

logo = Image.open(Logo_link)

# taking base width
basewidth = 400

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
link = input("What is the url for you QRCode?: ")
url = str(link)

# addingg URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'goldenrod'

# adding color to QR code
#QRimg = QRcode.make_image(
	#fill_color=QRcolor, back_color="black").convert('RGB')

QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color= "whitesmoke").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('newQRCode.jpg')

print('QR code generated!')

#List of colors in this qrcode: https://matplotlib.org/stable/gallery/color/named_colors.html
