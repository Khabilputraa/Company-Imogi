from django.db import models


class Client(models.Model):
    name = models.CharField("Nama klien", max_length=120)
    logo = models.ImageField("Logo", upload_to="klien/",
                             help_text="Logo klien. Disarankan PNG latar transparan.")
    website = models.URLField("Website", blank=True,
                              help_text="Opsional — tautan ke situs klien.")
    order = models.PositiveIntegerField("Urutan", default=0,
                                        help_text="Makin kecil makin awal.")
    is_active = models.BooleanField("Tampilkan", default=True)

    class Meta:
        verbose_name = "Klien"
        verbose_name_plural = "Klien"
        ordering = ["order", "id"]

    def __str__(self):
        return self.name
