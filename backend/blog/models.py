from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Nama kategori", max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True, blank=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField("Judul", max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True,
                            help_text="Otomatis dari judul bila dikosongkan.")
    author = models.CharField("Penulis", max_length=100, default="Tim Imogi Indonesia")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="posts", verbose_name="Kategori",
    )
    image = models.ImageField("Gambar utama", upload_to="blog/", blank=True)
    excerpt = models.TextField("Ringkasan", max_length=300,
                               help_text="Teks pendek yang tampil di kartu daftar artikel.")
    content = models.TextField("Isi artikel",
                               help_text="Tulis & format dengan toolbar (tebal, judul, daftar, tautan) — tanpa perlu kode.")
    is_published = models.BooleanField("Tayang", default=True)
    published_at = models.DateTimeField("Tanggal tayang", default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Artikel"
        verbose_name_plural = "Artikel"
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])

    def __str__(self):
        return self.title
