from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("Nama", max_length=120)
    company = models.CharField("Perusahaan", max_length=150, blank=True)
    email = models.EmailField("Email")
    subject = models.CharField("Subjek", max_length=200, blank=True)
    message = models.TextField("Pesan")
    is_read = models.BooleanField("Sudah dibaca", default=False)
    created_at = models.DateTimeField("Dikirim pada", auto_now_add=True)

    class Meta:
        verbose_name = "Pesan Kontak"
        verbose_name_plural = "Pesan Kontak"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject or '(tanpa subjek)'}"
