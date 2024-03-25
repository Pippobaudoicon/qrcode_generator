import qrcode
import qrcode.image.svg
from PIL import Image

# Function to generate QR code for WiFi connection
def generate_wifi_qr_code(ssid, password, security='WPA', hidden=False):
    wifi_config = f"WIFI:S:{ssid};T:{security};P:{password};H:{'true' if hidden else 'false'};"
    img = qrcode.make(wifi_config)
    return img

def save_qr_code(img, filename, format='png'):
    if format.lower() == 'svg':
        img.save(filename + ".svg")
    else:
        img.save(filename + ".png")

def main():
    export_format = input("Export to SVG, PNG or WIFI? ").lower()

    if export_format == "svg":
        input_data = input("URL of the website: ")
        input_name = input("File name: ")
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(input_data, image_factory=factory)
        save_qr_code(img, input_name, 'svg')
        print("QR code saved as SVG.")

    elif export_format == "png":
        input_data = input("URL of the website: ")
        input_name = input("File name: ")
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=20,
            border=2,
        )
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        save_qr_code(img, input_name, 'png')
        print("QR code saved as PNG.")

    elif export_format == "wifi":
        wifi_ssid = input("WiFi SSID: ")
        wifi_password = input("WiFi password: ")
        wifi_security = input("Security type (WPA, WEP, WPA2): ").upper()
        wifi_hidden = input("Hidden network? (yes/no): ").lower()
        if wifi_hidden == "yes":
            wifi_hidden = True
        else:
            wifi_hidden = False
        img = generate_wifi_qr_code(wifi_ssid, wifi_password, wifi_security, wifi_hidden)
        input_name = input("File name: ")
        save_qr_code(img, input_name, 'png')
        print("WiFi QR code saved as PNG.")

if __name__ == "__main__":
    main()
