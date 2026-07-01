from django.contrib import admin
from django.forms import MultiWidget
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.widgets import (
    UnfoldAdminDateWidget,
    UnfoldAdminSplitDateTimeWidget,
    UnfoldAdminTimeWidget,
)

from imogi.admin_mixins import RowDeleteMixin

from .models import BlogPost, Category


class CleanSplitDateTimeWidget(UnfoldAdminSplitDateTimeWidget):
    """Pemilih tanggal + jam, dengan jam format HH:MM (titik dua, tanpa detik)."""

    def __init__(self, attrs=None):
        widgets = [
            UnfoldAdminDateWidget(attrs={"placeholder": "hh-bb-tttt"}),
            UnfoldAdminTimeWidget(attrs={"placeholder": "JJ:MM"}, format="%H:%M"),
        ]
        MultiWidget.__init__(self, widgets, attrs)


@admin.register(Category)
class CategoryAdmin(RowDeleteMixin, ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(BlogPost)
class BlogPostAdmin(RowDeleteMixin, ModelAdmin):
    list_display = ("title", "category", "author", "is_published", "published_at")
    list_filter = ("is_published", "category", "published_at")
    list_editable = ("is_published",)
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if formfield is not None:
            if db_field.name == "published_at":
                formfield.widget = CleanSplitDateTimeWidget()
            elif db_field.name == "content":
                # Editor visual (toolbar): tanpa perlu menulis kode HTML.
                formfield.widget = WysiwygWidget()
        return formfield

    fieldsets = (
        (
            "Informasi Artikel",
            {
                "description": "Judul, tautan (slug), penulis, dan kategori artikel.",
                "fields": ("title", "slug", "author", "category"),
            },
        ),
        (
            "Gambar Utama",
            {
                "description": "Gambar yang tampil di kartu daftar & halaman artikel.",
                "fields": ("image",),
            },
        ),
        (
            "Konten",
            {
                "description": "Ringkasan singkat dan isi lengkap artikel.",
                "fields": ("excerpt", "content"),
            },
        ),
        (
            "Publikasi",
            {
                "description": "Atur status tayang dan tanggal publikasi.",
                "fields": ("is_published", "published_at"),
            },
        ),
    )
