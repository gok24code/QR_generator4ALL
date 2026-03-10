#!/bin/bash

# Kullanıcıdan QR kodu için metin al
read -p "QR kodu oluşturmak için bir metin girin: " input_text

# Metin boş mu kontrol et
if [ -z "$input_text" ]; then
  echo "Hata: Metin boş olamaz."
  exit 1
fi

# QR kodunu terminale yazdır
qrencode -t ANSIUTF8 "$input_text"

# Başarı mesajı
echo "QR kodu başarıyla oluşturuldu!"