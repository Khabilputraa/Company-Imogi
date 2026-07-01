from django.urls import reverse_lazy

from blog.models import BlogPost
from contact.models import ContactMessage
from products.models import Product


def dashboard_callback(request, context):
    """Data untuk dashboard admin (kartu statistik + ringkasan)."""
    unread = ContactMessage.objects.filter(is_read=False).count()

    context.update({
        "imogi_stats": [
            {
                "label": "Produk",
                "value": Product.objects.count(),
                "icon": "inventory_2",
                "link": reverse_lazy("admin:products_product_changelist"),
            },
            {
                "label": "Artikel",
                "value": BlogPost.objects.count(),
                "icon": "newspaper",
                "link": reverse_lazy("admin:blog_blogpost_changelist"),
            },
            {
                "label": "Pesan Kontak",
                "value": ContactMessage.objects.count(),
                "sub": f"{unread} belum dibaca" if unread else "Semua dibaca",
                "icon": "mail",
                "link": reverse_lazy("admin:contact_contactmessage_changelist"),
            },
        ],
        "imogi_recent_messages": ContactMessage.objects.order_by("-created_at")[:5],
        "imogi_recent_posts": BlogPost.objects.order_by("-published_at")[:5],
    })
    return context
