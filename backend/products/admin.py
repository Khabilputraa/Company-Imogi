from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from imogi.admin_mixins import RowDeleteMixin

from .models import Product


@admin.register(Product)
class ProductAdmin(RowDeleteMixin, ModelAdmin):
    list_display = ("name", "subtitle", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "subtitle", "description")
    prepopulated_fields = {"slug": ("name",)}

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == "detail" and formfield is not None:
            # Editor visual untuk penjelasan lengkap (tanpa menulis kode).
            formfield.widget = WysiwygWidget()
        return formfield

    fieldsets = (
        (
            "Informasi Produk",
            {
                "description": "Nama, tautan (slug), subjudul, ikon/logo produk. "
                               "Bila 'Logo produk' diunggah, ia menggantikan ikon.",
                "fields": ("name", "slug", "subtitle", "icon", "logo"),
            },
        ),
        (
            "Konten Beranda",
            {
                "description": "Deskripsi singkat & fitur yang tampil di kartu beranda.",
                "fields": ("description", "features"),
            },
        ),
        (
            "Halaman Detail Produk",
            {
                "description": "Gambar besar & penjelasan lengkap (manfaat, fungsi, cara kerja) "
                               "yang tampil di halaman /produk/<slug>/.",
                "fields": ("image", "detail"),
            },
        ),
        (
            "Pengaturan",
            {
                "fields": ("order", "is_active"),
            },
        ),
    )
