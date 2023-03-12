import qrcode
import os

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = "https://www.youtube.com/"  # replace with your video URL
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code and save it
img = qr.make_image(fill_color="black", back_color="white")
img_path = "my_qr_code.png"
img.save(img_path)

# Open the image using the default image viewer
os.startfile(img_path)
