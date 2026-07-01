from django.contrib import admin
from unfold.admin import ModelAdmin

from imogi.admin_mixins import RowDeleteMixin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(RowDeleteMixin, ModelAdmin):
    list_display = ("name", "company", "email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    list_editable = ("is_read",)
    search_fields = ("name", "company", "email", "subject", "message")
    readonly_fields = ("name", "company", "email", "subject", "message", "created_at")

    fieldsets = (
        (
            "Pengirim",
            {
                "description": "Identitas pengirim pesan dari form kontak situs.",
                "fields": ("name", "company", "email", "created_at"),
            },
        ),
        (
            "Isi Pesan",
            {
                "fields": ("subject", "message"),
            },
        ),
        (
            "Status",
            {
                "fields": ("is_read",),
            },
        ),
    )

    def has_add_permission(self, request):
        # Messages only come from the website form, not added manually.
        return False
