from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField("Nama produk", max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True,
                            help_text="Otomatis dari nama bila dikosongkan.")
    subtitle = models.CharField("Subjudul", max_length=150,
                                help_text="Contoh: Manajemen Bisnis Retail")
    description = models.TextField("Deskripsi singkat",
                                   help_text="Teks pendek yang tampil di kartu beranda.")
    icon = models.CharField("Ikon", max_length=60, default="bi bi-box-seam",
                            help_text="Kelas Bootstrap Icons (dipakai bila Logo dikosongkan). "
                                      "Contoh: bi bi-box-seam, bi bi-tools, bi bi-shop")
    logo = models.ImageField("Logo produk", upload_to="produk/logo/", blank=True,
                             help_text="Opsional. Bila diisi, menggantikan ikon di kartu & halaman detail.")
    image = models.ImageField("Gambar halaman detail", upload_to="produk/", blank=True,
                              help_text="Gambar besar di halaman detail produk (opsional).")
    features = models.TextField(
        "Fitur Utama", blank=True,
        help_text="Satu fitur per baris (tekan Enter untuk fitur berikutnya).")
    detail = models.TextField(
        "Penjelasan Lengkap", blank=True,
        help_text="Manfaat, fungsi, dan cara kerja aplikasi — tampil di halaman detail produk.")
    order = models.PositiveIntegerField("Urutan", default=0,
                                        help_text="Makin kecil makin awal.")
    is_active = models.BooleanField("Tampilkan", default=True)

    class Meta:
        verbose_name = "Produk"
        verbose_name_plural = "Produk"
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:120]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:detail", args=[self.slug])

    @property
    def feature_list(self):
        """Daftar fitur dari teks (satu per baris), tanpa baris kosong."""
        return [f.strip() for f in self.features.splitlines() if f.strip()]

    @property
    def anchor_id(self):
        """ID anchor untuk kartu & link dropdown (mis. produk-imogi-retail)."""
        return f"produk-{self.slug}"

    def __str__(self):
        return self.name
