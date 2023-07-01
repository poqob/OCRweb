# OCR Uygulaması - Docker ile Çalıştırma

Bu proje, kullanıcıların yüklediği görüntüleri işleyerek metin içeriğini çıkaran basit bir OCR (Optical Character Recognition) uygulamasıdır. Proje Flask web çatısı kullanılarak geliştirilmiştir ve Docker ile çalıştırılabilir hale getirilmiştir.

## Gereksinimler

- Docker
- Docker Compose (opsiyonel)

## Kurulum

1. Bu GitHub deposunu klonlayın:

```
git clone https://github.com/poqob/ocr-web.git
cd ocr-web
```

2. Docker imajını oluşturun:

```
docker build -t ocr-web .
```

## Çalıştırma

Docker imajını oluşturduktan sonra, uygulamayı aşağıdaki komutla başlatabilirsiniz:

```
docker run -p 5000:5000 ocr-web
```

Tarayıcınızda `http://localhost:5000` adresine giderek OCR uygulamasının çalıştığını görebilirsiniz. Görüntü yükleyerek metin içeriğini çıkartabilirsiniz.

## Docker Compose ile Çalıştırma (Opsiyonel)

Eğer Docker Compose yüklüyse, projeyi daha kolay başlatabilirsiniz:

```
docker-compose up
```

Bu komutla hem Flask uygulaması hem de gerekli bağımlılıklar otomatik olarak çalıştırılacaktır.

## Notlar

- Proje ana dizinindeki `app` klasörü altında Flask uygulaması bulunmaktadır.
- `requirements.txt` dosyasında gerekli Python kütüphaneleri ve sürümleri listelenmiştir.
- OCR işlemleri için Tesseract OCR kütüphanesini kullanıyoruz. Docker imajı, bu kütüphaneyi içerir ve uygulama içinde doğru şekilde yapılandırılmıştır.

## Katkı

Her türlü katkı ve öneriler için açığız. Lütfen bir işlem başlatmadan önce GitHub üzerinden bir konu açın.

---
