# Django Kişisel Site

Django tabanlı kişisel blog sitesi.

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. `.env` dosyasını oluşturun (`.env.example` dosyasından kopyalayarak):
```bash
cp .env.example .env
```

3. `.env` dosyasında SECRET_KEY'i güncelleyin. Yeni bir secret key oluşturmak için:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

4. Veritabanı migrasyonlarını çalıştırın:
```bash
python manage.py migrate
```

5. Statik dosyaları toplayın:
```bash
python manage.py collectstatic
```

6. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

## Güvenlik

- **SECRET_KEY**: Production ortamında mutlaka `.env` dosyasından yüklenmeli ve güvenli bir değer kullanılmalıdır.
- **DEBUG**: Production ortamında `False` olmalıdır.
- **ALLOWED_HOSTS**: Production ortamında domain isimlerinizi eklemelisiniz.

## Ortam Değişkenleri

Proje aşağıdaki ortam değişkenlerini destekler:

- `SECRET_KEY`: Django secret key (zorunlu, production için)
- `DEBUG`: Debug modu (varsayılan: True)
- `ALLOWED_HOSTS`: İzin verilen host isimleri (virgülle ayrılmış)
