from django.db import models


class Material(models.Model):
    title = models.CharField("Judul materi", max_length=150)
    file = models.FileField(
        "File materi", upload_to="materi/", blank=True,
        help_text="Unggah file materi (mis. PDF). Kosongkan jika memakai tautan.")
    link = models.CharField(
        "Tautan eksternal", max_length=300, blank=True,
        help_text="Link YouTube/TikTok/Drive, dll. Kosongkan jika mengunggah file.")
    order = models.PositiveIntegerField("Urutan", default=0,
                                        help_text="Makin kecil makin awal.")
    is_active = models.BooleanField("Tampilkan", default=True)

    class Meta:
        verbose_name = "Materi"
        verbose_name_plural = "Materi"
        ordering = ["order", "id"]

    @property
    def get_url(self):
        """URL tujuan materi: file yang diunggah didahulukan, lalu tautan."""
        if self.file:
            return self.file.url
        return self.link or "#"

    def __str__(self):
        return self.title
