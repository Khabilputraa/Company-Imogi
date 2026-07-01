from django.contrib import admin
from unfold.admin import ModelAdmin

from imogi.admin_mixins import RowDeleteMixin

from .models import Material


@admin.register(Material)
class MaterialAdmin(RowDeleteMixin, ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "link")

    fieldsets = (
        (
            "Materi",
            {
                "description": "Isi SALAH SATU: unggah File (mis. PDF) ATAU isi Tautan eksternal "
                               "(YouTube/TikTok/Drive). Jika keduanya diisi, File yang dipakai.",
                "fields": ("title", "file", "link"),
            },
        ),
        (
            "Pengaturan",
            {
                "fields": ("order", "is_active"),
            },
        ),
    )
