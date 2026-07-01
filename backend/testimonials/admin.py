from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from imogi.admin_mixins import RowDeleteMixin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(RowDeleteMixin, ModelAdmin):
    list_display = ("photo_preview", "name", "company", "rating", "order", "is_active")
    list_display_links = ("name",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "rating")
    search_fields = ("name", "company", "quote")

    fieldsets = (
        ("Identitas", {
            "fields": ("name", "role", "company", "photo"),
        }),
        ("Isi Testimoni", {
            "fields": ("rating", "quote"),
        }),
        ("Pengaturan", {
            "fields": ("order", "is_active"),
        }),
    )

    @admin.display(description="Foto")
    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="height:40px;width:40px;border-radius:8px;object-fit:cover;" />',
                obj.photo.url,
            )
        return "—"
