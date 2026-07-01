# Imogi Indonesia — Backend (Django)

Backend untuk website company profile Imogi Indonesia. Menangani:

- **Form Kontak** → simpan ke database + kirim email notifikasi.
- **Newsletter** → tangkap email pelanggan.
- **Blog (CMS)** → kelola artikel lewat Django admin; halaman `/blog/` & `/blog/<slug>/` dinamis.

Frontend (HTML + `assets/`) berada di folder induk (`../`) dan di-render Django sebagai template.

## Menjalankan (development)

```bash
# dari folder backend/
.venv/Scripts/python.exe manage.py runserver
```

Buka:
- Situs:  http://127.0.0.1:8000/
- Blog:   http://127.0.0.1:8000/blog/
- Admin:  http://127.0.0.1:8000/admin/  (user: `admin`, pass: `admin123`)

> Catatan: situs kini dijalankan lewat Django (bukan dibuka via `file://`).
> Buka di `http://127.0.0.1:8000`, bukan klik dua kali `index.html`.

## Perintah berguna

```bash
.venv/Scripts/python.exe manage.py makemigrations
.venv/Scripts/python.exe manage.py migrate
.venv/Scripts/python.exe manage.py createsuperuser
```

## Struktur

- `imogi/`       — konfigurasi proyek (settings, urls)
- `blog/`        — model Artikel & Kategori, view list/detail
- `contact/`     — form kontak (model + endpoint `/contact/submit/`)
- `newsletter/`  — langganan (model + endpoint `/newsletter/subscribe/`)
- `templates/`   — base.html + template blog dinamis
- `db.sqlite3`   — database
- `media/`       — file upload (gambar artikel)

## Email

Default (development): email dicetak ke **terminal** (console backend).
Untuk produksi, aktifkan SMTP di `imogi/settings.py` (lihat bagian Email),
dan ubah `CONTACT_NOTIFY_EMAIL` ke alamat penerima asli.

## Produksi (ringkas)

1. `DEBUG = False`, isi `ALLOWED_HOSTS`, ganti `SECRET_KEY`.
2. `python manage.py collectstatic` (lalu serve `staticfiles/` & `media/`).
3. Jalankan via WSGI (gunicorn/uwsgi) + reverse proxy (nginx).
