from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from imogi.admin_mixins import RowDeleteMixin

from .models import Client


@admin.register(Client)
class ClientAdmin(RowDeleteMixin, ModelAdmin):
    list_display = ("logo_preview", "name", "order", "is_active")
    list_display_links = ("name",)
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)

    @admin.display(description="Logo")
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="height:34px;max-width:130px;object-fit:contain;" />',
                obj.logo.url,
            )
        return "—"
