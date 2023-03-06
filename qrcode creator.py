import qrcode
import qrcode.image.svg
from PIL import Image

export_format = input("Esportare in SVG o PNG? ").lower()

if export_format == "svg":
    method = "basic"
    input_data = input("URL del sito: ")
    input_name = str(input("Nome del file: "))
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(input_data, image_factory = factory)
    img.save(input_name+".svg")

elif export_format == "png":
    input_data = input("URL del sito: ")
    input_name = str(input("Nome del file: "))
    img = qrcode.make(input_data)
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save(input_name+".png")
