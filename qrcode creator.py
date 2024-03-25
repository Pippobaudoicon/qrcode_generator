import qrcode
import qrcode.image.svg
from PIL import Image

# Function to generate QR code for WiFi connection
def generate_wifi_qr_code(ssid, password, security='WPA', hidden=False):
    wifi_config = f"WIFI:S:{ssid};T:{security};P:{password};H:{'true' if hidden else 'false'};"
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    return img

def add_logo_to_qr(img, logo_path=None):
    if logo_path:
        logo = Image.open(logo_path)
        img_w, img_h = img.size
        logo_w, logo_h = logo.size
        logo_size = int(min(img_w, img_h) / 4)
        logo = logo.resize((logo_size, logo_size), Image.BICUBIC)

        # Create a mask for the logo to preserve transparency
        logo_mask = logo.convert("RGBA").split()[3]  

        # Paste the logo onto the QR code with the mask
        pos = ((img_w - logo_size) // 2, (img_h - logo_size) // 2)
        img.paste(logo, pos, mask=logo_mask)
    
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
        logo_path = input("Logo path (leave blank for no logo): ")
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
        img_with_logo = add_logo_to_qr(img, logo_path)
        save_qr_code(img_with_logo, input_name, 'png')
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
        logo_path = input("Logo path: ")  # Path to your logo image
        img_with_logo = add_logo_to_qr(img, logo_path)
        input_name = input("File name: ")
        save_qr_code(img_with_logo, input_name, 'png')
        print("WiFi QR code with logo saved as PNG.")

if __name__ == "__main__":
    main()
