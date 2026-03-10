import qrcode
import os

def create_and_open_qr(link):
    try:
        # QR kodu oluştur
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        # QR kodunu bir görüntü dosyasına kaydet
        img = qr.make_image(fill_color="black", back_color="white")
        qr_file = "qr_code.png"
        img.save(qr_file)

        # QR kodunu aç
        os.system(f"xdg-open {qr_file}")
        print(f"QR kodu oluşturuldu ve {qr_file} dosyası açıldı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    link = input("Bir link girin: ")
    create_and_open_qr(link)