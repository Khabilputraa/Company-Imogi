from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Testimonial(models.Model):
    name = models.CharField("Nama", max_length=120)
    role = models.CharField("Jabatan", max_length=120,
                            help_text="Contoh: Direktur Operasional")
    company = models.CharField("Perusahaan", max_length=150,
                               help_text="Contoh: PT Tiga Perkasa Teknik")
    photo = models.ImageField("Foto", upload_to="testimoni/",
                              help_text="Foto orang yang memberi testimoni.")
    rating = models.PositiveSmallIntegerField(
        "Rating", default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Jumlah bintang (1–5).")
    quote = models.TextField("Kutipan testimoni")
    order = models.PositiveIntegerField("Urutan", default=0,
                                        help_text="Makin kecil makin awal.")
    is_active = models.BooleanField("Tampilkan", default=True)

    class Meta:
        verbose_name = "Testimoni"
        verbose_name_plural = "Testimoni"
        ordering = ["order", "id"]

    @property
    def filled_stars(self):
        return range(self.rating)

    @property
    def empty_stars(self):
        return range(5 - self.rating)

    def __str__(self):
        return f"{self.name} — {self.company}"
