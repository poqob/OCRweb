# OCR Uygulaması - Docker ile Çalıştırma

Bu proje, kullanıcıların yüklediği görüntüleri işleyerek metin içeriğini çıkaran basit bir OCR (Optical Character Recognition) uygulamasıdır. Proje Flask web çatısı kullanılarak geliştirilmiştir ve Docker ile çalıştırılabilir hale getirilmiştir.

## Gereksinimler

- Docker
- Docker Compose (opsiyonel)

## Kurulum

1. Bu GitHub deposunu klonlayın:

```
git clone https://github.com/poqob/OCRweb.git
cd OCRweb
```

2. Docker imajını oluşturun:

```
docker build -t OCRweb .
```

## Çalıştırma

Docker imajını oluşturduktan sonra, uygulamayı aşağıdaki komutla başlatabilirsiniz:

```
docker run -p 5000:5000 OCRweb
```

Tarayıcınızda `http://localhost:5000` adresine giderek OCR uygulamasının çalıştığını görebilirsiniz. Görüntü yükleyerek metin içeriğini çıkartabilirsiniz.

## Docker Compose ile Çalıştırma (Opsiyonel)

Eğer Docker Compose yüklüyse, projeyi daha kolay başlatabilirsiniz:

```
docker-compose up
```

Bu komutla hem Flask uygulaması hem de gerekli bağımlılıklar otomatik olarak çalıştırılacaktır.

## Notlar

- Proje ana dizinindeki `src` klasörü altında Flask uygulaması bulunmaktadır.
- `requirements.txt` dosyasında gerekli Python kütüphaneleri ve sürümleri listelenmiştir.
- OCR işlemleri için Tesseract OCR kütüphanesini kullanıyoruz. Docker imajı, bu kütüphaneyi içerir ve uygulama içinde doğru şekilde yapılandırılmıştır.
- build.bat, proje yaratımını yapar.
- destroy_all_containers.bat, çalışan-çalışmayan tüm konteynerleri durdurur ve siler.
- run_new_container.bat, yeni konteyner yürütür.
- start_last_container.bat, durdurulmuş son konteyneri başlatır.
- stop_all_containers.bat, çalışan bütün konteynerleri durdurur.

## Katkı

Her türlü katkı ve öneriler için açığız. Lütfen bir işlem başlatmadan önce GitHub üzerinden bir konu açın.

---


## Kullanım: Youtube 

[OCR-Web App Youtube Link](https://youtu.be/HaXJhpfLJZk)
