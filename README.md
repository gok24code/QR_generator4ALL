# QR Creator

Bu proje, terminal üzerinden QR kodları oluşturmanıza olanak tanıyan bir Bash scripti içerir. Kullanıcıdan alınan metni QR kodu olarak terminalde görüntüler.

## Linux Gereksinimleri

Bu scriptin çalışması için aşağıdaki yazılımların sisteminizde kurulu olması gerekir:

- `qrencode` (QR kodu oluşturmak için kullanılır)
- Bash terminali

## Kurulum

### Arch Linux

```bash
sudo pacman -S qrencode
```

### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install qrencode
```

### Fedora

```bash
sudo dnf install qrencode
```

### macOS

```bash
brew install qrencode
```

## Kullanım

1. Scripti çalıştırılabilir hale getirin:

   ```bash
   chmod +x generate_qr.sh
   ```

2. Scripti çalıştırın:

   ```bash
   ./generate_qr.sh
   ```

3. Script sizden bir metin girmenizi isteyecek. Girdiğiniz metin QR kodu olarak terminalde görüntülenecektir.

## Örnek Çalıştırma

```bash
$ ./generate_qr.sh
QR kodu oluşturmak için bir metin girin: Merhaba Dünya

[YOUR GENERATED CODE IMAGE]
QR kodu başarıyla oluşturuldu!
```

### Windows

Windows üzerinde bu scripti çalıştırmak için WSL (Windows Subsystem for Linux) kullanabilirsiniz. WSL üzerinde uygun bir Linux dağıtımı kurduktan sonra yukarıdaki adımları takip ederek `qrencode` aracını yükleyebilirsiniz.

### Windows (Python ile)

Windows kullanıcıları için, aşağıdaki Python scriptini kullanabilirsiniz:

1. Python'un sisteminizde kurulu olduğundan emin olun. Python'u [Python.org](https://www.python.org/downloads/) adresinden indirebilirsiniz.

2. Gerekli Python kütüphanesini yükleyin:

   ```bash
   pip install qrcode
   ```

3. Aşağıdaki powershell scriptini çalıştırın:

   ```powershell
    python generator.py
   ```

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue oluşturun.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
